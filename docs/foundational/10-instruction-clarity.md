---
layout: default
title: "10 · Instruction Clarity"
parent: Foundational Techniques
nav_order: 10
---

# Instruction Clarity
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

Instruction clarity is the practice of writing prompts that are **specific, unambiguous, and complete** — eliminating vague verbs, underspecified targets, and implicit assumptions. It is less a discrete technique and more a foundational discipline: the quality ceiling of any other technique is set by the clarity of its instructions.

The test for instruction clarity: could two different people read your prompt and produce the same output? If not, the model will make arbitrary choices to fill the gaps.

---

## Use Cases

- **Repeatable task pipelines** — when the same prompt will run on hundreds of inputs, ambiguity compounds across every result
- **Multi-step instructions** — decomposing complex tasks into clearly ordered, numbered steps prevents the model from re-ordering or conflating steps
- **Cross-team prompts** — when prompts are shared between team members, clarity prevents "it works differently for me" problems

---

## Weak Prompt

```
Make this email better.

[Original email pasted here]
```

### Weak Prompt Output (Gemini)

> *[Rewrite with minor phrasing improvements and a slightly warmer closing]*

**Assessment:** "Better" is undefined. The model made conservative style edits. The user may have wanted structural changes, tone shifts, length reduction, or a complete rewrite — the model had no way to know.

---

## Improved Prompt

```
Rewrite the following email to achieve these specific goals:
1. Reduce length by approximately 40% — cut filler sentences
2. Make the ask in paragraph 3 explicit and move it to the opening
3. Adopt a direct, professional tone — remove hedge phrases like "I just wanted to" and "sorry to bother you"
4. Keep all factual details unchanged

Return only the rewritten email. Do not explain what you changed.

[Original email pasted here]
```

### Improved Prompt Output (Gemini)

> *[Rewrite that leads with the ask, is measurably shorter, removes hedging language, and preserves factual content]*

**Assessment:** Every instruction is unambiguous and independently verifiable. The model has a clear quality target for each dimension.

---

## Verdict

Instruction clarity underlies the effectiveness of every other technique in this playbook. Before reaching for chain-of-thought or few-shot examples, check whether the basic instruction is specific enough. Most prompt failures are instruction clarity failures in disguise — the model chose an interpretation you didn't intend.

---

## Common Pitfalls

**1. Using vague evaluation verbs**
"Improve", "enhance", "fix", "make better" are all undefined. Replace with: "reduce to 200 words", "remove passive voice", "add a call-to-action in the last sentence."

**2. Implicit assumptions about format**
If you want bullet points, say so. If you want a single paragraph, say so. The model's default format choice may not match your expectation.

**3. Burying the most important instruction**
Models attend more strongly to instructions at the beginning and end of prompts. Put your most critical requirements first, not last.
