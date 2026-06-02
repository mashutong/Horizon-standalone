---
layout: default
title: "Horizon Summary: 2026-06-02 (EN)"
date: 2026-06-02
lang: en
---

> From 26 items, 12 important content pieces were selected

---

1. [Backprop destroys V1 brain alignment; predictive coding preserves it](#item-1) ⭐️ 8.0/10
2. [Minimax M3 Found Without Political Censorship](#item-2) ⭐️ 8.0/10
3. [Local Qwen3.6-27B Replaces Claude in Multi-Agent Orchestrator](#item-3) ⭐️ 8.0/10
4. [1-bit and Ternary Bonsai Image 4B Models Enable Local Image Gen](#item-4) ⭐️ 8.0/10
5. [Benchmarking 20 Small LLMs on a 6GB GPU](#item-5) ⭐️ 8.0/10
6. [Microsoft unveils MAI-Thinking-1 and MAI-Code-1-Flash models](#item-6) ⭐️ 7.0/10
7. [PapersWithCode Revived with CVPR 2026 Conference Browsing](#item-7) ⭐️ 7.0/10
8. [Hobbyist Runs V100 Datacenter GPU in Gaming PC for Local LLMs](#item-8) ⭐️ 7.0/10
9. [Coding Benchmark: Step 3.7 vs Qwen Models](#item-9) ⭐️ 7.0/10
10. [llama.cpp Adds Thinking Mode Toggle with Reasoning Effort Levels](#item-10) ⭐️ 7.0/10
11. [Gemma 4 E4B with LiteRT: 2.4x text speedup over Q4 GGUF](#item-11) ⭐️ 7.0/10
12. [75M LLM Trained on 18B Tokens Beats 135M Model](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Backprop destroys V1 brain alignment; predictive coding preserves it](https://www.reddit.com/r/MachineLearning/comments/1tupu9z/backpropagation_destroys_v1_brain_alignment_in/) ⭐️ 8.0/10

A new study shows that backpropagation (BP) training destroys 90% of V1 brain alignment after just one epoch, while predictive coding (PC) and STDP preserve alignment with only 25–31% drops. This reveals a fundamental trade-off: global error signals improve higher visual areas but destroy early visual cortex alignment, challenging the biological plausibility of backprop and informing neuroAI model design. The study tracked representational similarity analysis (RSA) alignment to human fMRI across 8 training checkpoints for BP, feedback alignment (FA), PC, and STDP, using 5 seeds per rule. By epoch 40, PC and STDP significantly outperformed BP and FA in V1 alignment (Cohen's d > 5).

reddit · r/MachineLearning · ConfusionSpiritual19 · Jun 2, 12:43

**Background**: Representational similarity analysis (RSA) measures how similarly a model and a brain region represent stimuli by comparing their activation patterns. Backpropagation uses global error signals to update weights, while predictive coding and STDP rely on local learning rules, making them more biologically plausible.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.22401">Cross-Species RSA Reveals Conserved Early Visual Alignment ...</a></li>
<li><a href="https://github.com/nilsleut/CROSS_SPECIES_RSA/blob/main/README.md">CROSS_SPECIES_RSA/README.md at main · nilsleut ... - GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spike-timing-dependent_plasticity">Spike-timing-dependent plasticity - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters debated the implications for neuroAI, with some noting that the trade-off between global and local learning aligns with known brain hierarchies. Others questioned the small sample size (5 seeds) and the domain shift from CIFAR-10 to THINGS, but overall the findings were seen as robust and thought-provoking.

**Tags**: `#backpropagation`, `#brain alignment`, `#predictive coding`, `#STDP`, `#neuroAI`

---

<a id="item-2"></a>
## [Minimax M3 Found Without Political Censorship](https://i.redd.it/vgkda1ua5w4h1.png) ⭐️ 8.0/10

A bias benchmark researcher discovered that Minimax M3, unlike other Chinese LLMs, does not exhibit political censorship, making it an outlier among models from Chinese AI companies. This is significant because Chinese LLMs are typically heavily censored on political topics, and M3's lack of censorship could challenge assumptions about AI bias and open new possibilities for unbiased research and deployment. The finding comes from a Chinese/CCP AI bias benchmark, and the researcher noted that all other Minimax models are censored as typical for Chinese LLMs, highlighting M3 as a unique exception.

reddit · r/LocalLLaMA · DingyAtoll · Jun 2, 15:52

**Background**: Chinese LLMs are known to incorporate political censorship, often refusing to answer sensitive questions or repeating official state narratives. This is a common trait enforced by regulations and training data filtering. Minimax M3 is a recent open-weight model released on June 1, 2026, featuring frontier coding, 1M context, and native multimodality.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/minimax-m3-complete-guide/">MiniMax M3: Complete Guide to the Open-Weight Frontier Model ...</a></li>
<li><a href="https://huggingface.co/blog/leonardlin/chinese-llm-censorship-analysis">An Analysis of Chinese LLM Censorship and Bias with Qwen 2 Instruct</a></li>
<li><a href="https://head-post.com/chinese-ai-chatbots-censor-politically-sensitive-questions/">HEAD POST: Chinese AI chatbots censor politically sensitive...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#censorship`, `#AI bias`, `#Chinese AI`, `#Minimax`

---

<a id="item-3"></a>
## [Local Qwen3.6-27B Replaces Claude in Multi-Agent Orchestrator](https://www.reddit.com/r/LocalLLaMA/comments/1tunmam/replaced_claude_with_local_qwen3627b_in_my/) ⭐️ 8.0/10

A developer replaced Claude with the local Qwen3.6-27B model via Ollama on a single RTX 3090 for two weeks, testing it across 47 multi-step coding workflows in a multi-agent orchestrator. This real-world comparison shows that local models like Qwen3.6-27B can compete with proprietary models for reasoning tasks such as plan generation and memory extraction, potentially reducing costs and improving data privacy for AI agent systems. Qwen3.6-27B achieved ~95% schema-valid plan generation and caught ~60% of bugs in auto-review compared to Claude, but had a ~12% JSON tool-call format error rate versus Claude's ~0.5%, and was weaker in code generation and debugging.

reddit · r/LocalLLaMA · Interesting-Sock3940 · Jun 2, 11:05

**Background**: Multi-agent orchestrators coordinate multiple AI agents to complete complex tasks, with a lead agent planning and delegating to sub-agents. Qwen3.6-27B is a 27-billion-parameter dense language model from Alibaba's Qwen team, released in April 2026. Ollama is a platform for running large language models locally.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.6-27B-FP8">Qwen/ Qwen 3 . 6 - 27 B -FP8 · Hugging Face</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.6-27b">Qwen 3 . 6 27 B - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ollama">Ollama - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#local-llm`, `#multi-agent`, `#qwen`, `#claude`, `#ollama`

---

<a id="item-4"></a>
## [1-bit and Ternary Bonsai Image 4B Models Enable Local Image Gen](https://i.redd.it/yamygpzjqv4h1.png) ⭐️ 8.0/10

Two quantized versions of the Bonsai Image 4B diffusion transformer have been released: a 1-bit version at 0.93 GB and a ternary version at 1.21 GB, enabling image generation on local devices with minimal memory footprint. This breakthrough dramatically reduces the memory requirements for high-quality image generation, making it feasible to run powerful diffusion transformers on resource-constrained devices like smartphones and edge hardware, potentially democratizing AI image creation. The 1-bit model uses binary weights, while the ternary model uses weights constrained to {-1, 0, +1}, both achieving extreme compression of the original 4B-parameter model. The models are based on the diffusion transformer (DiT) architecture, which replaces the traditional U-Net backbone with a transformer for scalable image generation.

reddit · r/LocalLLaMA · Addyad · Jun 2, 14:28

**Background**: Quantization is a technique that reduces the precision of neural network weights and activations, often from 32-bit floating point to lower bit widths like 8-bit, 2-bit, or even 1-bit, to decrease model size and computational cost. Diffusion transformers (DiTs) are a class of generative models that use transformer architectures to iteratively denoise latent representations, producing high-quality images. The Bonsai Image 4B model originally had 4 billion parameters, requiring significant memory; quantization to 1-bit or ternary drastically reduces its footprint.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/neoxia/the-era-of-1-bit-llms-c7761b3688ce">The Era of 1 - bit LLMs. Introduction: Deep dive in LLM | Medium</a></li>
<li><a href="https://arxiv.org/abs/1612.01064">[1612.01064] Trained Ternary Quantization</a></li>
<li><a href="https://arxiv.org/abs/2212.09748">[2212.09748] Scalable Diffusion Models with Transformers</a></li>

</ul>
</details>

**Tags**: `#quantization`, `#diffusion transformers`, `#edge AI`, `#image generation`, `#model compression`

---

<a id="item-5"></a>
## [Benchmarking 20 Small LLMs on a 6GB GPU](https://www.reddit.com/r/LocalLLaMA/comments/1tuvs6l/benchmarks_of_20_small_llms_on_a_6gb_rtx_4050/) ⭐️ 8.0/10

A Reddit user benchmarked 20 small LLMs quantized to fit a 6GB RTX 4050 GPU, using a custom 6-probe qualitative test set focused on real-world tasks like file organization and log triage. This addresses a practical gap for users with limited GPU memory (6GB), providing actionable insights on which quantized models perform well for specific local tasks, rather than relying on generic leaderboard scores. The benchmark used LM Studio's database to select models and focused on Q4/Q6 GGUF quantizations. The custom test set included parseable tool-call and multi-turn tool-call probes, targeting behaviors relevant to the user's overnight automation tasks.

reddit · r/LocalLLaMA · drfritz2 · Jun 2, 16:16

**Background**: Quantization reduces the precision of a model's weights (e.g., from 16-bit to 4-bit), shrinking its memory footprint so it can run on consumer GPUs with limited VRAM. LM Studio is a popular tool for running local LLMs, and GGUF is a file format for quantized models. Many users with 6GB GPUs struggle to find practical benchmarks for their hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datacamp.com/tutorial/lm-studio">LM Studio Tutorial: Get Started with Local LLMs - DataCamp</a></li>
<li><a href="https://medium.com/@techresearchspace/what-is-quantization-in-llm-01ba61968a51">What is Quantization in LLM . Large Language Models ... | Medium</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmarks`, `#local inference`, `#quantization`, `#GPU`

---

<a id="item-6"></a>
## [Microsoft unveils MAI-Thinking-1 and MAI-Code-1-Flash models](https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything) ⭐️ 7.0/10

Microsoft announced two new text LLMs: MAI-Thinking-1, a 35-billion-parameter reasoning model, and MAI-Code-1-Flash, a 5-billion-parameter code model. MAI-Code-1-Flash is rolling out to GitHub Copilot individual users in Visual Studio Code. These models demonstrate that strong performance can be achieved with far fewer parameters, potentially lowering costs and enabling local deployment. The use of clean, commercially licensed data without third-party distillation sets a new standard for responsible AI development. MAI-Thinking-1 is preferred to Sonnet 4.6 in blind human evaluations, despite being only 35B parameters. Both models were trained from scratch on enterprise-grade, clean, and appropriately licensed data, without distillation from third-party models.

rss · Simon Willison · Jun 2, 22:21

**Background**: Large language models (LLMs) typically have billions of parameters, with larger models often being more capable but also more expensive to run. Parameter count is a measure of model size; smaller models can be faster and cheaper to deploy. Microsoft's new models challenge the assumption that bigger is always better.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-thinking-1/">Introducing MAI - Thinking - 1 | Microsoft AI</a></li>
<li><a href="https://microsoft.ai/news/introducingmai-code-1-flash/">Introducing MAI-Code-1-Flash | Microsoft AI</a></li>
<li><a href="https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/">MAI-Code-1-Flash is now available for GitHub Copilot</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#LLM`, `#AI models`, `#efficiency`, `#code generation`

---

<a id="item-7"></a>
## [PapersWithCode Revived with CVPR 2026 Conference Browsing](https://www.reddit.com/r/MachineLearning/comments/1tukrf4/browse_cvpr_2026_papers_on_paperswithcode_p/) ⭐️ 7.0/10

Niels from Hugging Face announced a new feature on PapersWithCode.co that allows users to browse CVPR 2026 papers, categorized by task, with links to GitHub, project pages, and Hugging Face artifacts. This revival of PapersWithCode provides a centralized, up-to-date resource for tracking state-of-the-art AI research, making it easier for the community to access and reproduce results from major conferences like CVPR. The feature indexes all CVPR 2026 papers with arXiv IDs, categorizes them by task, and tags them with GitHub URLs, project pages, Hugging Face artifacts, and evaluations. Users can also browse Oral and Spotlight papers separately.

reddit · r/MachineLearning · NielsRogge · Jun 2, 08:32

**Background**: PapersWithCode was a popular platform for tracking machine learning papers with code, but it was discontinued. Niels from Hugging Face launched a community revival at PapersWithCode.co two weeks ago, and the new conference browsing feature extends its utility for major AI conferences like CVPR, NeurIPS, and ICML.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/spaces/huggingface/paperswithcode">Paperswithcode - a Hugging Face Space by huggingface</a></li>
<li><a href="https://medium.com/paperswithcode">PapersWithCode - Medium</a></li>

</ul>
</details>

**Tags**: `#computer vision`, `#conference`, `#paperswithcode`, `#CVPR`, `#AI`

---

<a id="item-8"></a>
## [Hobbyist Runs V100 Datacenter GPU in Gaming PC for Local LLMs](https://blog.tymscar.com/posts/v100localllm/) ⭐️ 7.0/10

A hobbyist successfully installed a used Nvidia Tesla V100 datacenter GPU, purchased for around £200, into a standard gaming PC to run local large language models (LLMs) for inference. The blog post details the setup process, performance results, and practical challenges encountered. This demonstrates a cost-effective way for hobbyists and small-scale AI developers to access enterprise-grade GPU power for local LLM inference, bypassing expensive cloud services. It highlights the growing trend of repurposing datacenter hardware for personal AI workloads, potentially democratizing access to powerful AI models. The V100 GPU used is a Tesla V100 with 16GB or 32GB HBM2 memory, originally designed for servers and requiring specific cooling and power considerations. The user likely needed adapters for power connectors and had to manage the lack of display outputs, as datacenter GPUs often lack video ports.

reddit · r/LocalLLaMA · tymscar · Jun 2, 17:29

**Background**: Local LLM inference means running a trained language model on one's own hardware rather than relying on cloud APIs, offering benefits like privacy, offline access, and no usage fees. The Nvidia Tesla V100 is a datacenter GPU based on the Volta architecture, optimized for AI and HPC workloads, and is now available cheaply on the secondhand market as newer models emerge. However, datacenter GPUs typically lack display outputs and require active cooling solutions, making them challenging to integrate into consumer PCs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kitguru.net/components/graphic-cards/joao-silva/nvidia-releases-the-new-tesla-v100s-datacenter-graphics-card/">Nvidia releases the new Tesla V 100 s datacenter graphics ... | KitGuru</a></li>
<li><a href="https://lenovopress.lenovo.com/lp0767-gpu-options-for-thinksystem-servers">GPU Options for ThinkSystem Servers > Lenovo Press</a></li>
<li><a href="https://tet.com.tr/product/tesla-v100-nvidia-gpu-computing-high-performace-computing">Nvidia Tesla V 100 | High Performace Computing | GPU Computing</a></li>

</ul>
</details>

**Tags**: `#GPU`, `#Local LLM`, `#Hardware`, `#AI Inference`, `#DIY`

---

<a id="item-9"></a>
## [Coding Benchmark: Step 3.7 vs Qwen Models](https://remy.io/blog/coding-benchmark-qwen-step/) ⭐️ 7.0/10

A hands-on coding benchmark compares Step 3.7 Flash, Qwen 3.5 122B-A10B, Qwen 3.6 27B, and Qwen 3.6 35B-A3B on real-world tasks, revealing performance differences. This independent benchmark provides valuable insights for developers selecting coding LLMs, highlighting trade-offs between model size, efficiency, and coding capability. Step 3.7 Flash is a 198B-parameter MoE model with ~11B activated parameters, while Qwen 3.5 122B-A10B uses 122B total with 10B activated, and Qwen 3.6 35B-A3B has 35B total with 3B activated.

reddit · r/LocalLLaMA · remeh · Jun 2, 17:24

**Background**: Large language models (LLMs) for coding are often evaluated on benchmarks that may not reflect real-world usage. This test uses practical tasks to compare recent models from StepFun and Alibaba's Qwen series, which use Mixture-of-Experts (MoE) architectures to balance performance and efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://static.stepfun.com/blog/step-3.7-flash/">Step 3.7 Flash — A high-efficiency Flash model for Real-World</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.5-122b-a10b">Qwen 3 . 5 - 122 B - A 10 B - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://qwen.ai/blog?id=qwen3.6-35b-a3b">Qwen3.6-35B-A3B: Agentic Coding Power, Now Open to All</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#coding benchmark`, `#Qwen`, `#Step`, `#model comparison`

---

<a id="item-10"></a>
## [llama.cpp Adds Thinking Mode Toggle with Reasoning Effort Levels](https://github.com/ggml-org/llama.cpp/pull/23434) ⭐️ 7.0/10

Pull request #23434 by allozaur adds a UI toggle for thinking mode with configurable reasoning effort levels to llama.cpp's chat interface, enabling users to enable, disable, or limit reasoning steps. This feature gives end-users fine-grained control over how much reasoning an LLM performs, which can reduce unnecessary computation for simple queries or enable deeper reasoning for complex tasks, improving both efficiency and output quality. The toggle supports three levels: disabled, normal, and high effort, allowing users to adjust reasoning effort per conversation. The implementation builds on existing thinking block handling in llama.cpp's server and client.

reddit · r/LocalLLaMA · jacek2023 · Jun 2, 13:59

**Background**: Thinking mode refers to a model's ability to generate internal reasoning tokens (often enclosed in special delimiters) before producing a final answer. This is common in models like Qwen3 and Gemma 4, which use multi-token prediction (MTP) to speed up inference. llama.cpp is a popular open-source C++ implementation for running LLMs locally.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/15333">How should the client handle thinking blocks? - GitHub</a></li>
<li><a href="https://huggingface.co/bartowski/Qwen_Qwen3-32B-GGUF/discussions/1">bartowski/Qwen_Qwen3-32B-GGUF · How to disable thinking?</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Multi-token-prediction in Gemma 4 - The Keyword</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion highlights excitement about the feature, with users noting its value for controlling reasoning in local LLM deployments. Some comments reference related work on StepFun and Gemma MTP, indicating interest in broader MTP support.

**Tags**: `#llama.cpp`, `#UI`, `#reasoning`, `#open-source`, `#LLM`

---

<a id="item-11"></a>
## [Gemma 4 E4B with LiteRT: 2.4x text speedup over Q4 GGUF](https://www.reddit.com/r/LocalLLaMA/comments/1tuygn6/using_gemma_4_e4b_with_the_litert_engine_24x/) ⭐️ 7.0/10

A benchmark shows that running Gemma 4 E4B with Google's LiteRT engine achieves approximately 2.4x faster text generation compared to the Q4 GGUF quantized version in llama.cpp, while image captioning speed is only about 1.1x faster. This demonstrates that LiteRT with multi-token prediction (MTP) can significantly accelerate text generation for edge-deployable models like Gemma 4 E4B, offering a practical performance boost for local LLM inference without sacrificing image processing capability. The speedup is attributed to MTP, where a drafter predicts multiple tokens ahead and verifies them, giving ~1.5-2x throughput on top of the efficient LiteRT runtime. Image captioning shows only 11% improvement because the bottleneck is the vision encoder, not the text decoder.

reddit · r/LocalLLaMA · AnticitizenPrime · Jun 2, 17:46

**Background**: Gemma 4 E4B is a small vision-language model from Google designed for edge devices, with 'E' standing for 'effective' parameters. LiteRT is Google's runtime for on-device AI inference, supporting hardware acceleration. GGUF is a file format for quantized models used by llama.cpp, with Q4 being a 4-bit quantization level.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/google/gemma-4-E4B">google/gemma-4-E4B · Hugging Face</a></li>
<li><a href="https://ai.google.dev/edge/litert/next/litert_lm_npu">Run LLMs using LiteRT -LM | Google AI Edge | Google AI for Developers</a></li>
<li><a href="https://dev.to/pat9000/gguf-quantization-explained-q4km-vs-q5km-vs-q8-which-to-pick-2026-31pl">GGUF Quantization Explained: Q 4 _K_M vs... - DEV Community</a></li>

</ul>
</details>

**Discussion**: The Reddit post received positive engagement, with users noting the significant text speedup and discussing the potential of MTP for local inference. Some expressed interest in trying LiteRT for other models, while others questioned the comparison methodology and the practicality of deploying LiteRT outside Google's ecosystem.

**Tags**: `#Gemma 4`, `#LiteRT`, `#LLM inference`, `#benchmark`, `#local LLM`

---

<a id="item-12"></a>
## [75M LLM Trained on 18B Tokens Beats 135M Model](https://www.reddit.com/r/LocalLLaMA/comments/1tuyb8s/i_trained_a_75m_parameter_llm_from_scratch_on_18b/) ⭐️ 7.0/10

A developer trained KeyLM, a 75M parameter decoder-only LLM, on just 18B tokens and achieved an IFEval score of 17.85, surpassing the 135M parameter SmolLM-135M-Instruct's score of 17.15. This result challenges the common assumption that larger models and more data are always necessary, demonstrating that careful data selection and training can yield competitive instruction-following performance at a fraction of the cost. KeyLM uses a standard architecture with GQA (8 query / 2 KV heads), RoPE, SwiGLU, per-head QK-Norm, 24 layers, hidden size 512, and 2048 context length, trained on public data including FineWeb-Edu, Wikipedia, and Reddit.

reddit · r/LocalLLaMA · cakes_and_candles · Jun 2, 17:41

**Background**: IFEval (Instruction-Following Evaluation) is a benchmark that tests a model's ability to follow verifiable instructions, such as formatting constraints or length limits. GGUF is a file format optimized for running LLMs locally on consumer hardware. GQA (Grouped Query Attention) is an attention mechanism that improves inference efficiency by grouping query heads.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/ifeval">IFEval Leaderboard</a></li>
<li><a href="https://pguso.medium.com/the-gguf-format-explained-making-ai-models-run-anywhere-even-on-your-laptop-30dcb45358da">The GGUF Format Explained: Making AI Models Run... | Medium</a></li>
<li><a href="https://www.geeksforgeeks.org/deep-learning/grouped-query-attention-gqa/">Grouped Query Attention ( GQA ) - GeeksforGeeks</a></li>

</ul>
</details>

**Discussion**: The community discussion on Reddit was positive, with users asking technical questions about the architecture and training details, and expressing interest in the efficiency results. Some questioned the benchmark significance, but overall the sentiment was validating.

**Tags**: `#LLM`, `#efficiency`, `#small models`, `#training`, `#benchmarks`

---