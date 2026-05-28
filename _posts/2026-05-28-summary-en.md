---
layout: default
title: "Horizon Summary: 2026-05-28 (EN)"
date: 2026-05-28
lang: en
---

> From 4 items, 3 important content pieces were selected

---

1. [Anthropic Releases Claude Opus 4.8, Teases Mythos Model](#item-1) ⭐️ 8.0/10
2. [SQLite Adds AGENTS.md Rejecting AI Agent Contributions](#item-2) ⭐️ 8.0/10
3. [Postgres Alone for Durable Workflows?](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic Releases Claude Opus 4.8, Teases Mythos Model](https://www.anthropic.com/news/claude-opus-4-8) ⭐️ 8.0/10

Anthropic has released Claude Opus 4.8, a modest improvement over its predecessor, and announced Project Glasswing, under which a small number of organizations are using the more powerful Claude Mythos Preview for cybersecurity work. This release continues Anthropic's incremental improvements to its frontier models, while the Mythos Preview signals a significant leap in capability that could reshape AI-assisted cybersecurity, though it requires stronger safeguards before general release. Users can now disable adaptive thinking in the web UI, addressing issues where thinking did not trigger and produced subpar output. The Mythos model is part of Project Glasswing, an initiative to secure critical open source software by proactively identifying and fixing vulnerabilities at scale.

hackernews · craigmart · May 28, 16:49

**Background**: Anthropic's Claude family includes models like Sonnet and Opus, with version numbers like 4.5, 4.6, etc. Project Glasswing is an Anthropic initiative to secure critical software for the AI era by partnering with organizations responsible for infrastructure. The Mythos model is a new frontier model with higher intelligence than Opus, but its release is pending stronger cyber safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://www.bbc.com/news/articles/crk1py1jgzko">What is Anthopic's Claude Mythos and what risks does it pose?</a></li>

</ul>
</details>

**Discussion**: Community comments note this is the first time a frontier Anthropic model has received three minor version bumps (4.6, 4.7, 4.8) with modest gains, and some users appreciate the ability to disable adaptive thinking. Others are excited about the Mythos preview, though concerns about its potential risks are acknowledged.

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#frontier models`, `#cybersecurity`

---

<a id="item-2"></a>
## [SQLite Adds AGENTS.md Rejecting AI Agent Contributions](https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything) ⭐️ 8.0/10

SQLite added an AGENTS.md file outlining its policy on AI agent contributions, explicitly stating it does not accept agentic code but will accept agentic bug reports with reproducible test cases and documentation patches. A recent commit removed the word "currently" to strengthen the statement against accepting agentic code. This is one of the first explicit policies by a major open-source project on AI agent contributions, setting a precedent for how projects can manage the influx of AI-generated code and bug reports. It highlights the growing challenge of maintaining code quality and project governance in the age of autonomous coding agents. The AGENTS.md file was added five days ago, and the most recent commit removed "(currently)" from the phrase "SQLite does not (currently) accept agentic code" to strengthen the stance. Additionally, the SQLite forum was flooded with AI-generated bug reports, leading to the creation of a separate SQLite Bug Forum.

rss · Simon Willison · May 27, 23:44

**Background**: AGENTS.md is a simple, open format for guiding AI coding agents, used by over 60,000 open-source projects as a dedicated place to provide context and instructions. Agentic coding refers to a software development approach where autonomous AI agents plan, write, test, and modify code with minimal human intervention, which can introduce design decisions conflicting with project standards.

<details><summary>References</summary>
<ul>
<li><a href="https://agents.md/">AGENTS.md</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>
<li><a href="https://github.com/agentsmd/agents.md">GitHub - agentsmd/agents.md: AGENTS.md — a simple, open format for guiding coding agents</a></li>

</ul>
</details>

**Discussion**: The community discussion on the Datasette Discord highlighted the move as a notable development, with Alex Garcia sharing the news. The broader sentiment appears supportive of SQLite's proactive stance in managing AI-generated contributions.

**Tags**: `#AI agents`, `#open source governance`, `#SQLite`, `#software engineering`

---

<a id="item-3"></a>
## [Postgres Alone for Durable Workflows?](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 7.0/10

A blog post argues that Postgres alone suffices for durable workflow execution, comparing implementations like DBOS, River, and Absurd. This discussion highlights a trend toward simplifying durable workflow architectures by leveraging Postgres, potentially reducing operational complexity and costs. DBOS relies on a paid component (Conductor) for scaling and recovery, while River lacks built-in dead-letter queue support, which is a paid feature.

hackernews · KraftyOne · May 28, 18:41

**Background**: Durable workflow execution ensures that long-running processes survive crashes and restarts by persisting state. Traditionally, dedicated workflow engines like Temporal are used, but some argue Postgres can serve as both database and orchestration layer.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution">Postgres-backed Durable Workflow Execution | DBOS</a></li>
<li><a href="https://github.com/pgflow-dev/pgflow">GitHub - pgflow-dev/pgflow: Postgres-centric workflow engine with deep integration with Supabase · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters note that DBOS's reliance on a paid component for scaling is a drawback, and River's lack of free DLQ support is a limitation. Others share alternative implementations and compare experiences with Temporal.

**Tags**: `#durable workflows`, `#postgres`, `#distributed systems`, `#software engineering`

---