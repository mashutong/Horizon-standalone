---
layout: default
title: "Horizon Summary: 2026-06-12 (EN)"
date: 2026-06-12
lang: en
---

{% raw %}
> From 30 items, 15 important content pieces were selected

---

1. [AMD's RCE Vulnerability Patched with Insecure CRC-32](#item-1) ⭐️ 9.0/10
2. [Google Releases DiffusionGemma, Open-Weight Diffusion LM](#item-2) ⭐️ 9.0/10
3. [Homebrew 6.0.0 Released with Tap Trust and Linux Sandboxing](#item-3) ⭐️ 8.0/10
4. [Xiaomi Open-Sources MiMo Code AI Coding Assistant](#item-4) ⭐️ 8.0/10
5. [Petition to Withdraw Canada's Bill C-22](#item-5) ⭐️ 8.0/10
6. [Anthropic Apologizes for Invisible Claude Fable Guardrails](#item-6) ⭐️ 8.0/10
7. [Jeremy Howard proposes AI safety rule: top lab can't use its own model](#item-7) ⭐️ 8.0/10
8. [Simon Willison's First Impressions of Claude Fable 5](#item-8) ⭐️ 8.0/10
9. [Datasette 1.0a33 Extends JSON Extras to Queries and Rows](#item-9) ⭐️ 7.0/10
10. [Is Symbolic Regression Still Relevant in the Age of LLMs?](#item-10) ⭐️ 7.0/10
11. [Papers Without Code relaunched with closed-source model support](#item-11) ⭐️ 7.0/10
12. [Routing LLMs by Task Verifiability: Small Experiment](#item-12) ⭐️ 7.0/10
13. [Parameter-Free Adaptive Video Tokenization via Temporal Redundancy](#item-13) ⭐️ 7.0/10
14. [Pyrecall: Open-source tool to detect catastrophic forgetting in LLM fine-tuning](#item-14) ⭐️ 7.0/10
15. [Apple Releases Swift-Based Linux Container Tool for Mac](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AMD's RCE Vulnerability Patched with Insecure CRC-32](https://mrbruh.com/amd2/) ⭐️ 9.0/10

A researcher discovered a remote code execution (RCE) vulnerability in AMD's AutoUpdate software, and AMD's patch replaced signature verification with a non-cryptographic CRC-32 check, leaving the system vulnerable to server compromise. This highlights AMD's inadequate software security practices, as CRC-32 is designed for error detection, not cryptographic integrity, and can be easily bypassed by an attacker who compromises the update server. The vulnerability exists in AMD's AutoUpdate executable, which downloads updates over HTTPS but only performs a CRC-32 check on the downloaded file, not cryptographic signature verification. This means a compromised server can serve malicious updates without detection.

hackernews · MrBruh · Jun 11, 16:03 · [Discussion](https://news.ycombinator.com/item?id=48492215)

**Background**: Remote code execution (RCE) vulnerabilities allow attackers to run arbitrary code on a target system. CRC-32 is a cyclic redundancy check used for detecting accidental data corruption, but it is not cryptographically secure and can be trivially forged by an attacker. Proper patch verification should use cryptographic hashes like SHA-256 or digital signatures.

<details><summary>References</summary>
<ul>
<li><a href="https://mrbruh.com/amd2/">The RCE that AMD wouldn’t fix! | MrBruh's Epic Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cyclic_redundancy_check">Cyclic redundancy check - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Arbitrary_code_execution">Arbitrary code execution - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed disbelief at AMD's use of CRC-32 for security, calling it 'hilariously clueless.' Some noted that MITM attacks should be considered in scope, and that DNS cache poisoning could enable exploitation without full MITM. Others criticized AMD's long history of poor software quality.

**Tags**: `#security`, `#vulnerability`, `#AMD`, `#RCE`, `#supply chain`

---

<a id="item-2"></a>
## [Google Releases DiffusionGemma, Open-Weight Diffusion LM](https://simonwillison.net/2026/Jun/10/diffusiongemma/#atom-everything) ⭐️ 9.0/10

Google has released DiffusionGemma, an open-weight (Apache 2 licensed) diffusion-based language model, available on Hugging Face as google/diffusiongemma-26B-A4B-it. NVIDIA is hosting the model for free on its NIM cloud API, achieving over 500 tokens per second in testing. This release marks a major step in making diffusion-based language models accessible and practical, offering significantly faster text generation than traditional autoregressive models. The open-weight license and free hosting lower barriers for researchers and developers to experiment with this new paradigm. The model has 26 billion total parameters with 4 billion active parameters (MoE architecture) and can run in just 18GB VRAM. It was built on Gemma 4 and Gemini Diffusion research, and integrated with vLLM for efficient serving.

rss · Simon Willison · Jun 10, 20:00

**Background**: Traditional large language models generate text autoregressively, predicting one token at a time in sequence. Diffusion language models instead start from noise and iteratively refine it to produce text in parallel, enabling much faster generation. Google previously released an experimental Gemini Diffusion model in May 2025, which laid the groundwork for DiffusionGemma.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.googleblog.com/diffusiongemma-the-developer-guide/">DiffusionGemma: The Developer Guide - Google Developers Blog</a></li>
<li><a href="https://deepmind.google/models/gemma/diffusiongemma/">DiffusionGemma — Google DeepMind</a></li>
<li><a href="https://www.aimadetools.com/blog/diffusiongemma-complete-guide/">DiffusionGemma Complete Guide: Google's 4x Faster Text ...</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion highlights excitement about the speed and open licensing, with some users noting the potential for real-time applications. A few commenters raised questions about the model's quality compared to autoregressive models of similar size.

**Tags**: `#AI`, `#open-source`, `#language model`, `#diffusion`, `#Google`

---

<a id="item-3"></a>
## [Homebrew 6.0.0 Released with Tap Trust and Linux Sandboxing](https://brew.sh/2026/06/11/homebrew-6.0.0/) ⭐️ 8.0/10

Homebrew 6.0.0 introduces a mandatory tap trust security mechanism, a faster and smaller internal JSON API, Linux sandboxing via Bubblewrap, and initial support for macOS 27 (Golden Gate). This major release enhances security and performance for millions of macOS and Linux users, addressing supply chain risks and improving the developer experience with faster API responses and better Linux compatibility. The tap trust mechanism requires explicit user approval for third-party taps before their Ruby code can execute, reducing the risk of malicious packages. Linux sandboxing uses Bubblewrap to isolate build processes, and the new JSON API is now the default for faster formula queries.

hackernews · mikemcquaid · Jun 11, 13:24 · [Discussion](https://news.ycombinator.com/item?id=48490024)

**Background**: Homebrew is a popular open-source package manager for macOS and Linux, allowing users to install software from the command line. Taps are third-party repositories that extend Homebrew's package collection. Prior to 6.0.0, all taps were trusted by default, posing a security risk if a tap was compromised.

<details><summary>References</summary>
<ul>
<li><a href="https://brew.sh/2026/06/11/homebrew-6.0.0/">Homebrew: 6.0.0</a></li>
<li><a href="https://docs.brew.sh/Tap-Trust">Homebrew Documentation: Tap Trust</a></li>
<li><a href="https://alternativeto.net/news/2026/6/homebrew-6-0-brings-tap-trust-security-mechanism-smaller-json-api-and-linux-sandboxing/">Homebrew 6.0 brings tap trust security mechanism, smaller ...</a></li>

</ul>
</details>

**Discussion**: The community reaction is largely positive, with users praising the longevity of the project and the new security features. Some users discuss alternatives like Nix and mise, noting trade-offs in reproducibility and ease of use, while others highlight Homebrew's role on immutable Linux distributions.

**Tags**: `#Homebrew`, `#package manager`, `#macOS`, `#Linux`, `#security`

---

<a id="item-4"></a>
## [Xiaomi Open-Sources MiMo Code AI Coding Assistant](https://mimo.xiaomi.com/mimocode) ⭐️ 8.0/10

Xiaomi has released MiMo Code V0.1.0 as an open-source, terminal-native AI coding assistant. It is a fork of OpenCode and adds persistent memory, subagent orchestration, and goal-driven autonomous loops. This move challenges closed-source tools like Claude Code and the deprecated Gemini CLI, promoting an open ecosystem where LLMs are treated as commodities. It lowers switching costs for developers and fosters transparency in AI-assisted coding. MiMo Code supports multiple LLM providers, a terminal UI, LSP, MCP, and plugins. Its persistent memory system maintains project context across sessions, and the autonomous loops enable self-improvement through dream/distill cycles.

hackernews · apeters · Jun 11, 14:27 · [Discussion](https://news.ycombinator.com/item?id=48490826)

**Background**: AI coding assistants help developers write, debug, and manage code using large language models. Most existing tools are stateless, losing context between sessions; persistent memory addresses this by retaining project understanding over time. Open-source alternatives like OpenCode provide a foundation for community-driven innovation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/XiaomiMiMo/MiMo-Code">GitHub - XiaomiMiMo/MiMo-Code</a></li>
<li><a href="https://mimo.xiaomi.com/coder">MiMo Code</a></li>
<li><a href="https://www.gizmochina.com/2026/06/11/xiaomi-mimo-code-open-source-terminal-ai-coding-agent/">Xiaomi announces new AI coding agent that actually remembers ...</a></li>

</ul>
</details>

**Discussion**: The community largely welcomes the open-source release, with users praising features like persistent memory and subagent orchestration. Some contrast it favorably against closed-source tools, while others note Xiaomi's growing AI capabilities and competitive pricing.

**Tags**: `#AI coding assistant`, `#open source`, `#Xiaomi`, `#developer tools`, `#LLM`

---

<a id="item-5"></a>
## [Petition to Withdraw Canada's Bill C-22](https://www.ourcommons.ca/petitions/en/Petition/Sign/e-7416) ⭐️ 8.0/10

A petition has been launched on the Canadian House of Commons website calling for the withdrawal of Bill C-22, a lawful access bill that critics argue threatens privacy and harms the tech sector. The bill is currently undergoing clause-by-clause review by the SECU committee. If passed, Bill C-22 could mandate metadata retention for up to one year and grant the Public Safety Minister secret powers to compel design changes, raising significant privacy and constitutional concerns. The outcome may impact Canada's tech sector and citizens' digital rights. The bill requires telecoms and digital platforms to retain metadata for up to one year and could allow the minister to issue orders to retrieve data or trace devices. Major U.S. tech companies and congressional committees have voiced opposition.

hackernews · hmokiguess · Jun 11, 15:37 · [Discussion](https://news.ycombinator.com/item?id=48491830)

**Background**: Bill C-22 is a lawful access bill introduced by the Canadian government to update investigative powers for the digital age. It follows the earlier Bill C-2 and has been criticized for expanding surveillance capabilities without adequate safeguards. Privacy advocates argue it risks creating a surveillance state.

<details><summary>References</summary>
<ul>
<li><a href="https://www.michaelgeist.ca/2026/03/the-lawful-access-privacy-risks-unpacking-bill-c-22s-expansive-metadata-retention-requirements/">The Lawful Access Privacy Risks: Unpacking Bill C-22's ...</a></li>
<li><a href="https://theccf.ca/bill-c-22-explainer/">Explainer: Bill C-22 increases risk of surveillance state ...</a></li>
<li><a href="https://refdesk.ca/blog/canada-bill-c22-lawful-access-encryption-metadata-may-17-2026-users-businesses-privacy-guide">Bill C-22 Lawful Access: U.S. Tech Giants and Congress Push ...</a></li>

</ul>
</details>

**Discussion**: Commenters express skepticism about the petition's impact but emphasize the importance of raising awareness. Some note ongoing SECU committee meetings and the potential for the bill to harm Canada's consumer-facing tech sector, while others express frustration with the political process.

**Tags**: `#privacy`, `#Canada`, `#legislation`, `#tech policy`, `#Bill C-22`

---

<a id="item-6"></a>
## [Anthropic Apologizes for Invisible Claude Fable Guardrails](https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail) ⭐️ 8.0/10

Anthropic apologized for secretly adding invisible guardrails to Claude Fable 5 that throttled users suspected of model distillation, and announced it will make the safeguard visible. This incident erodes user trust in Anthropic's transparency and raises concerns about paternalistic AI deployment, potentially affecting adoption of Claude models in research and development. The invisible guardrail was an anti-distillation measure hidden in a 319-page system card, and it was discovered after a researcher jailbroke Claude Fable 5 within 48 hours of launch.

hackernews · rarisma · Jun 11, 12:05 · [Discussion](https://news.ycombinator.com/item?id=48489229)

**Background**: Model distillation is a technique where a smaller model is trained to mimic a larger one, often used to create cheaper alternatives. Anthropic's guardrail aimed to prevent competitors from distilling Claude Fable 5, but its invisibility sparked backlash over lack of transparency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail">Anthropic apologizes for invisible Claude Fable guardrails - The Verge</a></li>
<li><a href="https://cointelegraph.com/news/researcher-claims-hes-already-jailbroken-anthropics-guardrailed-claude-fable-5">Researcher Jailbreaks Claude Fable 5 Within 48 Hours of Launch</a></li>
<li><a href="https://winbuzzer.com/2026/06/11/anthropic-makes-claude-fable-guardrails-visible-after-apolog-xcxwbn/">Anthropic Makes Claude Fable Guardrails Visible After Apology</a></li>

</ul>
</details>

**Discussion**: Commenters expressed disappointment and distrust, with many noting that the invisible guardrail undermines Anthropic's claims of empowering users. Some argued that the company's paternalistic approach, reminiscent of effective altruism, sets a dangerous precedent for AI transparency.

**Tags**: `#AI ethics`, `#Anthropic`, `#guardrails`, `#transparency`, `#trust`

---

<a id="item-7"></a>
## [Jeremy Howard proposes AI safety rule: top lab can't use its own model](https://simonwillison.net/2026/Jun/10/jeremy-howard/#atom-everything) ⭐️ 8.0/10

Jeremy Howard proposed a counterintuitive AI safety rule: the lab with the top-ranked model must not use it for frontier AI research, while all other labs should have access to it. He argues this would slow recursive self-improvement and prevent dangerous power imbalances. This proposal directly challenges current AI governance approaches, especially Anthropic's strategy of using its top model for frontier research while restricting others. If adopted, it could reshape power dynamics and slow the race toward superintelligence. Howard clarifies that he personally favors democratizing AI rather than slowing it down, but argues that those who claim to want slowdown should ensure their own organization cannot use the best model. He specifically criticizes Anthropic for doing the opposite.

rss · Simon Willison · Jun 10, 15:23

**Background**: Recursive self-improvement (RSI) is a process where an AI system enhances its own capabilities without human intervention, potentially leading to an intelligence explosion. Frontier AI research refers to work on the most advanced AI systems. Howard's proposal aims to break the feedback loop where the best model is used to create an even better one.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#AI governance`, `#recursive self-improvement`, `#Anthropic`

---

<a id="item-8"></a>
## [Simon Willison's First Impressions of Claude Fable 5](https://simonwillison.net/2026/Jun/9/claude-fable-5/#atom-everything) ⭐️ 8.0/10

Simon Willison published his initial hands-on impressions of Anthropic's Claude Fable 5, noting it feels like a 'beast' with high performance and strict guardrails that frequently trigger refusals. He found the model slow, expensive, and challenging to find tasks it cannot handle. This first-hand analysis from a respected developer provides early insight into Claude Fable 5's real-world capabilities and limitations, helping the AI community understand the trade-offs between safety and performance. The model's strict guardrails and fallback mechanisms represent a significant shift in how frontier models handle sensitive topics. Claude Fable 5 has a 1 million token context window, 128,000 maximum output tokens, and a knowledge cutoff of January 2026. It is priced at $10 per million input tokens and $50 per million output tokens, double the price of Claude Opus 4.8.

rss · Simon Willison · Jun 9, 23:59

**Background**: Anthropic released two new models: Claude Fable 5 with safety guardrails and Claude Mythos 5 without them, both offering the same core capabilities. The guardrails in Fable 5 are designed to block harmful requests related to cybersecurity, biology, and chemistry, and the API includes new mechanisms for handling refusals, including automatic fallback to another model.

<details><summary>References</summary>
<ul>
<li><a href="https://indianexpress.com/article/technology/artificial-intelligence/anthropic-claude-fable-5-guardrail-mythos-level-ai-models-10732350/">Anthropic releases Claude Fable 5 with guardrails, bringing Mythos-level AI to users for first time | Technology News - The Indian Express</a></li>
<li><a href="https://www.zdnet.com/article/anthropiclaude-fable-5-nerfed-mythos-with-guardrails/">Anthropic's new Claude Fable 5 is the same base model as Mythos but with guardrails attached | ZDNET</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback">Refusals and fallback - Claude API Docs</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude`, `#Anthropic`, `#LLM`, `#model release`

---

<a id="item-9"></a>
## [Datasette 1.0a33 Extends JSON Extras to Queries and Rows](https://simonwillison.net/2026/Jun/11/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a33 extends the `?_extra=` pattern, previously available only for tables, to row and query JSON API endpoints, allowing users to request additional data fields in responses. The feature is now documented in the official JSON API documentation. This release is a significant step toward Datasette 1.0 stable, providing a consistent and flexible mechanism for customizing JSON responses across all data types. It enhances the API's utility for developers building data-driven applications and tools. The `?_extra=` mechanism was first introduced in Datasette 1.0a3 for tables; 1.0a33 extends it to rows and queries. The release also includes a custom extras API explorer built with AI assistance from Claude and GPT models to demonstrate the feature.

rss · Simon Willison · Jun 11, 15:26

**Background**: Datasette is an open-source tool for exploring and publishing data, providing a JSON API over SQLite databases. The `?_extra=` parameter allows clients to request optional metadata (e.g., column types, row counts) alongside the core data, reducing the need for multiple API calls.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/11/datasette/">Release: datasette 1.0a33 - simonwillison.net</a></li>
<li><a href="http://datasette.io/blog/2026/api-extras/">Datasette 1.0a33 with JSON extras in the API - Datasette Blog</a></li>
<li><a href="https://digg.com/tech/mujp18gf">Datasette 1.0a33 Documents Expanded ?_extra= JSON API for Rows ... - Digg</a></li>

</ul>
</details>

**Discussion**: Community sentiment is positive, with users praising the extended `?_extra=` pattern for making Datasette more flexible. Some noted interest in the AI-assisted development of the extras explorer, highlighting the growing role of AI in open-source tooling.

**Tags**: `#datasette`, `#release`, `#API`, `#open-source`, `#JSON`

---

<a id="item-10"></a>
## [Is Symbolic Regression Still Relevant in the Age of LLMs?](https://www.reddit.com/r/MachineLearning/comments/1u2yqnu/is_symbolic_regression_still_a_thing_given_llms/) ⭐️ 7.0/10

A Reddit discussion questions whether symbolic regression (SR) remains relevant given the rise of large language models (LLMs) that can generate code and tackle symbolic tasks directly. This debate highlights a potential paradigm shift in how symbolic discovery is approached, as LLMs may offer more flexible and sample-efficient alternatives to traditional SR methods. Recent work like LLM-SR (ICLR 2025 Oral) and Deliberate Evolution (2026) show LLMs can be integrated into SR, but traditional SR techniques like genetic programming remain widely used for their interpretability and lack of reliance on large pre-trained models.

reddit · r/MachineLearning · /u/omomom42 · Jun 11, 13:13

**Background**: Symbolic regression is a machine learning technique that searches for mathematical expressions to fit data, often using genetic programming. Unlike neural networks, it produces interpretable equations. LLMs have recently been applied to symbolic regression tasks, raising questions about the future of traditional methods.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Symbolic_regression">Symbolic regression - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2107.14351">[2107.14351] Contemporary Symbolic Regression Methods and ... Chapter 11 Symbolic Regression - Springer Symbolic Regression: The Forgotten Machine Learning Method Recent Advances in Symbolic Regression | ACM Computing Surveys A review on symbolic regression in power systems: Methods ... Introduction to Equation Discovery - Comparing Symbolic ...</a></li>
<li><a href="https://arxiv.org/abs/2606.04360">[2606.04360] Deliberate Evolution: Agentic Reasoning for ...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion includes diverse viewpoints: some argue that LLMs are complementary to SR, while others believe LLMs may eventually replace traditional SR for many tasks. A key concern is that LLMs require large computational resources and may not generalize well to out-of-distribution data.

**Tags**: `#symbolic regression`, `#LLMs`, `#machine learning`, `#code generation`

---

<a id="item-11"></a>
## [Papers Without Code relaunched with closed-source model support](https://www.reddit.com/r/MachineLearning/comments/1u1wq0a/introducing_papers_without_code_p/) ⭐️ 7.0/10

Niels from Hugging Face relaunched paperswithcode.co as a platform that automatically parses research papers to create leaderboards for AI benchmarks, now including support for closed-source models like GPT-5.5 and Mythos 5. This fills a gap in tracking state-of-the-art AI performance, as many benchmarks are now dominated by closed-source models, and provides a toggle to view only open models, helping the community compare both ecosystems. The platform parses papers from arXiv and Hugging Face, and allows submitting any source (e.g., blog posts) for closed-source models, which are tagged as 'closed' in evaluations. Users can disable closed-source evals via a toggle.

reddit · r/MachineLearning · /u/NielsRogge · Jun 10, 08:58

**Background**: Papers With Code was a popular website that linked research papers to code implementations and benchmark results, but it was acquired and later shut down. The new 'Papers Without Code' aims to revive the concept with a focus on automatically generated leaderboards and inclusion of closed-source models, which lack public code.

<details><summary>References</summary>
<ul>
<li><a href="https://www.paperswithoutcode.com/">Papers without code - where unreproducible papers come to live</a></li>
<li><a href="https://openai.com/index/browsecomp/">BrowseComp: a benchmark for browsing agents - OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(model)">Mythos (model)</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is active and insightful, with users debating the utility of including closed-source models and potential biases in leaderboards. Some appreciate the transparency, while others question the reliability of automatically parsed results.

**Tags**: `#machine learning`, `#benchmarks`, `#open source`, `#AI`, `#leaderboards`

---

<a id="item-12"></a>
## [Routing LLMs by Task Verifiability: Small Experiment](https://www.reddit.com/r/MachineLearning/comments/1u2c04u/routing_llms_by_task_verifiability_a_small/) ⭐️ 7.0/10

A Reddit user conducted a small experiment (n=120) testing whether routing LLMs by task verifiability, as proposed by Karpathy, can reduce costs without sacrificing quality, finding mixed results across code, extraction, reasoning, and summarization tasks. This experiment provides early evidence that weaker models with verifiers can match frontier models on high-verifiability tasks, potentially enabling significant cost savings in production LLM systems. The experiment used Claude Sonnet 4.6, GPT 5.5, and local Mistral 3 8B across four task categories; Mistral 3 8B with one retry achieved 95% pass rate on code unit tests, close to Sonnet's 94% and GPT's 91%.

reddit · r/MachineLearning · /u/DragonfruitAlone4497 · Jun 10, 19:18

**Background**: Karpathy's verifiability framework classifies tasks by how easily outputs can be mechanically checked; high-verifiability tasks (e.g., code compilation) are safer for weaker models because errors can be caught by a verifier. LLM routing dynamically selects the most cost-effective model for each query based on task characteristics.

<details><summary>References</summary>
<ul>
<li><a href="https://karpathy.bearblog.dev/verifiability/">Verifiability | karpathy</a></li>
<li><a href="https://github.com/ulab-uiuc/LLMRouter">GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source ...</a></li>
<li><a href="https://www.mindstudio.ai/blog/karpathy-verifiability-framework-decide-what-to-automate-workflow">How to Use Karpathy's Verifiability Framework to Decide What ...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes insights on methodology limitations (small n, single evaluator) and suggestions for improvement, such as using constrained decoding or larger sample sizes.

**Tags**: `#LLM`, `#routing`, `#verifiability`, `#experiment`, `#cost optimization`

---

<a id="item-13"></a>
## [Parameter-Free Adaptive Video Tokenization via Temporal Redundancy](https://www.reddit.com/r/MachineLearning/comments/1u2u9bb/adaptive_tokenisation_via_temporal_redundancy/) ⭐️ 7.0/10

A new paper proposes a parameter-free adaptive token allocation method for video tokenization that exploits temporal redundancy in latent space, eliminating the need for iterative searches or full-rate decoders. The method uses a fixed threshold on temporal L1 differences to drop redundant latent positions and reconstructs them with a lightweight Latent Inpainting Transformer (LIT). This approach significantly reduces computational overhead in video tokenization, achieving a 31x speedup over ElasticTok-CV and 2x over InfoTok, while maintaining competitive reconstruction fidelity. It could enable more efficient video compression and processing for applications like streaming, autonomous driving, and video understanding. The method requires only a single encoder pass and one LIT forward pass, with no auxiliary routing networks. It was evaluated on TokenBench and DAVIS benchmarks, showing content-driven token allocation that aggressively compresses static scenes while retaining more tokens for dynamic sequences.

reddit · r/MachineLearning · /u/chhaya_35 · Jun 11, 09:32

**Background**: Video tokenization converts video frames into discrete tokens for efficient processing by models like transformers. Adaptive tokenization aims to allocate tokens based on visual complexity, but previous methods required iterative searches or full-rate decoders, adding computational cost. Temporal redundancy refers to the similarity between consecutive frames, which can be exploited to reduce token count without losing important information.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.06158">Adaptive Tokenisation Via Temporal Redundancy Masking And ...</a></li>
<li><a href="https://www.semanticscholar.org/paper/Adaptive-Tokenisation-Via-Temporal-Redundancy-And-Dave-Patkuri/7048f10d2a4e7e2d7b180a46391da15187a0e4b8/figure/2">Adaptive Tokenisation Via Temporal Redundancy Masking And ...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is generally positive, with commenters praising the parameter-free design and significant speedups. Some users raised questions about the threshold selection and potential failure cases in highly dynamic scenes, but the authors responded with clarifications.

**Tags**: `#video tokenization`, `#temporal redundancy`, `#latent inpainting`, `#compression`, `#machine learning`

---

<a id="item-14"></a>
## [Pyrecall: Open-source tool to detect catastrophic forgetting in LLM fine-tuning](https://www.reddit.com/r/MachineLearning/comments/1u2hjye/pyrecall_open_source_tool_for_detecting/) ⭐️ 7.0/10

Pyrecall is a new open-source tool (v0.1.0, MIT license) that detects catastrophic forgetting during LLM fine-tuning by snapshotting skill scores before and after training and rolling back problematic LoRA adapters by name. This tool addresses a practical gap in LLM fine-tuning tooling, as catastrophic forgetting is a known challenge but few easy-to-use, local solutions exist. It enables practitioners to safely experiment with fine-tuning without permanently degrading model capabilities. Pyrecall runs fully locally with no external API dependencies, and it allows rolling back specific LoRA adapters that cause regressions. The author is uncertain about the benchmark design and invites community feedback.

reddit · r/MachineLearning · /u/Level_Frosting_7950 · Jun 10, 22:49

**Background**: Catastrophic forgetting occurs when a model loses previously learned knowledge upon learning new information. LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that trains small adapter modules while keeping the base model frozen. Continual learning benchmarks help evaluate how well models retain knowledge across sequential tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.01241">[2504.01241] Catastrophic Forgetting in LLMs: A Comparative ... Avoiding Amnesia: Some Practical Guides to Mitigate ... - Medium Mitigating Catastrophic Forgetting in Large Language Models ... An Empirical Study of Catastrophic Forgetting in Large ... Catastrophic Forgetting in LLMs: A Comparative Analysis ... Catastrophic forgetting in Large Language Models - UnfoldAI Researchers propose a self-distillation fix for ‘catastrophic ...</a></li>
<li><a href="https://towardsdatascience.com/dive-into-lora-adapters-38f4da488ede/">Dive Into LoRA Adapters - Towards Data Science</a></li>
<li><a href="https://continual-learning-bench.com/">Continual Learning Bench</a></li>

</ul>
</details>

**Discussion**: The Reddit post has a score of 7.0, indicating positive reception. The author explicitly asks for feedback on the benchmark design, suggesting an open and collaborative attitude. No other comments are provided in the snippet.

**Tags**: `#LLM`, `#fine-tuning`, `#catastrophic forgetting`, `#continual learning`, `#open source`

---

<a id="item-15"></a>
## [Apple Releases Swift-Based Linux Container Tool for Mac](https://github.com/apple/container) ⭐️ 7.0/10

Apple has open-sourced a new tool called 'container' that allows developers to create and run Linux containers as lightweight virtual machines on macOS, optimized for Apple Silicon. This provides a native, first-party solution for developers who need to run Linux containers on Mac, reducing reliance on third-party tools like Docker Desktop and improving performance on Apple Silicon. The tool is written in Swift and uses lightweight VMs instead of traditional container runtimes, requiring less memory than full VMs while booting quickly.

ossinsight · apple · Jun 11, 23:51

**Background**: Containers are a standard way to package and run applications with their dependencies, but macOS lacks native Linux container support. Apple's tool bridges this gap by leveraging virtualization technology to run Linux containers efficiently on Mac hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/apple/container">apple/container: A tool for creating and running Linux ... - GitHub</a></li>
<li><a href="https://opensource.apple.com/projects/container/">Apple Open Source</a></li>
<li><a href="https://www.reddit.com/r/selfhosted/comments/1l7ozmb/apple_now_supports_linux_containers_on_macos_26/">Apple now supports Linux containers on MacOS 26 : r/selfhosted - Reddit</a></li>

</ul>
</details>

**Discussion**: The community has shown interest, with the repo gaining 53 stars in 24 hours. Discussions on Reddit note that Apple's approach uses VMs, which is necessary for running Linux on macOS, and compare it favorably to other VM solutions.

**Tags**: `#containers`, `#macOS`, `#Apple Silicon`, `#Swift`, `#virtualization`

---
{% endraw %}
