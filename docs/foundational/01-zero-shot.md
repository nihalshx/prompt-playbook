---
layout: default
title: "01 · Zero-Shot Prompting"
parent: Foundational Techniques
nav_order: 1
---

# Zero-Shot Prompting
{: .no_toc }

**Tier:** Foundational · **Task types:** All · **Difficulty:** ⭐☆☆☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Zero-shot prompting means asking a language model to complete a task **without providing any examples**. The model must rely entirely on its pre-trained knowledge and the instructions you provide. "Zero-shot" refers to zero training examples in the prompt — not zero instructions.

The quality of a zero-shot prompt depends almost entirely on **clarity of instruction**. The more precisely you describe the task, expected format, constraints, and context, the better the model performs without examples.

---

## Use Cases

- **Quick factual queries** where providing examples would be slower than just asking directly
- **Well-defined formatting tasks** where the output type is unambiguous (e.g., "write a subject line for this email")
- **Baseline testing** — zero-shot is the control condition when evaluating whether few-shot or chain-of-thought adds measurable value

---

## Weak Prompt

```
Write something about climate change.
```

**Why this fails:** The instruction is maximally ambiguous. The model has no guidance on format (paragraph? list? essay?), audience (children? scientists? policymakers?), length, tone, or specific angle. The output will be generic and safe — because generic and safe is the only rational response to a vague request.

### Weak Prompt Output (Gemini)

> Climate change is one of the most pressing issues facing our planet today. Rising temperatures, caused primarily by human activities such as burning fossil fuels and deforestation, are leading to more frequent and severe weather events, rising sea levels, and disruptions to ecosystems worldwide. Addressing climate change requires urgent action from governments, businesses, and individuals alike, including transitioning to renewable energy, reducing carbon emissions, and adapting to changes that are already underway.

**Assessment:** Technically accurate. Completely generic. Suitable for no specific purpose.

---

## Improved Prompt

```
Write a 3-sentence explanation of climate change for a Year 8 science class.
Use simple vocabulary. End with one concrete action students can take this week.
```

**What changed:** Added audience (Year 8), length constraint (3 sentences), vocabulary guidance (simple), and a specific structural requirement (end with an action). Same zero-shot technique — just precise instruction.

### Improved Prompt Output (Gemini)

> Climate change is the long-term warming of Earth caused by extra greenhouse gases — like CO₂ from cars and factories — trapping heat in the atmosphere, similar to how a greenhouse keeps plants warm. This warming is making weather more extreme, melting ice caps, and raising sea levels, which threatens animals, plants, and communities around the world. This week, you can help by keeping track of how much energy your household uses and turning off lights and devices when you're not using them.

**Assessment:** Age-appropriate, structured, ends with the requested action. Same zero-shot technique, dramatically different result.

---

## Verdict

Zero-shot prompting works well when the task is inherently well-defined and your instructions are precise. The technique is often underestimated — many practitioners jump to few-shot when more careful zero-shot specification would have solved the problem without the overhead of writing examples.

---

## Common Pitfalls

**1. Confusing "zero-shot" with "minimal instruction"**
Zero-shot means no examples, not no guidance. Pack your prompt with constraints, format requirements, and context. The absence of examples should be compensated by precision of instruction.

**2. Using zero-shot for highly stylistic tasks**
If you need output that matches a very specific tone or format, zero-shot often falls short — the model has no reference point for your exact desired style. Use few-shot instead.

**3. Accepting the first output without iteration**
Zero-shot is fast but often produces a first draft, not a final one. Treat the initial output as a starting point for prompt refinement.
