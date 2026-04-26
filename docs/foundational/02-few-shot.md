---
layout: default
title: "02 · Few-Shot Prompting"
parent: Foundational Techniques
nav_order: 2
---

# Few-Shot Prompting
{: .no_toc }

**Tier:** Foundational · **Task types:** Pattern-matching, formatting, classification · **Difficulty:** ⭐⭐☆☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Few-shot prompting provides **2–5 worked examples** within the prompt before presenting the actual task. Each example shows the model the input–output pattern you want it to replicate. The model uses these examples as an in-context demonstration of what success looks like — without any weight updates or fine-tuning.

Few-shot is the single most reliable technique for **enforcing consistent output format**, because you show rather than describe the pattern.

---

## Use Cases

- **Classification tasks** where you want outputs restricted to specific labels (e.g., sentiment: positive / negative / neutral)
- **Reformatting content** where the exact input–output transformation is best demonstrated, not described
- **Stylistic consistency** when you need many outputs to share the same tone, structure, or vocabulary as a reference

---

## Weak Prompt

```
Label these customer reviews as positive, negative, or neutral.

Review: "The packaging was damaged but the product itself works fine."
```

**Why this fails:** Without examples, the model must guess the classification criteria. Is "damaged packaging but working product" positive (product works), negative (damaged), or neutral (mixed)? Ambiguous boundary cases produce inconsistent results at scale.

### Weak Prompt Output (Gemini)

> Neutral. The review mentions a negative aspect (damaged packaging) and a positive aspect (working product), resulting in an overall neutral sentiment.

---

## Improved Prompt

```
Label each customer review as POSITIVE, NEGATIVE, or NEUTRAL.
Use only these three labels — no explanations.

Examples:
Review: "Arrived quickly and exactly as described." → POSITIVE
Review: "Stopped working after two days. Very disappointed." → NEGATIVE
Review: "It's okay. Nothing special but does the job." → NEUTRAL

Now label this review:
Review: "The packaging was damaged but the product itself works fine."
```

**What changed:** Three examples establish the label format (uppercase, no explanation), the classification boundary, and the response style. The model now has reference cases for both mixed signals and clear signals.

### Improved Prompt Output (Gemini)

> NEUTRAL

**Assessment:** Consistent with the examples. No unsolicited explanation. Replicable at scale across hundreds of reviews.

---

## Verdict

Few-shot prompting is the most reliable technique for format consistency and boundary-case classification. The overhead of writing 2–3 good examples is almost always worth it when you need repeatable, parseable outputs. Its weakness is example selection — poor examples teach the wrong pattern just as effectively as good ones teach the right one.

---

## Common Pitfalls

**1. Using too many examples**
More than 5–6 examples in a prompt rarely improves performance and often wastes context. Prioritise diversity of examples over quantity — ensure your examples cover the important edge cases, not just the easy ones.

**2. Using unrepresentative examples**
If all your examples are clear-cut positives and negatives, the model has no reference for genuinely ambiguous cases. Deliberately include boundary examples.

**3. Inconsistent example formatting**
If some examples have explanations and some don't, the model will inconsistently include or omit explanations. Every example must demonstrate exactly the output format you want.
