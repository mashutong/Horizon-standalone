---
layout: default
title: "Horizon Summary: 2026-06-20 (EN)"
date: 2026-06-20
lang: en
---

{% raw %}
> From 25 items, 15 important content pieces were selected

---

1. [Project Valhalla Value Types Arrive in JDK 28](#item-1) ⭐️ 9.0/10
2. [GLM-5.2: Most Powerful Open-weights LLM Released](#item-2) ⭐️ 9.0/10
3. [Norway bans AI for elementary school students](#item-3) ⭐️ 8.0/10
4. [AI Economics Shift Toward Open-Weight Models](#item-4) ⭐️ 8.0/10
5. [Ohio State open-sources QUEST-35B deep research agent](#item-5) ⭐️ 8.0/10
6. [EU selects EUROPA consortium for open-source frontier AI model](#item-6) ⭐️ 8.0/10
7. [Eagle3 speculative decoding lands in llama.cpp for Qwen](#item-7) ⭐️ 8.0/10
8. [Suitcase Robot Gets High via Real Gas Sensor Modulating LLM](#item-8) ⭐️ 8.0/10
9. [Triton 3.7.1 Patch Fixes Two Critical Regressions](#item-9) ⭐️ 7.0/10
10. [ATProto Has No Instances, Explains Dan Abramov](#item-10) ⭐️ 7.0/10
11. [Hyundai acquires full ownership of Boston Dynamics](#item-11) ⭐️ 7.0/10
12. [MCP's Key Value: Auth Isolation Outside Context Window](#item-12) ⭐️ 7.0/10
13. [Datasette Apps: Sandboxed HTML/JS Apps with SQL Access](#item-13) ⭐️ 7.0/10
14. [New Agentic Benchmark: Claude Fable and GLM 5.2 Lead](#item-14) ⭐️ 7.0/10
15. [$1800 4x RTX 5060 Ti 16GB runs Qwen 27B at 55 tok/s](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Project Valhalla Value Types Arrive in JDK 28](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 9.0/10

Project Valhalla's value types, a decade-long effort to introduce dense memory layouts and improved performance, are finally arriving in JDK 28, allowing the JVM to store values directly in arrays without object headers or pointers. This represents a major paradigm shift for Java performance and memory efficiency, enabling applications to handle large data sets with significantly reduced memory footprint and improved cache locality, benefiting fields like big data, machine learning, and high-frequency trading. Value types are immutable and identity-free, meaning they lack object headers and can be flattened in arrays, but heap flattening is limited to objects with 64-bit or smaller representations; larger value types still incur some overhead.

hackernews · philonoist · Jun 19, 06:35 · [Discussion](https://news.ycombinator.com/item?id=48595511)

**Background**: In traditional Java, every object has a header (12-16 bytes) and is accessed via pointers, causing memory overhead and poor cache performance. Project Valhalla introduces value types that behave like primitives but can have methods and fields, combining object-oriented abstraction with the efficiency of primitives. This is achieved through JEPs such as JEP 401 (Primitive Objects) and JEP 402 (Value Objects), building on earlier work like JEP 450 (Compact Object Headers).

<details><summary>References</summary>
<ul>
<li><a href="https://openjdk.org/projects/valhalla/">Project Valhalla - OpenJDK</a></li>
<li><a href="https://openjdk.org/jeps/450">JEP 450: Compact Object Headers (Experimental)</a></li>
<li><a href="https://www.infoq.com/news/2025/06/java-25-compact-object-headers/">Java 25 Integrates Compact Object Headers with JEP 519 - InfoQ</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some praise the technical achievement but critique limitations like heap flattening constraints for larger objects, while others defend Java's evolution and note that many critics are unaware of modern JVM improvements. There is also debate about the null-safety trade-offs in the simplified model.

**Tags**: `#Java`, `#JVM`, `#Project Valhalla`, `#performance`, `#memory model`

---

<a id="item-2"></a>
## [GLM-5.2: Most Powerful Open-weights LLM Released](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

Z.ai released GLM-5.2, a 753B parameter open-weights LLM under MIT license, with a 1M token context window and Mixture of Experts architecture with 40 active parameters. GLM-5.2 is likely the most powerful text-only open-weights model, topping the Artificial Analysis Intelligence Index and ranking 2nd on Code Arena WebDev, challenging proprietary models like Claude Fable 5. The model uses 43k output tokens per task on average, more than competitors, and is available via OpenRouter at $1.40/M input and $4.40/M output tokens. It lacks image input, yet excels at front-end coding tasks.

rss · Simon Willison · Jun 17, 23:58

**Background**: GLM-5.2 is a Mixture of Experts (MoE) model, which uses multiple specialized sub-networks (experts) and activates only a subset per token, enabling high capacity with lower computational cost. Its 1M token context window allows processing very long documents, such as entire codebases or lengthy books. The model introduces IndexShare, a technique that reuses indexers across sparse attention layers to reduce FLOPs by 2.9× at long contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/GLM-5.2 · Hugging Face</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM-5.2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>

</ul>
</details>

**Discussion**: The community is excited about GLM-5.2's performance, especially its SVG generation and coding abilities. Some users note it is token-hungry compared to peers, but overall sentiment is positive, with many praising its open license and strong benchmarks.

**Tags**: `#LLM`, `#open-weights`, `#AI`, `#GLM-5.2`, `#Z.ai`

---

<a id="item-3"></a>
## [Norway bans AI for elementary school students](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/) ⭐️ 8.0/10

Norway announced a near-total ban on AI use for elementary school students aged 6-13, and restricted use for students aged 14-16 under teacher supervision, effective from the 2026 school year. This policy sets a precedent for national-level AI regulation in education, highlighting concerns that generative AI may hinder foundational learning skills like reading, writing, and critical thinking in young children. The ban applies to all AI tools, including generative AI like ChatGPT, and covers both classroom and homework use. The government cited the need to protect children's cognitive development and privacy.

hackernews · ilreb · Jun 19, 16:03 · [Discussion](https://news.ycombinator.com/item?id=48600093)

**Background**: Generative AI tools like ChatGPT have rapidly entered classrooms worldwide, raising concerns about academic integrity, over-reliance, and developmental appropriateness. Norway's move is one of the strictest national policies to date, contrasting with other countries that have issued only guidelines or voluntary frameworks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research">Guidance for generative AI in education and research</a></li>
<li><a href="https://www.edweek.org/technology/states-put-unprecedented-attention-on-ais-role-in-schools/2026/01">States Put 'Unprecedented' Attention on AI's Role in Schools</a></li>
<li><a href="https://www.ed.gov/about/ed-overview/artificial-intelligence-ai-guidance">Artificial Intelligence (AI) Guidance - U.S. Department of Education</a></li>

</ul>
</details>

**Discussion**: The community largely supports the ban, drawing parallels to not giving calculators before understanding arithmetic. Some educators note AI has been a disaster for student outcomes, while others question how the ban would be enforced without increasing teacher workload.

**Tags**: `#AI regulation`, `#education`, `#policy`, `#generative AI`, `#Norway`

---

<a id="item-4"></a>
## [AI Economics Shift Toward Open-Weight Models](https://www.reddit.com/r/LocalLLaMA/comments/1ua5b16/the_economics_of_ai_are_starting_to_favor_open/) ⭐️ 8.0/10

A Reddit analysis argues that open-weight AI models like DeepSeek, Qwen, and GLM are now competitive with closed APIs on cost-performance, challenging the assumption that frontier models require expensive proprietary access. This shift could democratize AI access for businesses, reducing reliance on expensive API tokens and enabling more cost-effective deployment of capable models for most real-world tasks. The analysis highlights that open models dominate the upper-left quadrant of a cost-intelligence chart, offering high intelligence at low cost, while closed models still provide advantages in zero infrastructure, reliability, and faster access to frontier capabilities.

reddit · r/LocalLLaMA · /u/Mr-serial_killer · Jun 19, 15:38

**Background**: Open-weight models release the trained neural network parameters, allowing users to download and run them locally, unlike closed APIs that only provide online access. DeepSeek, a Chinese AI company, gained attention for training competitive models at a fraction of the cost of rivals like GPT-4, using techniques like mixture of experts and weaker chips due to export restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_Coder">DeepSeek Coder</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you've been told - Open Source Initiative</a></li>

</ul>
</details>

**Discussion**: The Reddit community largely agrees with the analysis, noting that for many tasks the capability gap is shrinking while cost differences remain large. Some commenters caution that closed models still offer better reliability and support for mission-critical applications.

**Tags**: `#AI economics`, `#open-source AI`, `#model comparison`, `#cost-performance`, `#DeepSeek`

---

<a id="item-5"></a>
## [Ohio State open-sources QUEST-35B deep research agent](https://www.reddit.com/r/LocalLLaMA/comments/1u9w6my/researchers_trained_a_deep_research_agent_with_32/) ⭐️ 8.0/10

Researchers at Ohio State University released QUEST-35B, an open-source Deep Research agent trained with only 32 H100 GPUs and ~8K synthetic samples, including full training recipe, code, weights, and datasets. This lowers the barrier for reproducing and building upon frontier-level deep research agents, enabling broader community participation and accelerating open-source AI research. QUEST-35B achieves competitive performance against several frontier closed-source deep research systems, and the team open-sourced everything under Apache-2.0 license on Hugging Face.

reddit · r/LocalLLaMA · /u/BuildwithVignesh · Jun 19, 08:20

**Background**: Deep Research agents are AI systems that autonomously conduct multi-step web research, analyze sources, and generate comprehensive reports. Training such agents typically requires massive compute resources and proprietary data, making them inaccessible to most researchers.

<details><summary>References</summary>
<ul>
<li><a href="https://osu-nlp-group.github.io/QUEST/">QUEST: Training Frontier Deep Research Agents with Fully Synthetic Tasks</a></li>
<li><a href="https://huggingface.co/osunlp/QUEST-35B-SFT/discussions">osunlp/QUEST-35B-SFT · Discussions</a></li>
<li><a href="https://en.wikipedia.org/wiki/H100_GPU">H100 GPU</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion highlights that while QUEST-35B is a significant step, the biggest remaining gaps include reliability, tool-use robustness, and the ability to handle very long contexts compared to frontier closed systems.

**Tags**: `#open-source`, `#deep research`, `#LLM`, `#AI agent`, `#NLP`

---

<a id="item-6"></a>
## [EU selects EUROPA consortium for open-source frontier AI model](https://www.reddit.com/r/LocalLLaMA/comments/1ua5otx/commission_selects_europa_consortium_as_the/) ⭐️ 8.0/10

The European Commission has selected the EUROPA consortium, led by Italian company Domyn, as the winner of the Frontier AI Grand Challenge to build an open-source frontier AI model with over 400 billion parameters covering all 24 official EU languages. This initiative strengthens Europe's AI sovereignty by developing advanced AI on its own infrastructure, making frontier AI accessible to businesses, researchers, and public institutions across Europe's linguistic diversity. The model must have more than 400 billion parameters, a scale associated with the world's most advanced AI systems, and will be openly available. The Frontier AI Grand Challenge was launched in February 2026 by the European Commission and the EuroHPC Joint Undertaking.

reddit · r/LocalLLaMA · /u/pmttyji · Jun 19, 15:53

**Background**: The Frontier AI Grand Challenge is a flagship EU-wide competition aimed at bridging the strategic gap in high-end AI development by fostering sovereign, large-scale European AI models. It provides massive computational power and support through EuroHPC. Domyn specializes in responsible AI for regulated industries, emphasizing full control over models, data, and infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://digital-strategy.ec.europa.eu/en/news/commission-selects-europa-consortium-winner-frontier-ai-grande-challenge-project-build-european">Commission selects EUROPA consortium as the winner of the Frontier AI Grande Challenge, a project to build European open-source frontier AI model in all 24 EU languages | Shaping Europe’s digital future</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/funding/turning-strategy-action-commission-launches-frontier-ai-grand-challenge">Turning strategy into action: Commission launches Frontier AI ...</a></li>
<li><a href="https://www.domyn.com/">Domyn | Your own domain of intelligence</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes community insights on feasibility and implications, but no specific comments were provided.

**Tags**: `#AI`, `#Open Source`, `#European Union`, `#Frontier Model`, `#Multilingual`

---

<a id="item-7"></a>
## [Eagle3 speculative decoding lands in llama.cpp for Qwen](https://www.reddit.com/r/LocalLLaMA/comments/1u9z4e4/the_eagle3_has_landed_for_qwen/) ⭐️ 8.0/10

Eagle3 speculative decoding is now available in llama.cpp release b9723, enabled via the --spec-type draft-eagle3 flag, allowing users to accelerate Qwen model inference with a draft model. This integration brings significant inference speedups for local Qwen model deployment, making high-performance speculative decoding accessible to the open-source community and reducing latency for real-time applications. The draft model consumes additional VRAM and tensor parallelism is not currently supported, which may limit its use on tight setups or multi-GPU configurations. Performance is reported to be similar to draft-mtp speculative decoding.

reddit · r/LocalLLaMA · /u/Legitimate-Dog5690 · Jun 19, 11:11

**Background**: Speculative decoding accelerates LLM inference by using a smaller draft model to generate candidate tokens that are then verified by the larger target model. Eagle3 is an advanced speculative decoding technique that improves efficiency by predicting multiple tokens in parallel. Tensor parallelism splits model layers across multiple GPUs to reduce memory per device, but its absence in this feature means users with multiple GPUs cannot yet benefit from combined speedups.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in ...</a></li>
<li><a href="https://huggingface.co/blog/lujangusface/tw-eagle3-gpu">Speculative Decoding in Practice: How EAGLE3 Makes LLMs Faster ...</a></li>
<li><a href="https://developers.redhat.com/articles/2025/07/01/fly-eagle3-fly-faster-inference-vllm-speculative-decoding">Fly Eagle(3) fly: Faster inference with vLLM & speculative decoding</a></li>

</ul>
</details>

**Discussion**: The community is excited about the performance gains but notes limitations: no tensor parallelism support and extra VRAM usage. Users hope for future improvements to support multi-GPU setups and tighter memory footprints.

**Tags**: `#llama.cpp`, `#speculative decoding`, `#Qwen`, `#inference optimization`, `#local LLM`

---

<a id="item-8"></a>
## [Suitcase Robot Gets High via Real Gas Sensor Modulating LLM](https://www.reddit.com/r/LocalLLaMA/comments/1u9a17y/my_suitcase_robot_gets_high_now_off_a_real_gas/) ⭐️ 8.0/10

A suitcase robot named Sparky uses an MQ-2 gas sensor to dynamically adjust LLM sampling parameters (temperature, top_p, top_k) in real time, causing its speech to become progressively more incoherent as smoke is detected. This novel integration of a physical sensor with LLM sampling parameters demonstrates a creative, real-time modulation of model behavior, opening up possibilities for interactive AI that responds to environmental stimuli in a non-scripted manner. The MQ-2 sensor reads smoke every 0.5 seconds against an adaptive clean-air baseline, converting hits into a 0-10 phase that climbs with smoke and decays over minutes. The phase rewires the sampler per token: temperature from 1.0 to ~1.6, top_p from 0.95 to 0.99, top_k from 64 to 120.

reddit · r/LocalLLaMA · /u/CreativelyBankrupt · Jun 18, 15:52

**Background**: LLM sampling parameters like temperature, top_p, and top_k control the randomness and diversity of generated text. Higher temperature increases randomness, higher top_p includes more low-probability tokens, and higher top_k expands the candidate pool. The MQ-2 is a semiconductor gas sensor that detects a broad range of combustible gases and smoke, commonly used for gas leak detection.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/MQ-2_and_MQ-9_gas_sensors">MQ-2 and MQ-9 gas sensors</a></li>
<li><a href="https://rumn.medium.com/setting-top-k-top-p-and-temperature-in-llms-3da3a8f74832">Setting Top - K , Top - P and Temperature in LLMs | Medium</a></li>
<li><a href="https://www.carneiro.dev/blog/ai/llm-sampling-parameters">Luiz Carneiro Blog - Understanding Temperature , Top - p , and Top - k in...</a></li>

</ul>
</details>

**Discussion**: The community praised the project for its originality and technical depth, with many finding it humorous. A key discussion point was the sensor's inability to distinguish cannabis smoke from other smoke, and users suggested alternatives like an e-nose or specific VOC sensors for better discrimination.

**Tags**: `#LLM`, `#hardware integration`, `#creative AI`, `#sensor`, `#real-time`

---

<a id="item-9"></a>
## [Triton 3.7.1 Patch Fixes Two Critical Regressions](https://github.com/triton-lang/triton/releases/tag/v3.7.1) ⭐️ 7.0/10

Triton 3.7.1, a patch release on top of 3.7.0, fixes two regressions: a missing fence for async copy dependencies and an LLVM InstCombine miscompilation. No new features or API changes are included. These fixes address correctness issues that could produce incorrect GPU computation results, which is critical for users relying on Triton for high-performance GPU programming. The patch ensures reliability without introducing breaking changes. The first fix adds async read dependencies to FenceAsync to prevent a race condition between shared-memory stores and async copy operations. The second fix corrects an LLVM InstCombine optimization that mishandled known-zero bits from the left-hand side of an addition.

github · atalman · Jun 18, 14:38

**Background**: Triton is a compiler and language for GPU programming that simplifies writing efficient GPU kernels. Async copy is a feature in NVIDIA Ampere GPUs that allows data transfers to overlap with computation. LLVM InstCombine is an optimization pass that simplifies LLVM IR, but can sometimes introduce miscompilations.

<details><summary>References</summary>
<ul>
<li><a href="https://discourse.llvm.org/t/modeling-gpu-async-copy-ampere-feature/4924">Modeling GPU async copy (Ampere feature) - LLVM Discussion Forums</a></li>
<li><a href="https://github.com/llvm/llvm-project/issues/142518">InstCombine miscompilation · Issue #142518 · llvm / llvm -project</a></li>

</ul>
</details>

**Tags**: `#triton`, `#gpu`, `#compiler`, `#bug-fix`, `#llvm`

---

<a id="item-10"></a>
## [ATProto Has No Instances, Explains Dan Abramov](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 7.0/10

Dan Abramov published a blog post clarifying that ATProto, the protocol behind Bluesky, does not have 'instances' like Mastodon, using a blog analogy to explain its architecture of relays, app views, and personal data servers. This clarification helps prevent confusion between ATProto and ActivityPub-based systems, highlighting a fundamental architectural difference that affects decentralization and user experience in decentralized social media. In ATProto, relays aggregate data from personal data servers (PDSes) and provide a firehose to app views, which are separate services that process data for specific applications like Bluesky. This separation allows each component to scale independently, unlike Mastodon's monolithic instances.

hackernews · danabramov · Jun 19, 15:10 · [Discussion](https://news.ycombinator.com/item?id=48599515)

**Background**: ATProto (Authenticated Transfer Protocol) is an open standard for decentralized social networking, developed by Bluesky. It separates data hosting (PDS), data aggregation (relays), and data consumption (app views), whereas ActivityPub (used by Mastodon) combines these into instances. This design aims to reduce fragmentation and improve performance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.wiki/en/wiki/reference/core-architecture/relay">Relays | AT Protocol Community Wiki</a></li>
<li><a href="https://atproto.wiki/en/wiki/reference/core-architecture/appview">AppViews | AT Protocol Community Wiki</a></li>

</ul>
</details>

**Discussion**: Community comments on Hacker News debated the practical centralization of Bluesky, with some noting that Bluesky Corporation runs the main app and hosts most user data. Others praised the architectural separation of relays, app views, and PDSes as a beautiful system design solution.

**Tags**: `#ATProto`, `#decentralization`, `#social media`, `#protocols`, `#Bluesky`

---

<a id="item-11"></a>
## [Hyundai acquires full ownership of Boston Dynamics](https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/) ⭐️ 7.0/10

Hyundai Motor Group has exercised its option to purchase the remaining 9% stake in Boston Dynamics from SoftBank, completing full ownership of the robotics company for a total valuation of approximately $1.1 billion. This acquisition positions Hyundai to lead in robotics and manufacturing automation, especially as South Korea faces a projected 25% decline in working-age population by 2040, making automation critical for economic sustainability. Hyundai initially purchased an 80% controlling interest in Boston Dynamics from SoftBank in December 2020 for $880 million, with a put option that SoftBank has now exercised. The remaining 9% stake was acquired at a valuation consistent with the original $1.1 billion deal.

hackernews · ck2 · Jun 19, 16:28 · [Discussion](https://news.ycombinator.com/item?id=48600312)

**Background**: Boston Dynamics is an American robotics company known for highly mobile robots like Spot, Atlas, and Stretch. Hyundai Motor Group has been integrating robotics into its broader AI and manufacturing strategy, as highlighted by its AI Robotics Strategy unveiled at CES 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Boston_Dynamics">Boston Dynamics - Wikipedia</a></li>
<li><a href="https://www.hyundaimotorgroup.com/en/news/hyundai-motor-group-announces-ai-robotics-strategy--to-lead-human-centered-robotics-era-at-ces-2026">Hyundai Motor Group Announces AI Robotics Strategy to Lead ...</a></li>

</ul>
</details>

**Discussion**: Commenters debated the value of humanoid robots versus purpose-built robots for manufacturing, with some arguing that humanoid forms are inefficient. Others linked the acquisition to South Korea's demographic decline and high robot density, suggesting a strategic focus on general-purpose robotics beyond automotive.

**Tags**: `#robotics`, `#acquisition`, `#Hyundai`, `#Boston Dynamics`, `#manufacturing`

---

<a id="item-12"></a>
## [MCP's Key Value: Auth Isolation Outside Context Window](https://simonwillison.net/2026/Jun/19/sean-lynch/#atom-everything) ⭐️ 7.0/10

Sean Lynch argues that the Model Context Protocol (MCP) offers a unique advantage over traditional skills or CLI approaches by isolating the authentication flow outside the agent's context window, potentially serving as an auth gateway for APIs. This insight reframes MCP's role from a general-purpose context provider to a security boundary, which could simplify agent architectures and reduce context window pollution from auth logic. Lynch suggests that the idealized form of MCP might be nothing more than an auth gateway for APIs, and that alone would be a win. This perspective highlights MCP's potential to handle authentication delegation without burdening the LLM's limited context.

rss · Simon Willison · Jun 19, 22:45

**Background**: The Model Context Protocol (MCP) is an open standard for connecting AI applications, particularly LLMs, to external data sources and tools. In agent systems, authentication flows often consume valuable context window space, limiting the agent's ability to process other information. MCP can abstract this complexity away by handling auth outside the agent's direct context.

<details><summary>References</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://modelcontextprotocol.io/specification/2025-03-26">Specification - Model Context Protocol</a></li>
<li><a href="https://github.com/jscaballerodev/mcp-auth-security-gateway">GitHub - jscaballerodev/ mcp - auth -security- gateway : A plug-and-play...</a></li>

</ul>
</details>

**Tags**: `#model-context-protocol`, `#llms`, `#ai`, `#authentication`, `#agent-systems`

---

<a id="item-13"></a>
## [Datasette Apps: Sandboxed HTML/JS Apps with SQL Access](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 7.0/10

Simon Willison released the datasette-apps plugin, which allows hosting sandboxed HTML+JavaScript applications inside Datasette with read/write SQL access via iframe sandboxing and CSP headers. This plugin transforms Datasette from a read-only data publishing tool into a full application platform, enabling users to build custom interactive dashboards and tools directly on their data without external hosting. Apps run in a sandboxed iframe with allow-scripts and allow-forms, and are blocked from making external HTTP requests via CSP, preventing data exfiltration. Write queries require pre-configured stored queries.

rss · Simon Willison · Jun 18, 23:58

**Background**: Datasette is an open-source tool for exploring and publishing data, traditionally offering a JSON API for building custom frontends. The new plugin allows those frontends to be hosted directly within Datasette, simplifying deployment and security.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/datasette/datasette-apps">GitHub - datasette/datasette-apps: Apps that live inside Datasette · GitHub</a></li>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps: Host custom HTML applications inside Datasette</a></li>
<li><a href="https://datasette.io/blog/2026/datasette-apps">Host applications inside Datasette with Datasette Apps - Datasette Blog</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#plugin`, `#sql`, `#web-applications`, `#sandbox`

---

<a id="item-14"></a>
## [New Agentic Benchmark: Claude Fable and GLM 5.2 Lead](https://www.reddit.com/r/LocalLLaMA/comments/1u9yt6v/new_agentic_benchmark_out_claude_fable_and_glm_52/) ⭐️ 7.0/10

Artificial Analysis released AA-Briefcase, a new agentic benchmark that evaluates LLMs on realistic multi-week knowledge work projects, and found Claude Fable and GLM 5.2 top their respective cohorts. This benchmark tests planning and task execution, areas where traditional benchmarks are saturated, providing a more meaningful evaluation of frontier model capabilities. AA-Briefcase uses a combined Elo metric aggregating rubric pass rate, analytical quality, and presentation quality, and is designed to resist 'benchmaxxing'—optimizing for leaderboard scores rather than true capability.

reddit · r/LocalLLaMA · /u/Few_Painter_5588 · Jun 19, 10:54

**Background**: Benchmaxxing refers to the practice of optimizing models specifically for benchmark metrics, which can inflate scores without improving real-world performance. AA-Briefcase aims to mitigate this by using complex, multi-step tasks that are harder to game. The benchmark was built by industry experts and involves thousands of input tokens per task.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/articles/aa-briefcase">Announcing AA-Briefcase: a frontier knowledge work evaluation | Artificial Analysis</a></li>
<li><a href="https://www.jeannelizabeth.com/blog/benchmaxxing-the-ugly-art-of-optimising-for-leaderboards">What is Benchmaxxing? — Jeanne Elizabeth Daniel</a></li>

</ul>
</details>

**Discussion**: The Reddit community praised the benchmark for being novel and resistant to saturation, with users noting that it tests real agentic capabilities rather than memorization. Some expressed interest in seeing more models evaluated.

**Tags**: `#LLM`, `#benchmark`, `#agentic`, `#AI evaluation`, `#Claude`

---

<a id="item-15"></a>
## [$1800 4x RTX 5060 Ti 16GB runs Qwen 27B at 55 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1uah3oc/1800_in_gpu_cost_running_with_p2p_running/) ⭐️ 7.0/10

A Reddit user shared a $1800 4x RTX 5060 Ti 16GB P2P setup running Qwen 27B FP8 with 262K context at 55 tok/s using vLLM with tensor parallelism and speculative decoding. This demonstrates a highly cost-effective multi-GPU inference setup for large language models, making long-context, high-throughput inference accessible to individual users and small teams. The setup uses 4x RTX 5060 Ti 16GB with P2P enabled via NCCL, vLLM with tensor-parallel-size 4, FP8 model weights, BF16 KV cache, and speculative decoding with 3 draft tokens, achieving 55.67 tok/s output throughput.

reddit · r/LocalLLaMA · /u/joorklee · Jun 19, 23:30

**Background**: Tensor parallelism splits model layers across multiple GPUs to reduce memory per GPU and enable larger models. NCCL P2P allows direct GPU-to-GPU communication, critical for multi-GPU inference. FP8 is a low-precision format that reduces memory and bandwidth usage while maintaining acceptable accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/serving/parallelism_scaling/">Parallelism and Scaling - vLLM</a></li>
<li><a href="https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html">Environment Variables — NCCL 2.30.3 documentation</a></li>
<li><a href="https://arxiv.org/html/2411.08719v1">Balancing Speed and Stability: The Trade-offs of FP8 vs. BF16 ...</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#multi-GPU`, `#cost optimization`, `#vLLM`, `#local LLM`

---
{% endraw %}
