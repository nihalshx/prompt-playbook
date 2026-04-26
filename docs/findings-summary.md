---
layout: default
title: Findings Summary
nav_order: 4
permalink: docs/findings-summary
---

# Findings Summary
{: .no_toc }

Evidence-based observations from testing all 20 techniques across four task types.
{: .fs-5 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Testing Methodology

All 20 techniques were tested using the Google Gemini API (`gemini-1.5-flash`, temperature 0.7 unless otherwise noted) across four standardised task types:

| Task Type | Description | Example Tasks |
|---|---|---|
| **Summarisation** | Condensing documents to key points | News articles, research papers, reports |
| **Factual Q&A** | Answering specific knowledge questions | Domain facts, calculations, definitions |
| **Creative Writing** | Generating original content | Poems, product copy, narrative writing |
| **Reasoning** | Multi-step logic, analysis, decisions | Word problems, argument analysis, trade-off evaluation |

Each technique was evaluated on: output quality improvement over an unstructured baseline, consistency across 3 runs, token efficiency, and ease of implementation.

---

## Key Finding 1: Format-Constrained Prompts Consistently Outperform Open-Ended Equivalents

Across all four task types, prompts that specified **explicit output format requirements** (length, structure, field names, number of items) produced outputs that were more directly usable without editing.

This held across:
- Summarisation: "3 bullet points, max 15 words each" vs. "summarise this"
- Structured output: JSON schema specification vs. "extract the key info"
- Creative writing: "60–80 words, no exclamation marks, no superlatives" vs. "write a product description"

**Practical implication:** Always specify format explicitly. Even if the content instruction is strong, an underspecified format produces outputs that require manual reformatting.

---

## Key Finding 2: Chain-of-Thought Shows the Largest Accuracy Delta on Reasoning Tasks

On word problems and multi-step logic tasks, chain-of-thought prompting reduced error rates significantly compared to direct-answer prompting. The effect was largest on problems with:

- Multiple arithmetic operations in sequence
- Distractors (irrelevant information inserted in the problem)
- Conditional logic branches

**When CoT failed:** On simple, single-step calculations, CoT added verbosity without accuracy benefit. On tasks where the model was fundamentally incorrect about domain facts (e.g., a false premise in the problem), CoT produced elaborate incorrect reasoning chains.

---

## Key Finding 3: Few-Shot Is the Most Reliable Format Enforcement Mechanism

When output format consistency across many runs was the primary requirement, few-shot prompting outperformed explicit format instructions alone. Showing the model 2–3 examples of the exact output structure produced more consistent adherence than describing the structure in words.

**Exception:** When format is extremely simple (single-word responses, yes/no, uppercase labels), explicit instruction is sufficient and few-shot adds unnecessary context overhead.

---

## Key Finding 4: Persona Prompting Shifts Register More Than Knowledge

Role-play / persona prompting reliably changed the register, vocabulary, and assumed audience of responses. However, it did **not** reliably add domain knowledge the model didn't already have. A "medical doctor" persona used correct medical vocabulary but was not more accurate on clinical specifics than a non-persona prompt.

**Practical implication:** Use persona for tone and register. Use context injection for domain-specific accuracy.

---

## Key Finding 5: Advanced Techniques Have Higher Variance

The ten advanced techniques showed higher variance in output quality than foundational techniques — meaning they had higher ceilings but also more failure modes. The techniques most prone to inconsistency were:

- **ReAct** (without real tool integration, observations were hallucinated)
- **Self-consistency** (consensus was sometimes consensus on the wrong answer)
- **Meta-prompting** (generated prompts were plausible but not always superior)

**Practical implication:** Establish a solid foundational-technique baseline before applying advanced methods. Advanced techniques add complexity — only adopt them if foundational approaches are genuinely insufficient.

---

## Technique Effectiveness Matrix

| Technique | Summarisation | Factual Q&A | Creative Writing | Reasoning |
|---|---|---|---|---|
| Zero-Shot | ★★★☆☆ | ★★★☆☆ | ★★☆☆☆ | ★★☆☆☆ |
| Few-Shot | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★☆☆ |
| Chain-of-Thought | ★★★☆☆ | ★★★☆☆ | ★☆☆☆☆ | ★★★★★ |
| Role-Play | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★★☆☆ |
| Structured Output | ★★★★★ | ★★★★☆ | ★★☆☆☆ | ★★★☆☆ |
| Negative Constraints | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★☆☆☆ |
| Context Injection | ★★★★★ | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Audience Specification | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★☆☆ |
| Tone Control | ★★☆☆☆ | ★☆☆☆☆ | ★★★★★ | ★☆☆☆☆ |
| Instruction Clarity | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Self-Consistency | ★★☆☆☆ | ★★★☆☆ | ★☆☆☆☆ | ★★★★★ |
| ReAct | ★★☆☆☆ | ★★★★☆ | ★☆☆☆☆ | ★★★★☆ |
| Step-Back | ★★★☆☆ | ★★★★☆ | ★★☆☆☆ | ★★★★★ |
| Prompt Chaining | ★★★★★ | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| Least-to-Most | ★★★☆☆ | ★★★★☆ | ★☆☆☆☆ | ★★★★★ |
| Generated Knowledge | ★★★★☆ | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Calibration Prompts | ★★☆☆☆ | ★★★★★ | ★☆☆☆☆ | ★★★☆☆ |
| Directional Stimulus | ★★☆☆☆ | ★☆☆☆☆ | ★★★★★ | ★★☆☆☆ |
| Meta-Prompting | ★★★☆☆ | ★★☆☆☆ | ★★★☆☆ | ★★★☆☆ |
| Evaluation Prompts | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★★☆ |

*★★★★★ = Highly effective · ★☆☆☆☆ = Limited applicability*

---

## Recommended Technique Stacks by Task Type

### For Summarisation
1. **Instruction clarity** (be explicit: length, format, what to preserve)
2. **Structured output** (define the exact fields or structure)
3. **Audience specification** (who will read this summary?)
4. **Negative constraints** (exclude: opinions, caveats, filler)
5. **Prompt chaining** for long/complex documents

### For Factual Q&A
1. **Context injection** (provide the source document or data)
2. **Generated knowledge** (prime with domain context first)
3. **Calibration prompts** (surface uncertainty on high-stakes answers)
4. **Step-back** for complex multi-condition questions
5. **Least-to-most** for questions with prerequisite sub-questions

### For Creative Writing
1. **Tone control** (specific, anchored tone specification)
2. **Audience specification** (who is reading this?)
3. **Directional stimulus** (evocative keywords to steer direction)
4. **Negative constraints** (no clichés, no specific words)
5. **Few-shot** for highly specific stylistic requirements
6. **Prompt chaining** for long-form pieces

### For Reasoning
1. **Chain-of-thought** (mandatory for multi-step problems)
2. **Instruction clarity** (unambiguous problem statement)
3. **Least-to-most** for prerequisite-dependent problems
4. **Self-consistency** for high-stakes answers
5. **Step-back** for problems requiring first-principles thinking

---

## Overarching Conclusions

**1. Specificity is the highest-ROI investment in prompting.**
The single most impactful change across all 20 techniques was moving from vague to specific instructions. Before reaching for advanced techniques, ask whether the basic prompt is as specific as it could be.

**2. Combination outperforms any single technique.**
The strongest outputs consistently came from stacking compatible techniques — e.g., role-play + structured output + negative constraints, or few-shot + chain-of-thought. Techniques are not mutually exclusive.

**3. Failure modes are as important as success modes.**
Every technique documented in this playbook has conditions under which it performs poorly. Understanding failure modes — not just best-case performance — is what separates practitioners from experimenters.

**4. Test on your actual tasks, not abstract benchmarks.**
Technique effectiveness varies significantly by task, model, and domain. The ratings in this playbook reflect testing on a specific set of tasks. Your mileage will vary — treat these ratings as hypotheses to test, not universal rankings.
