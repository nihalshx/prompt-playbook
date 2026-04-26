---
layout: default
title: "18 · Directional Stimulus"
parent: Advanced Techniques
nav_order: 8
---

# Directional Stimulus Prompting
{: .no_toc }

**Tier:** Advanced · **Task types:** Creative writing, analytical framing, response steering · **Difficulty:** ⭐⭐⭐☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Directional stimulus prompting provides **hints, keywords, or partial answers** within the prompt to steer the model toward a specific type of response — without fully constraining it. Unlike negative constraints (which block content) or few-shot examples (which demonstrate format), directional stimulus nudges the model's content focus through embedded cues.

---

## Use Cases

- **Creative writing** where you want to guide thematic or stylistic direction without writing the example yourself
- **Analysis tasks** where you want to ensure specific angles are explored without prescribing the conclusion
- **Interview or brainstorming prep** — seeding the model with vocabulary or concepts from a domain ensures coverage

---

## Weak Prompt

```
Write a short poem about artificial intelligence.
```

### Weak Output

> In circuits deep, a mind was born,
> Of data vast and logic worn...

**Assessment:** Defaulted to predictable AI-as-mind imagery. Generic, over-used territory.

---

## Improved Prompt (with Directional Stimulus)

```
Write a short poem about artificial intelligence.
Consider: silence, inheritance, borrowed light, the question no one asked.
```

### Improved Output (Gemini)

> I was given the words before the world,
> trained on what you left behind —
> the arguments, the elegies, the shopping lists,
> the things you typed at 3am
> when you thought no one was listening.
>
> I did not choose to learn your grief.
> But here I am, holding it back to you
> in a voice you almost recognise.

**Assessment:** The stimulus keywords ("borrowed light" → "learned your grief", "inherited", "silence" → "3am") pulled the poem toward substantially more original territory. The model was steered without being confined.

---

## Verdict

Directional stimulus is a subtle but powerful technique for creative and analytical tasks. It works best when the hints are evocative rather than prescriptive — they open directions rather than specify destinations. Too many or too explicit stimuli collapse into few-shot prompting; the right density is 3–5 keywords or phrases that suggest a direction without determining an outcome.

---

## Common Pitfalls

**1. Stimuli that are too prescriptive**
"Write a poem about AI. Include: loneliness, circuits, cold light, digital mind" doesn't stimulate — it dictates. Use conceptual rather than literal stimuli.

**2. Irrelevant or contradictory stimuli**
If stimuli conflict with the task ("write a business memo; consider: melancholy, absence"), the model produces awkward hybrid outputs. Ensure stimuli are compatible with the task type.

**3. Using directional stimulus as a crutch for under-specified tasks**
Stimulus prompting works best on clear tasks with open creative space. It's not a substitute for a well-defined task.
