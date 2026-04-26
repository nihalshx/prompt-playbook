---
layout: default
title: "15 · Least-to-Most Decomposition"
parent: Advanced Techniques
nav_order: 5
---

# Least-to-Most Decomposition
{: .no_toc }

**Tier:** Advanced · **Task types:** Complex problem-solving, curriculum design, layered explanations · **Difficulty:** ⭐⭐⭐☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Least-to-most decomposition breaks a hard problem into **sub-problems ordered from simplest to most complex**, solving each in turn and using earlier solutions to build toward the final answer. Unlike prompt chaining (which sequences independent steps), least-to-most explicitly builds on previous solutions — each step's answer is a prerequisite for the next.

---

## Use Cases

- **Mathematical problem solving** where simpler component calculations must precede the final computation
- **Curriculum and tutorial design** — sequencing learning from foundational to advanced concepts
- **Legal and policy analysis** — resolving simpler sub-questions before addressing the complex central question

---

## Weak Prompt

```
Is it legal for an employer to monitor employee emails on company devices
in the UK without telling them?
```

### Weak Output

> The legality depends on several factors including the employer's monitoring policy, GDPR requirements, and whether employees have been informed...

**Assessment:** Correct but shallow. The model surface-skims without resolving the component legal questions that the answer depends on.

---

## Improved Prompt (Least-to-Most)

```
Answer this legal question using least-to-most decomposition.
First identify the sub-questions that must be answered, solve the simplest
ones first, then use those answers to address the full question.

Question: Is it legal for an employer to monitor employee emails on company
devices in the UK without telling them?
```

### Improved Output (Gemini)

> **Sub-question 1 (simplest): Does GDPR apply to employee data monitoring in the UK?**
> Yes. Post-Brexit UK GDPR retains the same core principles as EU GDPR. Employee email data is personal data and subject to its requirements.
>
> **Sub-question 2: What does UK GDPR require before processing personal data?**
> A lawful basis. For employee monitoring, employers typically rely on "legitimate interests" — but this requires a balancing test showing that monitoring is proportionate and necessary.
>
> **Sub-question 3: Does the Investigatory Powers Act or RIPA apply?**
> RIPA 2000 makes it unlawful to intercept communications in transit without consent or a lawful authorisation. Stored email review is less clear-cut but still subject to data protection law.
>
> **Full Question: Is covert email monitoring legal?**
> No — not without telling employees. The ICO's Employment Practices Code requires employers to inform employees about monitoring in a privacy notice. Covert monitoring may breach UK GDPR's transparency principle and RIPA. Legal monitoring requires: a documented policy, a legitimate business purpose, and advance employee notification. Silent monitoring on company devices is not lawful in standard circumstances.

**Assessment:** Each sub-question answer is used to build the final conclusion. The reasoning is transparent and verifiable.

---

## Verdict

Least-to-most decomposition is highly effective for questions that appear to have a single answer but actually require resolving several prerequisite questions first. It makes the model's reasoning transparent and significantly reduces the risk of a confidently-stated but incomplete answer.

---

## Common Pitfalls

**1. Wrong ordering of sub-problems**
If you order sub-problems incorrectly, later steps lose the benefit of earlier foundations. Ask the model to identify the ordering itself, then verify it makes logical sense.

**2. Overusing for simple questions**
A factual lookup does not need decomposition. Use least-to-most for questions where you can identify genuine prerequisite sub-problems.

**3. Not referencing earlier answers in later steps**
Each step must explicitly build on previous answers. If the model re-derives from scratch each time, the decomposition isn't working as intended.
