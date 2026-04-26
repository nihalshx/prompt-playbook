---
layout: default
title: "14 · Prompt Chaining"
parent: Advanced Techniques
nav_order: 4
---

# Prompt Chaining
{: .no_toc }

**Tier:** Advanced · **Task types:** Long workflows, multi-stage content, complex pipelines · **Difficulty:** ⭐⭐⭐⭐☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Prompt chaining breaks a complex, multi-stage task into a **sequence of dependent prompts** where the output of each step feeds as input to the next. Rather than asking a single prompt to do everything (which degrades quality on long tasks), chaining allows each prompt to do one thing well.

Prompt chaining is the architecture underlying most LLM document processing pipelines and content generation systems.

---

## Use Cases

- **Long-form content generation** — research → outline → draft → edit → format as four chained steps, each with focused instructions
- **Document processing pipelines** — extract → classify → summarise → transform, where each stage has specific quality requirements
- **Multi-perspective analysis** — generate arguments for → generate arguments against → synthesise into balanced assessment

---

## Weak Approach (Single Prompt)

```
Research the pros and cons of remote work, write a balanced 800-word article
with an introduction, three supporting points, counterarguments, and a conclusion
formatted for a business audience.
```

**Problem:** This single prompt asks the model to simultaneously research, plan, write, balance, and format — competing demands that produce output weaker than chaining would achieve.

---

## Improved Approach (Chained Prompts)

**Chain Step 1 — Generate Key Points:**
```
List 5 well-evidenced benefits and 5 well-evidenced drawbacks of remote work
for knowledge workers. For each point, provide one supporting statistic or study.
Format as two numbered lists. No prose.
```

**Chain Step 2 — Build Outline (feeding Step 1 output):**
```
Using these research points: [Step 1 output]

Create a structured outline for an 800-word balanced article on remote work
for a business audience. Include: intro hook, 3 main sections, counterarguments
section, and conclusion. One sentence per section describing its focus.
```

**Chain Step 3 — Draft (feeding Step 2 output):**
```
Write the full 800-word article following this outline: [Step 2 output]
Use the research points from [Step 1 output] to support claims.
Tone: professional, evidence-led, not preachy.
```

**Chain Step 4 — Edit:**
```
Edit this article for: clarity, cut to 750 words, strengthen the opening hook,
ensure both sides are given equal weight. [Step 3 output]
```

**Assessment:** Each step produces a focused, high-quality output that serves as clean input for the next. Final quality is substantially higher than a single-prompt approach.

---

## Verdict

Prompt chaining is the right architecture for any task complex enough that a single prompt produces mediocre results. The cost is engineering overhead — chains require code to pass outputs between steps, and errors cascade. But for production systems handling complex content tasks, chaining is often the difference between a demo and a deployable product.

---

## Common Pitfalls

**1. Not validating intermediate outputs**
If Step 2 produces a poor outline, Step 3 will draft a poor article. Build quality checkpoints between steps, especially in automated pipelines.

**2. Losing context across chain steps**
By Step 4, the model may have drifted from original requirements. Include a brief requirements reminder at each step, not just Step 1.

**3. Over-engineering simple tasks**
A three-sentence summary does not need a four-step chain. Match complexity to the task.
