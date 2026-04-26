---
layout: default
title: "11 · Self-Consistency"
parent: Advanced Techniques
nav_order: 1
---

# Self-Consistency
{: .no_toc }

**Tier:** Advanced · **Task types:** Reasoning, maths, classification · **Difficulty:** ⭐⭐⭐☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Self-consistency samples the model **multiple times on the same reasoning prompt** (using chain-of-thought) with a non-zero temperature, then selects the answer that appears most frequently across samples. Rather than trusting a single reasoning chain, it treats the LLM as a noisy reasoner and aggregates across paths — similar to a committee vote.

The technique requires multiple API calls but reliably outperforms single-sample CoT on complex reasoning tasks.

---

## Use Cases

- **High-stakes arithmetic or logic problems** where a single CoT may contain an error that goes undetected
- **Ambiguous classification tasks** where different reasoning paths may reach the same or different conclusions
- **Reliability benchmarking** — self-consistency is a proxy for confidence: high agreement = reliable answer

---

## Weak Prompt (Single CoT)

```
A train leaves City A at 09:00 travelling at 90 km/h toward City B.
Another train leaves City B at 10:00 travelling at 110 km/h toward City A.
The cities are 400 km apart. At what time do the trains meet? Think step by step.
```

*Run once → single answer with no reliability signal.*

---

## Improved Approach (Self-Consistency)

Run the same prompt 5 times at temperature 0.7. Collect answers:
- Run 1: 11:45
- Run 2: 11:45
- Run 3: 12:00
- Run 4: 11:45
- Run 5: 11:30

**Majority vote: 11:45** (3/5 runs agree)

**Verification:** Train A travels from 09:00. At meeting time T hours after 09:00, Train A has covered 90T km. Train B has travelled (T−1) hours covering 110(T−1) km. 90T + 110(T−1) = 400 → 200T = 510 → T = 2.55 hours → 09:00 + 2h33m = **11:33**. The majority answer (11:45) is still wrong — but the disagreement across runs signals low confidence and flags the need for verification.

---

## Verdict

Self-consistency is most valuable not for the answer it produces but for the **confidence signal** it provides. High agreement (5/5) on a difficult problem is a meaningful reliability indicator. Low agreement flags problems that need human verification or a different approach entirely. The cost is proportional to the number of samples.

---

## Common Pitfalls

**1. Using temperature 0 (deterministic)**
At temperature 0, every run produces the same output — making self-consistency pointless. Use 0.5–0.9 for meaningful variation.

**2. Treating majority vote as ground truth**
A majority wrong answer is still wrong. Use self-consistency as a confidence filter, not a correctness guarantee.

**3. High API cost on production workloads**
5× the API calls means 5× the cost. Reserve self-consistency for high-stakes, low-volume tasks — not bulk processing.
