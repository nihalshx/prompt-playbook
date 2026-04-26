---
layout: default
title: "19 · Meta-Prompting"
parent: Advanced Techniques
nav_order: 9
---

# Meta-Prompting
{: .no_toc }

**Tier:** Advanced · **Task types:** Prompt optimisation, prompt generation, system design · **Difficulty:** ⭐⭐⭐⭐☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Meta-prompting uses an LLM to **generate, critique, or improve prompts** — treating the prompt itself as the output to be produced. Rather than writing prompts manually, you describe what you want to achieve and ask the model to draft the prompt that would achieve it, or provide a weak prompt and ask the model to improve it.

Meta-prompting is recursive: a well-crafted meta-prompt produces better prompts, which produce better outputs.

---

## Use Cases

- **Rapid prompt prototyping** — describe a task and have the model draft 3 prompt variants to test
- **Prompt critique and improvement** — submit a prompt that's underperforming and ask the model to diagnose its weaknesses
- **Prompt templating** — generating a family of related prompts for similar tasks across a product

---

## Weak Meta-Prompt

```
Write me a good prompt for summarising articles.
```

### Weak Output

> Prompt: "Summarise this article in 3 bullet points covering the main points."

**Assessment:** Generic. No consideration of audience, length, format requirements, or the variation across article types.

---

## Improved Meta-Prompt

```
I need a high-quality prompt for an automated pipeline that summarises
news articles before sending them to busy executives. Requirements:
- Outputs should be 3–5 sentences maximum
- Must preserve key people, organisations, and numerical figures
- Should flag if the article is opinion vs. news reporting
- Tone should be neutral and factual
- Must work across articles from 200–5000 words

Write two prompt variants and explain the design choices behind each.
```

### Improved Output (Gemini)

> **Variant A — Instruction-heavy:**
> ```
> Summarise the following article in 3–5 sentences for an executive audience.
> Preserve all named people, organisations, and specific numerical figures.
> If this article is opinion or editorial rather than news reporting, begin
> your summary with [OPINION]. Use factual, neutral language. Do not add
> commentary or context beyond what is in the article.
>
> Article: {article_text}
> ```
> *Design rationale: Explicit constraints reduce hallucination risk. The [OPINION] flag handles mixed article types systematically.*
>
> **Variant B — Role + instruction:**
> ```
> You are an executive briefing assistant. Read the following article and
> produce a neutral 3–5 sentence summary that preserves key people, organisations,
> and numerical data exactly as stated. Label opinion pieces [OPINION] before
> the summary. No added commentary.
>
> Article: {article_text}
> ```
> *Design rationale: Role framing activates a professional briefing register. Slightly shorter instruction set, similar constraint enforcement.*

**Assessment:** Two testable variants with explicit design rationale. Far more useful than the single generic prompt the weak meta-prompt produced.

---

## Verdict

Meta-prompting significantly accelerates prompt development by leveraging the model's understanding of prompting principles. The strongest use case is critique and improvement — submitting an underperforming prompt and asking "what's wrong with this and how would you fix it?" often surfaces issues that aren't obvious to the prompt author.

---

## Common Pitfalls

**1. Trusting meta-generated prompts without testing**
Meta-prompting produces plausible-looking prompts that may not actually perform better. Always test generated prompts against real inputs.

**2. Underspecifying the use case**
"Write me a summarisation prompt" is too vague. Describe your specific pipeline, audience, and requirements — the model can only design for the constraints you provide.

**3. Not asking for rationale**
"Write a prompt" produces a prompt. "Write a prompt and explain every design decision" produces a prompt you can understand, evaluate, and modify intelligently.
