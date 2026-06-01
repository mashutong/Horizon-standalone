"""Reddit scraper implementation."""

import asyncio
import calendar
import logging
import os
import re
import time
from datetime import datetime, timezone
from typing import List, Optional

import feedparser
import httpx
from bs4 import BeautifulSoup

from .base import BaseScraper
from ..models import ContentItem, RedditConfig, RedditSubredditConfig, RedditUserConfig, SourceType

logger = logging.getLogger(__name__)

REDDIT_BASE = "https://www.reddit.com"
REDDIT_OAUTH_BASE = "https://oauth.reddit.com"
REDDIT_TOKEN_URL = f"{REDDIT_BASE}/api/v1/access_token"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36 Horizon/1.0 "
    "(+https://github.com/mashutong/Horizon-standalone)"
)


class RedditScraper(BaseScraper):
    """Scraper for Reddit posts and comments."""

    def __init__(self, config: RedditConfig, http_client: httpx.AsyncClient):
        super().__init__(config.model_dump(), http_client)
        self.reddit_config = config
        self.client_id = os.environ.get("REDDIT_CLIENT_ID", "").strip()
        self.client_secret = os.environ.get("REDDIT_CLIENT_SECRET", "").strip()
        self.user_agent = os.environ.get("REDDIT_USER_AGENT", USER_AGENT).strip() or USER_AGENT
        self._access_token: Optional[str] = None
        self._access_token_expires_at = 0.0

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.config.get("enabled", True):
            return []

        tasks = []
        for sub_cfg in self.reddit_config.subreddits:
            if sub_cfg.enabled:
                tasks.append(self._fetch_subreddit(sub_cfg, since))
        for user_cfg in self.reddit_config.users:
            if user_cfg.enabled:
                tasks.append(self._fetch_user(user_cfg, since))

        if not tasks:
            return []

        results = await asyncio.gather(*tasks, return_exceptions=True)
        items = []
        for result in results:
            if isinstance(result, Exception):
                logger.warning("Error fetching Reddit source: %s", result)
            elif isinstance(result, list):
                items.extend(result)
        return items

    async def _fetch_subreddit(self, cfg: RedditSubredditConfig, since: datetime) -> List[ContentItem]:
        params = {"limit": min(cfg.fetch_limit, 100), "raw_json": 1}
        if cfg.sort in ("top", "controversial"):
            params["t"] = cfg.time_filter

        data = await self._reddit_get(f"/r/{cfg.subreddit}/{cfg.sort}", params)
        if not data:
            return await self._fetch_subreddit_rss(cfg, since)

        posts = [child["data"] for child in data.get("data", {}).get("children", [])
                 if child.get("kind") == "t3"]
        return await self._process_posts(
            posts, since, "subreddit", cfg.subreddit, cfg.min_score
        )

    async def _fetch_subreddit_rss(self, cfg: RedditSubredditConfig, since: datetime) -> List[ContentItem]:
        params = {"limit": min(cfg.fetch_limit, 100)}
        if cfg.sort in ("top", "controversial"):
            params["t"] = cfg.time_filter

        url = f"{REDDIT_BASE}/r/{cfg.subreddit}/{cfg.sort}/.rss"
        data = await self._reddit_feed(url, params)
        if not data:
            return []

        posts = [
            self._parse_rss_entry(entry, subreddit=cfg.subreddit)
            for entry in data.entries
        ]
        posts = [post for post in posts if post]
        return await self._process_posts(
            posts, since, "subreddit", cfg.subreddit, cfg.min_score
        )

    async def _fetch_user(self, cfg: RedditUserConfig, since: datetime) -> List[ContentItem]:
        params = {"limit": min(cfg.fetch_limit, 100), "sort": cfg.sort, "raw_json": 1}
        data = await self._reddit_get(f"/user/{cfg.username}/submitted", params)
        if not data:
            return await self._fetch_user_rss(cfg, since)

        posts = [child["data"] for child in data.get("data", {}).get("children", [])
                 if child.get("kind") == "t3"]
        return await self._process_posts(
            posts, since, "user", cfg.username, min_score=0
        )

    async def _fetch_user_rss(self, cfg: RedditUserConfig, since: datetime) -> List[ContentItem]:
        params = {"limit": min(cfg.fetch_limit, 100), "sort": cfg.sort}
        url = f"{REDDIT_BASE}/user/{cfg.username}/submitted/.rss"
        data = await self._reddit_feed(url, params)
        if not data:
            return []

        posts = [
            self._parse_rss_entry(entry, username=cfg.username)
            for entry in data.entries
        ]
        posts = [post for post in posts if post]
        return await self._process_posts(
            posts, since, "user", cfg.username, min_score=0
        )

    async def _process_posts(
        self,
        posts: list,
        since: datetime,
        subtype: str,
        source_name: str,
        min_score: int,
    ) -> List[ContentItem]:
        valid_posts = []
        comment_tasks = []
        fetch_comments = self.reddit_config.fetch_comments

        for post in posts:
            created = datetime.fromtimestamp(post.get("created_utc", 0), tz=timezone.utc)
            if created < since:
                continue
            score = post.get("score")
            if score is not None and score < min_score:
                continue
            valid_posts.append(post)
            if fetch_comments > 0 and self._has_oauth_config():
                comment_tasks.append(
                    self._fetch_comments(post.get("subreddit", ""), post["id"])
                )
            else:
                comment_tasks.append(self._empty_comments())

        if not valid_posts:
            return []

        all_comments = await asyncio.gather(*comment_tasks, return_exceptions=True)

        items = []
        for post, comments in zip(valid_posts, all_comments):
            if isinstance(comments, Exception):
                comments = []
            item = self._parse_post(post, comments, subtype)
            if item:
                items.append(item)
        return items

    @staticmethod
    async def _empty_comments() -> List[dict]:
        return []

    async def _fetch_comments(self, subreddit: str, post_id: str) -> List[dict]:
        if not self._has_oauth_config():
            return []

        fetch_limit = self.reddit_config.fetch_comments
        params = {"limit": fetch_limit, "depth": 1, "sort": "top", "raw_json": 1}

        data = await self._reddit_get(f"/r/{subreddit}/comments/{post_id}", params)
        if not data or not isinstance(data, list) or len(data) < 2:
            return []

        comments = []
        for child in data[1].get("data", {}).get("children", []):
            if child.get("kind") != "t1":
                continue
            c = child["data"]
            if c.get("body") and not c.get("distinguished") == "moderator":
                comments.append(c)

        comments.sort(key=lambda c: c.get("score", 0), reverse=True)
        return comments[:fetch_limit]

    def _parse_post(self, post: dict, comments: List[dict], subtype: str) -> Optional[ContentItem]:
        post_id = post["id"]
        title = post.get("title", "")
        is_self = post.get("is_self", False)
        subreddit = post.get("subreddit", "")
        discussion_url = f"https://www.reddit.com{post.get('permalink', '')}"

        # For link posts, use the external URL; for self posts, use the discussion URL
        url = discussion_url if is_self else post.get("url", discussion_url)

        author = post.get("author", "unknown")
        created = datetime.fromtimestamp(post.get("created_utc", 0), tz=timezone.utc)

        # Build content
        parts = []
        if post.get("selftext"):
            text = post["selftext"]
            if len(text) > 1500:
                text = text[:1497] + "..."
            parts.append(text)

        if comments:
            parts.append("\n--- Top Comments ---")
            for c in comments:
                commenter = c.get("author", "anon")
                body = c.get("body", "")
                body = body.strip()
                if len(body) > 500:
                    body = body[:497] + "..."
                score = c.get("score", 0)
                parts.append(f"[{commenter} ({score} pts)]: {body}")

        content = "\n\n".join(parts)

        return ContentItem(
            id=self._generate_id("reddit", subtype, post_id),
            source_type=SourceType.REDDIT,
            title=title,
            url=url,
            content=content,
            author=author,
            published_at=created,
            metadata={
                "score": post.get("score"),
                "upvote_ratio": post.get("upvote_ratio"),
                "num_comments": post.get("num_comments", 0),
                "subreddit": subreddit,
                "is_self": is_self,
                "flair": post.get("link_flair_text"),
                "discussion_url": discussion_url,
                "score_unknown": post.get("score") is None,
            },
        )

    def _has_oauth_config(self) -> bool:
        return bool(self.client_id and self.client_secret)

    async def _get_access_token(self) -> Optional[str]:
        if not self._has_oauth_config():
            return None
        if self._access_token and time.monotonic() < self._access_token_expires_at - 60:
            return self._access_token

        try:
            response = await self.client.post(
                REDDIT_TOKEN_URL,
                data={"grant_type": "client_credentials"},
                auth=(self.client_id, self.client_secret),
                headers={"User-Agent": self.user_agent},
            )
            response.raise_for_status()
            payload = response.json()
            token = payload.get("access_token")
            if not token:
                logger.warning("Reddit OAuth token response did not include access_token")
                return None

            expires_in = int(payload.get("expires_in", 3600))
            self._access_token = token
            self._access_token_expires_at = time.monotonic() + expires_in
            return token
        except httpx.HTTPError as e:
            logger.warning("Reddit OAuth token request failed: %s", e)
            return None

    async def _reddit_get(self, path: str, params: dict) -> Optional[dict]:
        token = await self._get_access_token()
        if not token:
            logger.info("Reddit OAuth is unavailable; using RSS fallback")
            return None

        headers = {
            "Authorization": f"Bearer {token}",
            "User-Agent": self.user_agent,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
        }
        url = f"{REDDIT_OAUTH_BASE}{path}"
        try:
            response = await self.client.get(url, params=params, headers=headers, follow_redirects=True)
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 5))
                logger.warning("Reddit rate limited, retrying after %ds", retry_after)
                await asyncio.sleep(retry_after)
                response = await self.client.get(url, params=params, headers=headers, follow_redirects=True)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.warning("Reddit request failed for %s: %s", url, e)
            return None

    async def _reddit_feed(self, url: str, params: dict) -> Optional[dict]:
        headers = {
            "User-Agent": self.user_agent,
            "Accept": "application/atom+xml, application/rss+xml, text/xml, */*",
            "Accept-Language": "en-US,en;q=0.9",
        }
        try:
            response = await self.client.get(url, params=params, headers=headers, follow_redirects=True)
            response.raise_for_status()
            feed = feedparser.parse(response.text)
            if feed.bozo:
                logger.warning("Reddit RSS parse warning for %s: %s", url, feed.bozo_exception)
            return feed
        except httpx.HTTPError as e:
            logger.warning("Reddit RSS request failed for %s: %s", url, e)
            return None

    def _parse_rss_entry(
        self,
        entry: dict,
        subreddit: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Optional[dict]:
        created = self._parse_rss_date(entry)
        if not created:
            return None

        discussion_url = entry.get("link", "")
        post_id = entry.get("id", discussion_url).replace("t3_", "", 1)
        if not post_id and discussion_url:
            match = re.search(r"/comments/([^/]+)/", discussion_url)
            post_id = match.group(1) if match else discussion_url

        summary_html = entry.get("summary", "")
        external_url = self._extract_rss_link(summary_html, discussion_url)
        author = (entry.get("author") or username or "unknown").strip()
        author = re.sub(r"^/u/", "", author)

        return {
            "id": post_id,
            "title": entry.get("title", "Untitled"),
            "url": external_url or discussion_url,
            "permalink": self._permalink_from_url(discussion_url),
            "author": author,
            "created_utc": created.timestamp(),
            "selftext": self._extract_rss_content(summary_html),
            "is_self": not external_url or external_url == discussion_url,
            "subreddit": subreddit or self._subreddit_from_url(discussion_url),
            "score": None,
            "upvote_ratio": None,
            "num_comments": 0,
            "link_flair_text": None,
        }

    @staticmethod
    def _parse_rss_date(entry: dict) -> Optional[datetime]:
        for field in ("published", "updated", "created"):
            parsed = entry.get(f"{field}_parsed")
            if parsed:
                return datetime.fromtimestamp(calendar.timegm(parsed), tz=timezone.utc)
        return None

    @staticmethod
    def _extract_rss_content(summary_html: str) -> str:
        soup = BeautifulSoup(summary_html, "html.parser")
        content = soup.select_one("div.md")
        if not content:
            return ""
        text = content.get_text("\n", strip=True)
        return text[:1500] + "..." if len(text) > 1500 else text

    @staticmethod
    def _extract_rss_link(summary_html: str, discussion_url: str) -> str:
        soup = BeautifulSoup(summary_html, "html.parser")
        for link in soup.find_all("a"):
            if link.get_text(strip=True) == "[link]":
                href = link.get("href") or ""
                if href and "/comments/" not in href:
                    return href
        return discussion_url

    @staticmethod
    def _permalink_from_url(url: str) -> str:
        match = re.search(r"https?://(?:www\.)?reddit\.com(?P<path>/r/[^/]+/comments/[^?#]+)", url)
        return match.group("path") if match else url

    @staticmethod
    def _subreddit_from_url(url: str) -> str:
        match = re.search(r"/r/([^/]+)/", url)
        return match.group(1) if match else ""
