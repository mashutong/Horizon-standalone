---
layout: default
title: "Horizon Summary: 2026-05-29 (EN)"
date: 2026-05-29
lang: en
---

> From 8 items, 7 important content pieces were selected

---

1. [vLLM v0.22.0: DeepSeek V4 Hardening, MRv2, Rust Frontend](#item-1) ⭐️ 8.0/10
2. [The Dead Economy Theory: AI May Destroy Its Own Market](#item-2) ⭐️ 8.0/10
3. [Anthropic's run-rate revenue hits $47 billion](#item-3) ⭐️ 8.0/10
4. [SQLite as a Foundation for Durable Workflows](#item-4) ⭐️ 7.0/10
5. [Mistral AI Pivots to On-Prem and European-Hosted AI](#item-5) ⭐️ 7.0/10
6. [Datasette 1.0a31 Adds Write Queries and Stored Queries](#item-6) ⭐️ 7.0/10
7. [Claude Opus 4.8: A Modest Step Forward](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.22.0: DeepSeek V4 Hardening, MRv2, Rust Frontend](https://github.com/vllm-project/vllm/releases/tag/v0.22.0) ⭐️ 8.0/10

vLLM v0.22.0, released with 459 commits from 230 contributors, includes major hardening for DeepSeek V4, Model Runner V2 (MRv2) advances toward becoming the default, and an experimental Rust frontend. This release significantly improves inference performance and reliability for DeepSeek V4 and other models, with batch-invariant Cutlass FP8 support yielding up to 28.9% latency improvement, and multi-tier KV cache offloading extending memory efficiency beyond CPU. DeepSeek V4 gains NVFP4 fused MoE support, full and piecewise CUDA graphs, MTP speculative decoding, and a dedicated package. MRv2 now automatically selects for Qwen3 dense models and falls back to MRv1 when a KV connector is present.

github · khluu · May 29, 10:28

**Background**: vLLM is a high-throughput, memory-efficient LLM inference engine widely used in production. Model Runner V2 is a redesigned execution path aiming to improve performance and flexibility. DeepSeek V4 is a large language model requiring optimized kernels for efficient inference.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe/">trtllm_ nvfp 4 _ moe - vLLM</a></li>
<li><a href="https://medium.com/practical-llm-systems/i-tested-mtp-speculative-decoding-on-two-qwen-models-one-was-a-trap-46c2dfe584c7">I Tested MTP Speculative Decoding on Two Qwen Models... | Medium</a></li>
<li><a href="https://pyshine.com/DeepGEMM-Efficient-FP8-GEMM-Kernels/">DeepGEMM: Clean and Efficient FP8 GEMM Kernels with... | PyShine</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#open source`, `#AI infrastructure`

---

<a id="item-2"></a>
## [The Dead Economy Theory: AI May Destroy Its Own Market](https://www.owenmcgrann.com/p/the-dead-economy-theory) ⭐️ 8.0/10

Owen McGrann's article 'The Dead Economy Theory' proposes that AI-driven efficiency gains could eliminate human customers, leading to a paradoxical economic collapse where companies destroy their own markets by replacing workers with AI. This theory challenges the prevailing optimistic narrative around AI and automation, highlighting a systemic risk that could reshape economic policy and labor markets globally. The article describes a three-turn scenario: companies fire workers to save costs, those workers lose income and stop buying, and revenue stalls as customers disappear, potentially leading to a fully non-human AI economy.

hackernews · WillDaSilva · May 29, 15:46

**Background**: The 'dead economy' theory builds on historical patterns of labor displacement and economic restructuring, but argues that AI's ability to replace cognitive work at scale creates a unique risk of eliminating the consumer base itself. It contrasts with earlier automation fears by focusing on demand-side collapse rather than just job loss.

**Discussion**: Commenters largely engaged with the theory's implications, with some drawing parallels to India's agricultural inefficiency subsidies and others noting that overcapacity in tech (e.g., Facebook's Messenger team) may already signal a pre-dead economy. A few questioned the extreme conclusion but praised the systemic analysis.

**Tags**: `#economics`, `#AI`, `#automation`, `#labor`, `#technology`

---

<a id="item-3"></a>
## [Anthropic's run-rate revenue hits $47 billion](https://simonwillison.net/2026/May/29/anthropic/#atom-everything) ⭐️ 8.0/10

Anthropic announced that its run-rate revenue crossed $47 billion in May 2026, up from $9 billion at the end of 2025 and $30 billion in April 2026, as disclosed in its $65 billion Series H funding announcement. This explosive growth signals rapid enterprise adoption of AI, positioning Anthropic as one of the fastest-scaling companies in history and validating the market for large language models. Run-rate revenue is an annualized projection based on the most recent month's revenue multiplied by 12. The $47 billion figure was included in Anthropic's Series H announcement, and the company has consistently shared such metrics in prior funding rounds.

rss · Simon Willison · May 29, 01:23

**Background**: Run-rate revenue extrapolates a company's current financial performance to estimate annual revenue, assuming no changes. It is commonly used by fast-growing startups to indicate momentum, though it can overstate sustainable revenue if growth is not linear. Anthropic is a leading AI company focused on developing safe and capable large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/series-h">Anthropic raises $65B in Series H funding at $965B post- ...</a></li>
<li><a href="https://corporatefinanceinstitute.com/resources/accounting/revenue-run-rate/">Revenue Run Rate - Definition, Calculation, Examples</a></li>
<li><a href="https://www.investopedia.com/terms/r/runrate.asp">Run Rate Explained: Benefits, Risks, and Business Insights</a></li>

</ul>
</details>

**Discussion**: Some skeptics, like Ed Zitron, previously questioned the $30 billion figure, but the author argues that lying to investors in a $65 billion fundraising would constitute securities fraud, lending credibility to the numbers. Others dismiss the figures as untrustworthy because they come from Anthropic, but the author counters that the real numbers will emerge in the S-1 filing for the IPO.

**Tags**: `#Anthropic`, `#AI industry`, `#revenue`, `#funding`, `#enterprise AI`

---

<a id="item-4"></a>
## [SQLite as a Foundation for Durable Workflows](https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/) ⭐️ 7.0/10

A blog post argues that SQLite can serve as a sufficient foundation for building durable workflow systems, challenging the need for more complex solutions like Temporal or Postgres. This sparks debate on whether lightweight embedded databases can replace dedicated workflow orchestrators, potentially simplifying infrastructure for many applications. The article suggests using SQLite's WAL mode and row-level locking to handle concurrency, but critics point out SQLite's poor type system and lack of built-in concurrency control for multi-process access.

hackernews · tomasol · May 29, 17:54

**Background**: Durable workflows ensure that long-running processes survive failures and can be resumed. Traditional approaches use dedicated workflow engines like Temporal or databases like Postgres for state management. SQLite is an embedded SQL database typically used for local storage, not concurrent multi-user scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://www.inngest.com/uses/durable-workflows">Inngest - Durable Workflows</a></li>
<li><a href="https://www.restate.dev/what-is-durable-execution">What is Durable Execution? A Definitive Guide | Restate</a></li>
<li><a href="https://docs.temporal.io/workflows">Temporal Workflow | Temporal Platform Documentation</a></li>

</ul>
</details>

**Discussion**: Comments are mixed: some praise SQLite's simplicity for local or single-process workflows, while others argue it is unsuitable for production due to concurrency limitations and poor type enforcement. Temporal is mentioned as a more robust alternative that also uses SQLite internally for local setups.

**Tags**: `#SQLite`, `#workflows`, `#durability`, `#database`, `#software engineering`

---

<a id="item-5"></a>
## [Mistral AI Pivots to On-Prem and European-Hosted AI](https://koenvangilst.nl/lab/mistral-ai-now-summit) ⭐️ 7.0/10

At the Mistral AI Now Summit, the company announced a strategic pivot toward on-premises and European-hosted AI solutions for regulated industries, with case studies from BNP Paribas and Abanca. This move positions Mistral as a key alternative to US hyperscalers for European companies in regulated sectors, potentially reshaping the AI adoption landscape in finance and other sensitive industries. Mistral's on-prem solution allows banks like BNP Paribas to run models for KYC while keeping sensitive data within their own infrastructure, and Abanca uses agent orchestration for 2 million customers.

hackernews · vnglst · May 29, 16:22

**Background**: Mistral AI is a Paris-based startup founded in 2023 by former Google DeepMind and Meta engineers, known for open-weight large language models. On-premises AI refers to deploying models on a company's own servers rather than in the cloud, which is critical for data privacy compliance in regulated industries.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mistral_AI">Mistral AI - Wikipedia</a></li>
<li><a href="https://mistral.ai/">Frontier AI LLMs, assistants, agents, services | Mistral AI</a></li>
<li><a href="https://mistral.ai/news/mistral-small-3-1/">Mistral Small 3.1 | Mistral AI</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some praise Mistral's on-prem focus as smart for European regulated industries, while others criticize the company for falling behind in reasoning models and small model performance compared to Chinese labs like DeepSeek and Qwen.

**Tags**: `#Mistral AI`, `#AI regulation`, `#on-prem AI`, `#European tech`, `#small models`

---

<a id="item-6"></a>
## [Datasette 1.0a31 Adds Write Queries and Stored Queries](https://simonwillison.net/2026/May/29/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a31 introduces the ability for authorized users to execute write queries (INSERT, UPDATE, DELETE) against databases and to save stored queries (renamed from 'canned queries') for private or shared use. This release transforms Datasette from a read-only exploration tool into a full interactive database management platform, enabling users to edit data directly through the web UI and share reusable queries, which significantly expands its utility for collaborative data projects. Write query execution is permission-controlled, requiring the 'execute-sql' permission, and users can only run statements on tables they have permission to edit; stored queries support templated parameters and can be saved privately or publicly.

rss · Simon Willison · May 29, 03:32

**Background**: Datasette is an open-source tool for exploring and publishing relational databases, primarily SQLite, via a web interface. Previously, it only allowed read-only SQL queries. The new write and stored query features build on functionality that was previously available only through plugins like datasette-write.

<details><summary>References</summary>
<ul>
<li><a href="https://datasette.io/blog/2026/sql-write-queries/">SQL write queries and stored queries in Datasette ... - Datasette Blog</a></li>
<li><a href="https://simonwillison.net/2026/May/29/datasette/">Release: datasette 1.0a31 | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#open-source`, `#database`, `#SQL`, `#release`

---

<a id="item-7"></a>
## [Claude Opus 4.8: A Modest Step Forward](https://simonwillison.net/2026/May/28/claude-opus-4-8/#atom-everything) ⭐️ 7.0/10

Anthropic released Claude Opus 4.8 on May 28, 2026, describing it as a modest but tangible improvement over its predecessor, with a focus on model honesty and reduced hallucination. This release is significant for its transparent communication about incremental progress, a rare practice in the AI industry, and for advancing model honesty—a critical aspect of AI safety and trustworthiness. Opus 4.8 is priced identically to Opus 4.5/4.6/4.7 at $5/million input tokens and $25/million output tokens, with a 1,000,000-token context window and 128,000-token max output. It also introduces mid-conversation system messages, allowing dynamic instruction updates without full prompt restatement.

rss · Simon Willison · May 28, 23:59

**Background**: Claude Opus is Anthropic's flagship large language model series, known for strong reasoning and coding capabilities. The 4.8 release comes just six weeks after Opus 4.7, marking the fastest cadence between Opus releases. Anthropic has been emphasizing model honesty as a key safety feature, training models to avoid unsupported claims and flag uncertainties.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/opus">Claude Opus 4 . 8 \ Anthropic</a></li>
<li><a href="https://overchat.ai/models/claude/claude-opus-4-8">Claude Opus 4 . 8</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#model release`, `#honesty`

---