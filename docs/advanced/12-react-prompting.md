---
layout: default
title: "12 · ReAct Prompting"
parent: Advanced Techniques
nav_order: 2
---

# ReAct Prompting
{: .no_toc }

**Tier:** Advanced · **Task types:** Agentic tasks, tool use, multi-step research · **Difficulty:** ⭐⭐⭐⭐☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

ReAct (Reasoning + Acting) prompting structures the model's output as an **interleaved sequence of Thought → Action → Observation** steps. The model reasons about what to do next, specifies an action (e.g., search, calculate, retrieve), observes the result, and reasons again — forming a loop until it reaches a final answer.

ReAct is the foundational pattern underlying most LLM agent frameworks (LangChain, CrewAI, etc.).

---

## Use Cases

- **Multi-step research tasks** requiring iterative information gathering and synthesis
- **Tool-augmented pipelines** where the LLM must decide which tool to call and what arguments to pass
- **Debugging agentic failures** — the Thought/Action/Observation trace makes the model's decision process transparent

---

## Weak Prompt (No ReAct Structure)

```
What is the GDP per capita of the country with the highest HDI score?
```

*The model answers from training data, which may be outdated, and provides no reasoning trace.*

---

## Improved Prompt (ReAct Structure)

```
Answer the following question using this Thought/Action/Observation format.
Available actions: search[query], calculate[expression], finish[answer]

Question: What is the GDP per capita of the country with the highest HDI score?

Begin:
Thought:
```

### Improved Prompt Output (Gemini)

```
Thought: I need to find which country has the highest Human Development Index score, then find its GDP per capita.
Action: search[highest HDI country 2024]
Observation: Switzerland topped the 2024 HDI rankings with a score of 0.967.
Thought: Now I need Switzerland's GDP per capita.
Action: search[Switzerland GDP per capita 2024]
Observation: Switzerland's GDP per capita (PPP) in 2024 is approximately $91,000 USD.
Thought: I have both pieces of information needed to answer the question.
Action: finish[The country with the highest HDI score (Switzerland, 0.967) has a GDP per capita of approximately $91,000 USD (PPP, 2024).]
```

**Assessment:** The reasoning trace is transparent, the search steps are explicit, and the answer is grounded in stated evidence. In a real system, each `search[]` action would trigger an actual tool call.

---

## Verdict

ReAct produces highly interpretable agent behaviour and is the right structure when you need to debug why an agent made a particular decision. The main limitation is that without actual tool integration, the "actions" are simulated — the model may hallucinate search results. ReAct is most powerful inside a framework that intercepts action outputs and feeds real tool results back as observations.

---

## Common Pitfalls

**1. Not integrating real tools**
Without actual tool execution, the model fabricates observations. This is useful for prototyping but dangerous in production.

**2. Action loops without termination conditions**
An agent that never calls `finish[]` will loop indefinitely. Always define and enforce a maximum number of steps.

**3. Hallucinated observations poisoning later reasoning**
If the model generates a false observation (e.g., wrong search result), all subsequent reasoning builds on a false premise. Intercept and validate observations from real tools.
