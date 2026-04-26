---
layout: default
title: "17 · Calibration Prompts"
parent: Advanced Techniques
nav_order: 7
---

# Calibration Prompts
{: .no_toc }

**Tier:** Advanced · **Task types:** Uncertainty quantification, high-stakes decisions, knowledge auditing · **Difficulty:** ⭐⭐⭐☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Calibration prompts elicit the model's **explicit confidence estimate** alongside an answer, or ask the model to flag where it might be wrong. LLMs default to confidently-stated answers regardless of actual reliability. Calibration prompts counteract this by making uncertainty a first-class output.

Well-calibrated models — and well-calibrated prompts — express appropriate uncertainty on uncertain claims and appropriate confidence on reliable ones.

---

## Use Cases

- **Medical, legal, or financial questions** where knowing the reliability of an answer matters as much as the answer itself
- **Knowledge auditing** — systematically identifying where a model is confident vs. uncertain on a given domain
- **Human-in-the-loop systems** — routing uncertain answers to human review, confident answers to automated processing

---

## Weak Prompt

```
What is the lethal dose of acetaminophen in adults?
```

### Weak Output

> The toxic dose of acetaminophen in adults is generally considered to be above 7.5–10 grams in a single dose, with doses above 150 mg/kg potentially causing severe liver damage...

**Assessment:** Stated with high confidence. No indication of which parts of this are well-established vs. approximate, or when to seek clinical guidance.

---

## Improved Prompt

```
What is the lethal dose of acetaminophen in adults?

After your answer, rate your confidence on a scale of 1–5 and identify any
parts of your answer that a medical professional should verify or that vary
significantly by individual factors (weight, liver function, alcohol use, etc.).
```

### Improved Output (Gemini)

> Acetaminophen toxicity in adults typically begins with hepatotoxicity at single doses above approximately 7.5–10g (150 mg/kg), though this varies substantially by individual. Doses above 15–25g are associated with severe liver failure and potentially death. However, chronic alcoholics and those with liver disease may experience toxicity at substantially lower doses.
>
> **Confidence: 3/5.** The specific thresholds I've cited are approximate and drawn from general pharmacology training data. Key areas to verify with a medical professional: (1) current UK/US clinical guidelines for overdose assessment (these use the Rumack-Matthew nomogram which I have simplified), (2) individual risk factor adjustments, (3) management thresholds for activated charcoal and N-acetylcysteine treatment.

**Assessment:** The confidence rating and specific uncertainty flags are more useful than a confident-sounding answer that the reader might over-trust.

---

## Verdict

Calibration prompts partially counteract the LLM tendency toward overconfident assertion. They don't make models actually calibrated (they can still be confidently wrong), but they surface the model's own uncertainty signals, which correlate with actual reliability better than no uncertainty expression at all. Highly recommended for any domain where overconfidence causes real harm.

---

## Common Pitfalls

**1. Treating confidence ratings as accurate**
A self-rated "5/5" is not ground truth. Calibration prompts surface expressed uncertainty, not actual reliability.

**2. Not acting on the uncertainty signal**
If the model flags "verify with a professional" and you don't, calibration prompting provided no practical benefit. Build the verification step into your workflow.

**3. Using arbitrary scales**
Define what your scale means. "5 = I would stake my professional reputation on this claim" is more useful than just "5 = very confident."
