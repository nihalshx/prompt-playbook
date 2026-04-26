---
layout: default
title: Advanced Techniques
nav_order: 3
has_children: true
permalink: docs/advanced
---

# Advanced Techniques

The ten advanced techniques are designed for complex, multi-step, or high-stakes tasks where foundational techniques alone are insufficient. These require more careful prompt engineering, more context budget, and often more iterative refinement — but they unlock capabilities that simpler techniques cannot reach.

**Who these are for:** Practitioners building LLM-powered products, researchers evaluating model behaviour, and engineers designing prompt pipelines for production systems.

---

## Techniques in This Section

11. [Self-Consistency](11-self-consistency) — Sampling multiple reasoning paths and majority-voting the answer
12. [ReAct Prompting](12-react-prompting) — Interleaving reasoning and action in an agentic loop
13. [Step-Back Prompting](13-step-back) — Reasoning from first principles before tackling specifics
14. [Prompt Chaining](14-prompt-chaining) — Breaking long tasks into sequential, dependent prompts
15. [Least-to-Most Decomposition](15-least-to-most) — Solving the simplest sub-problem first, building to the hardest
16. [Generated Knowledge](16-generated-knowledge) — Prompting the model to generate useful context before answering
17. [Calibration Prompts](17-calibration-prompts) — Eliciting confidence estimates and surfacing uncertainty
18. [Directional Stimulus](18-directional-stimulus) — Using hints or keywords to steer response direction
19. [Meta-Prompting](19-meta-prompting) — Using an LLM to write or improve prompts
20. [Evaluation Prompts](20-evaluation-prompts) — Using LLMs as judges to score or compare outputs

---

{: .warning }
Advanced techniques consume more tokens, often require multiple API calls, and have more failure modes than foundational techniques. Always establish a foundational baseline before applying advanced methods.
