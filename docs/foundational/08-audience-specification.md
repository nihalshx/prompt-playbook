---
layout: default
title: "08 · Audience Specification"
parent: Foundational Techniques
nav_order: 8
---

# Audience Specification
{: .no_toc }

**Tier:** Foundational · **Task types:** Educational content, documentation, communication · **Difficulty:** ⭐☆☆☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Audience specification tells the model **who will read the output** — their background, expertise level, age, role, or relationship to the topic. LLMs default to a generic, broadly-educated adult audience. Specifying your actual audience recalibrates vocabulary, assumed knowledge, depth, and tone automatically.

This technique requires almost no extra prompting effort and consistently improves output appropriateness.

---

## Use Cases

- **Educational content** — the same topic explained at primary school, undergraduate, and expert level requires dramatically different language
- **Internal vs. external communication** — documentation for engineers vs. documentation for end-users requires different jargon and assumed context
- **Persuasive writing** — knowing your audience (sceptical investors, enthusiastic early adopters, risk-averse regulators) shapes which arguments to lead with

---

## Weak Prompt

```
Explain what an API is.
```

### Weak Prompt Output (Gemini)

> An API, or Application Programming Interface, is a set of rules and protocols that allows different software applications to communicate with each other. It defines the methods and data formats that applications can use to request and exchange information...

**Assessment:** Technically accurate, aimed at a vague "somewhat technical" audience. Not right for a non-technical business user, not detailed enough for a developer.

---

## Improved Prompt

```
Explain what an API is to a non-technical marketing manager who has heard
the term in meetings and wants to understand what it means in plain English.
Use a real-world analogy. Maximum 100 words. No code, no technical jargon.
```

### Improved Prompt Output (Gemini)

> Think of an API like a waiter in a restaurant. You (an app) don't go into the kitchen (another app's data or service) yourself — you tell the waiter what you want, the waiter goes and gets it, and brings the result back to you. When your CRM automatically pulls in data from your email platform, an API is the waiter making that happen. It's simply a standardised way for software to talk to other software — you don't need to know how it works under the hood, just that it does.

**Assessment:** Appropriate analogy, business-context example, zero jargon, within word limit.

---

## Verdict

Audience specification is one of the highest ROI prompt additions — one short phrase ("explain this to a [person] who [context]") dramatically shifts vocabulary and depth. It's most impactful when the audience differs significantly from the model's default assumption (technically literate, anglophone adult). Never omit it when you know who will read the output.

---

## Common Pitfalls

**1. Specifying audience but not purpose**
"Explain X to a manager" is better than nothing, but "explain X to a manager who needs to decide whether to approve budget for it" gives the model both audience and task framing.

**2. Underestimating the model's defaults**
Without audience specification, the model aims for a broadly-educated adult — which may be fine for many tasks. Only specify audience when your actual reader differs meaningfully from this default.

**3. Conflicting audience and instruction signals**
"Explain this simply to a 10-year-old using advanced technical terminology" creates contradictory constraints. Ensure audience specification and other instructions are mutually consistent.
