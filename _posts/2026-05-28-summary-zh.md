---
layout: default
title: "Horizon Summary: 2026-05-28 (ZH)"
date: 2026-05-28
lang: zh
---

> From 4 items, 3 important content pieces were selected

---

1. [Anthropic 发布 Claude Opus 4.8，预告 Mythos 模型](#item-1) ⭐️ 8.0/10
2. [SQLite 添加 AGENTS.md 拒绝 AI 代理贡献](#item-2) ⭐️ 8.0/10
3. [仅用 Postgres 实现持久化工作流？](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Opus 4.8，预告 Mythos 模型](https://www.anthropic.com/news/claude-opus-4-8) ⭐️ 8.0/10

Anthropic 发布了 Claude Opus 4.8，相比前代有适度提升，并宣布了 Project Glasswing 项目，在该项目下，少数组织正在使用更强大的 Claude Mythos Preview 进行网络安全工作。 此次发布延续了 Anthropic 对其前沿模型的渐进式改进，而 Mythos Preview 则预示着能力的重大飞跃，可能重塑 AI 辅助的网络安全领域，但需要更强的安全措施才能全面发布。 用户现在可以在 Web 界面中关闭自适应思考功能，解决了思考未触发导致输出质量不佳的问题。Mythos 模型是 Project Glasswing 的一部分，该计划旨在通过大规模主动识别和修复漏洞来保护关键开源软件。

hackernews · craigmart · May 28, 16:49

**背景**: Anthropic 的 Claude 系列包括 Sonnet 和 Opus 等模型，版本号如 4.5、4.6 等。Project Glasswing 是 Anthropic 的一项计划，通过与负责基础设施的组织合作，为 AI 时代保护关键软件。Mythos 模型是比 Opus 智能更高的新前沿模型，但其发布需要更强的网络安全保障。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://www.bbc.com/news/articles/crk1py1jgzko">What is Anthopic's Claude Mythos and what risks does it pose?</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，这是 Anthropic 前沿模型首次连续三次小版本升级（4.6、4.7、4.8），提升幅度有限，一些用户对能够关闭自适应思考功能表示赞赏。其他人则对 Mythos 预览版感到兴奋，但也承认其潜在风险令人担忧。

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#frontier models`, `#cybersecurity`

---

<a id="item-2"></a>
## [SQLite 添加 AGENTS.md 拒绝 AI 代理贡献](https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything) ⭐️ 8.0/10

SQLite 添加了 AGENTS.md 文件，明确了其对 AI 代理贡献的政策，明确表示不接受代理生成的代码，但接受包含可复现测试用例的代理错误报告和文档补丁。最近一次提交删除了“currently”一词，以强化不接受代理代码的声明。 这是主要开源项目首次明确制定关于 AI 代理贡献的政策，为项目如何管理 AI 生成的代码和错误报告的涌入树立了先例。它凸显了在自主编码代理时代维护代码质量和项目治理的日益严峻挑战。 AGENTS.md 文件于五天前添加，最近一次提交从“SQLite does not (currently) accept agentic code”中删除了“(currently)”，以强化立场。此外，SQLite 论坛被 AI 生成的错误报告淹没，导致创建了单独的 SQLite Bug Forum。

rss · Simon Willison · May 27, 23:44

**背景**: AGENTS.md 是一种简单的开放格式，用于指导 AI 编码代理，已被超过 60,000 个开源项目用作提供上下文和说明的专用位置。代理编码是一种软件开发方法，自主 AI 代理在最少人工干预下规划、编写、测试和修改代码，这可能会引入与项目标准冲突的设计决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agents.md/">AGENTS.md</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>
<li><a href="https://github.com/agentsmd/agents.md">GitHub - agentsmd/agents.md: AGENTS.md — a simple, open format for guiding coding agents</a></li>

</ul>
</details>

**社区讨论**: Datasette Discord 上的社区讨论强调此举是一个值得注意的发展，Alex Garcia 分享了这一消息。总体情绪似乎支持 SQLite 在管理 AI 生成贡献方面的积极立场。

**标签**: `#AI agents`, `#open source governance`, `#SQLite`, `#software engineering`

---

<a id="item-3"></a>
## [仅用 Postgres 实现持久化工作流？](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 7.0/10

一篇博文认为仅使用 Postgres 就足以实现持久化工作流执行，并比较了 DBOS、River 和 Absurd 等实现。 这一讨论凸显了通过利用 Postgres 简化持久化工作流架构的趋势，可能降低运维复杂性和成本。 DBOS 依赖付费组件 Conductor 进行扩展和恢复，而 River 缺乏内置的死信队列支持，该功能需付费。

hackernews · KraftyOne · May 28, 18:41

**背景**: 持久化工作流执行通过持久化状态确保长时间运行的过程在崩溃和重启后仍能继续。传统上使用 Temporal 等专用工作流引擎，但有人认为 Postgres 可以同时作为数据库和编排层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution">Postgres-backed Durable Workflow Execution | DBOS</a></li>
<li><a href="https://github.com/pgflow-dev/pgflow">GitHub - pgflow-dev/pgflow: Postgres-centric workflow engine with deep integration with Supabase · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 DBOS 依赖付费组件进行扩展是一个缺点，而 River 缺乏免费的死信队列支持是限制。其他人分享了替代实现并与 Temporal 的使用体验进行了比较。

**标签**: `#durable workflows`, `#postgres`, `#distributed systems`, `#software engineering`

---