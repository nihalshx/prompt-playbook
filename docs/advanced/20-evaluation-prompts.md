---
layout: default
title: "20 · Evaluation Prompts"
parent: Advanced Techniques
nav_order: 10
---

# Evaluation Prompts (LLM-as-Judge)
{: .no_toc }

**Tier:** Advanced · **Task types:** Quality assessment, A/B testing outputs, automated review · **Difficulty:** ⭐⭐⭐⭐☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Evaluation prompts use an LLM to **score, rank, or critique the outputs** of other LLM calls — or human-written content. The model acts as a judge rather than a generator. This enables automated quality assessment at scale, replacing or augmenting expensive human evaluation in content pipelines.

Well-designed evaluation prompts specify explicit criteria, provide a rubric, and request structured output for programmatic processing.

---

## Use Cases

- **A/B prompt testing** — automatically comparing which of two prompt variants produces better outputs across a test set
- **Content quality gates** — filtering LLM outputs below a quality threshold before they reach users
- **Dataset labelling** — using LLM judgements as a cost-effective alternative to human annotation for subjective quality tasks

---

## Weak Evaluation Prompt

```
Is this a good customer service response?

[Response text]
```

### Weak Output

> Yes, this is a good customer service response. It addresses the customer's concern and is written in a friendly tone.

**Assessment:** Binary, unexplained, non-actionable. Not useful for systematically improving outputs.

---

## Improved Evaluation Prompt

```
You are a customer service quality evaluator. Score the following response
on these four criteria, each scored 1–5:

1. **Resolution clarity** (1=vague, 5=specific next steps given)
2. **Tone appropriateness** (1=cold/defensive, 5=warm/professional)
3. **Accuracy** (1=contains errors or missing info, 5=factually complete)
4. **Conciseness** (1=excessive, 5=appropriately brief)

For each criterion: give the score, one sentence of justification, and one
specific improvement suggestion.

End with: TOTAL: [sum]/20 and an OVERALL_VERDICT of PASS (≥14) or FAIL (<14).

Response to evaluate:
---
Dear Customer, thank you for reaching out. We're sorry to hear about your
experience. Your case has been escalated to our team and someone will be in
touch. We appreciate your patience.
---
```

### Improved Output (Gemini)

> **1. Resolution clarity: 2/5**
> The response offers no specific timeline, no case number, and no indication of what "escalated to our team" means practically.
> *Improvement: Add a specific expected response timeframe (e.g., "within 2 business days") and a case reference number.*
>
> **2. Tone appropriateness: 4/5**
> Warm and professional; the apology is genuine and non-defensive.
> *Improvement: Personalise by using the customer's name if available.*
>
> **3. Accuracy: 3/5**
> No factual errors, but omits confirmation of what issue was received or what team it was escalated to.
> *Improvement: Briefly confirm the specific issue being escalated to show it was understood.*
>
> **4. Conciseness: 5/5**
> Appropriately brief without being dismissive.
> *Improvement: None needed.*
>
> **TOTAL: 14/20**
> **OVERALL_VERDICT: PASS**

**Assessment:** Structured, specific, actionable, and machine-parseable. The PASS/FAIL output enables automated routing.

---

## Verdict

LLM-as-judge evaluation prompts are one of the highest-leverage uses of LLMs in production systems — they enable quality measurement at a scale that human review cannot match. The main risk is model bias and inconsistency. Mitigate by: using explicit rubrics, requesting justification (not just scores), and periodically spot-checking against human judgements.

---

## Common Pitfalls

**1. No rubric — just asking "is this good?"**
Without a rubric, evaluation is vague, inconsistent, and not actionable. Define specific criteria with anchored descriptions for each score level.

**2. Position bias**
When comparing two outputs, models tend to prefer whichever appears first. Randomise order across evaluations, or use a pointwise scoring approach instead of pairwise comparison.

**3. Not validating against human judgements**
LLM evaluation correlates with human judgement but is not equivalent. For high-stakes quality gates, periodically audit LLM scores against human reviewers.
