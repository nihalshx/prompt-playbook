---
layout: home
title: Home
nav_order: 1
description: "A practitioner-oriented prompt engineering reference — 20 techniques with real LLM test results, honest verdicts, and documented failure modes."
permalink: /
---

# Prompt Engineering Playbook
{: .fs-9 }

A structured reference covering **20 prompt engineering techniques** — each documented with original before-and-after examples, real Google Gemini API outputs, personal verdicts, and common failure modes.
{: .fs-6 .fw-300 }

[Browse Foundational Techniques](#foundational-techniques){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Browse Advanced Techniques](#advanced-techniques){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## What Is This?

The **Prompt Engineering Playbook** is a practitioner-first reference that treats prompt engineering as a craft — something learned through empirical testing, not memorising technique names.

Every page follows a consistent **seven-section template**:

| Section | Content |
|---|---|
| **Definition** | Plain-English explanation of the technique |
| **Use Cases** | Three practical scenarios where the technique applies |
| **Weak Prompt** | An example prompt that underperforms, and why |
| **Improved Prompt** | The same task rewritten using the technique |
| **LLM Outputs** | Actual Gemini API responses — side by side |
| **Verdict** | Honest two-sentence assessment based on testing |
| **Pitfalls** | Common mistakes and how to avoid them |

---

## Foundational Techniques

The ten foundational techniques every AI practitioner should know.

| # | Technique | Best For |
|---|---|---|
| 1 | [Zero-Shot Prompting](docs/foundational/01-zero-shot) | Quick tasks, general queries |
| 2 | [Few-Shot Prompting](docs/foundational/02-few-shot) | Pattern-matching, formatting tasks |
| 3 | [Chain-of-Thought](docs/foundational/03-chain-of-thought) | Reasoning, maths, multi-step problems |
| 4 | [Role-Play / Persona](docs/foundational/04-role-play) | Expert tone, domain framing |
| 5 | [Structured Output](docs/foundational/05-structured-output) | JSON, tables, parseable responses |
| 6 | [Negative Constraints](docs/foundational/06-negative-constraints) | Scoping, avoiding unwanted content |
| 7 | [Context Injection](docs/foundational/07-context-injection) | Grounding LLM in specific facts |
| 8 | [Audience Specification](docs/foundational/08-audience-specification) | Calibrating reading level & depth |
| 9 | [Tone Control](docs/foundational/09-tone-control) | Formal, casual, persuasive writing |
| 10 | [Instruction Clarity](docs/foundational/10-instruction-clarity) | Reducing ambiguity in any task |

---

## Advanced Techniques

Ten advanced techniques for complex, multi-step, and high-stakes tasks.

| # | Technique | Best For |
|---|---|---|
| 11 | [Self-Consistency](docs/advanced/11-self-consistency) | Improving accuracy on reasoning tasks |
| 12 | [ReAct Prompting](docs/advanced/12-react-prompting) | Agentic tasks, tool-use framing |
| 13 | [Step-Back Prompting](docs/advanced/13-step-back) | Abstract reasoning, first principles |
| 14 | [Prompt Chaining](docs/advanced/14-prompt-chaining) | Long, multi-stage workflows |
| 15 | [Least-to-Most Decomposition](docs/advanced/15-least-to-most) | Complex problems, sub-task breakdown |
| 16 | [Generated Knowledge](docs/advanced/16-generated-knowledge) | Factual accuracy, context priming |
| 17 | [Calibration Prompts](docs/advanced/17-calibration-prompts) | Uncertainty, confidence estimation |
| 18 | [Directional Stimulus](docs/advanced/18-directional-stimulus) | Steering creative or analytical tone |
| 19 | [Meta-Prompting](docs/advanced/19-meta-prompting) | Prompt generation, self-improvement |
| 20 | [Evaluation Prompts](docs/advanced/20-evaluation-prompts) | LLM-as-judge, quality assessment |

---

## Findings Summary

After testing all 20 techniques across four task types (summarisation, factual Q&A, creative writing, and reasoning), key patterns emerged.

[Read the Findings Summary →](docs/findings-summary){: .btn .btn-outline }

---

## Tech Stack

- **Site**: GitHub Pages with [Just the Docs](https://just-the-docs.com/) Jekyll theme
- **LLM Testing**: Google Gemini API (`gemini-1.5-flash`)
- **Scripts**: Python 3.11+ with `google-generativeai` SDK
- **Prompts**: 40+ original weak/improved pairs across 4 task types

---

> **Note**: All LLM outputs shown in this playbook were generated during hands-on testing. Results may vary with different models, temperatures, or dates. Treat verdicts as empirically-grounded opinions, not universal truths.
