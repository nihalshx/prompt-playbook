---
layout: default
title: "03 · Chain-of-Thought"
parent: Foundational Techniques
nav_order: 3
---

# Chain-of-Thought Prompting
{: .no_toc }

**Tier:** Foundational · **Task types:** Reasoning, maths, logic, multi-step analysis · **Difficulty:** ⭐⭐☆☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Chain-of-thought (CoT) prompting instructs the model to **reason through a problem step by step before giving the final answer**. Instead of jumping to a conclusion, the model externalises its reasoning process, which makes errors visible and correctable — and dramatically improves accuracy on tasks that require multi-step logic.

The simplest CoT trigger is appending *"Think step by step"* to your prompt. More powerful versions provide an example of step-by-step reasoning (few-shot CoT).

---

## Use Cases

- **Mathematical word problems** where intermediate calculation steps are needed for accuracy
- **Multi-condition logic** — decisions that depend on several factors being weighed in sequence
- **Argument analysis** — identifying premises, assumptions, and conclusions in complex texts

---

## Weak Prompt

```
A store sells apples for £0.40 each and oranges for £0.65 each.
Sarah buys 7 apples and 4 oranges. She pays with a £10 note.
How much change does she receive?
```

### Weak Prompt Output (Gemini)

> Sarah receives £3.60 in change.

**Assessment:** Wrong. (Correct answer: £10 − (7×£0.40 + 4×£0.65) = £10 − (£2.80 + £2.60) = £10 − £5.40 = **£4.60**.) The model jumped to an answer without showing its working.

---

## Improved Prompt

```
A store sells apples for £0.40 each and oranges for £0.65 each.
Sarah buys 7 apples and 4 oranges. She pays with a £10 note.
How much change does she receive?

Think through this step by step before giving the final answer.
```

### Improved Prompt Output (Gemini)

> **Step 1:** Calculate the cost of apples: 7 × £0.40 = £2.80
>
> **Step 2:** Calculate the cost of oranges: 4 × £0.65 = £2.60
>
> **Step 3:** Calculate the total cost: £2.80 + £2.60 = £5.40
>
> **Step 4:** Calculate the change: £10.00 − £5.40 = **£4.60**
>
> Sarah receives **£4.60** in change.

**Assessment:** Correct, clearly reasoned, auditable. The step-by-step format also makes it easy to spot where an error would occur if the numbers were changed.

---

## Verdict

Chain-of-thought is one of the highest-impact techniques for reasoning tasks — the improvement in accuracy is consistent and significant. The trade-off is output length: CoT responses are longer and may require post-processing to extract the final answer if parsing programmatically.

---

## Common Pitfalls

**1. Applying CoT to simple tasks**
"Think step by step" on a basic factual lookup adds verbosity without benefit. Reserve CoT for genuinely multi-step problems.

**2. Trusting the reasoning but not verifying the answer**
CoT makes errors visible, but the model can reason convincingly toward a wrong conclusion. Always verify final answers on high-stakes tasks.

**3. Not extracting the answer cleanly**
If you're parsing CoT output programmatically, add an explicit instruction like *"End your response with: ANSWER: [value]"* to make extraction reliable.
