---
layout: default
title: "04 · Role-Play / Persona"
parent: Foundational Techniques
nav_order: 4
---

# Role-Play / Persona Prompting
{: .no_toc }

**Tier:** Foundational · **Task types:** Expert tone, domain-specific writing, audience calibration · **Difficulty:** ⭐⭐☆☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Role-play (or persona) prompting assigns the model an **expert identity before the task begins**. By framing the model as a specific type of professional — "You are a senior data engineer", "You are an experienced GP" — you activate vocabulary, reasoning patterns, and assumptions appropriate to that role. The technique doesn't grant the model knowledge it doesn't have, but it does shift the register, depth, and framing of responses.

---

## Use Cases

- **Expert domain writing** — technical documentation, legal summaries, medical explainers written at a professional level
- **Feedback and critique** — the model adopts an editor's, mentor's, or reviewer's perspective rather than being generically helpful
- **Audience-matched communication** — framing the model as the reader ("You are a sceptical CFO reviewing this proposal") can improve analytical depth

---

## Weak Prompt

```
Explain why my Python code is slow.
```

### Weak Prompt Output (Gemini)

> There are many reasons why Python code can be slow. Common causes include using inefficient data structures, unnecessary loops, not using built-in functions, and memory management issues...

**Assessment:** Generic. Doesn't ask for the code. Treats the request as a tutorial rather than a diagnostic task.

---

## Improved Prompt

```
You are a senior Python performance engineer with 10 years of experience
optimising production codebases. A junior developer has shared this code
and asked why it's slow. Diagnose the specific bottlenecks and explain
each one clearly enough for a junior to understand.

```python
data = []
for i in range(100000):
    data = data + [i * 2]
```
```

### Improved Prompt Output (Gemini)

> As a performance engineer, I can see two significant issues here:
>
> **1. List concatenation inside a loop (major bottleneck)**
> `data = data + [i * 2]` creates a **brand new list** on every iteration. With 100,000 iterations, Python is allocating and copying increasingly large lists — this is O(n²) behaviour. The correct approach is `data.append(i * 2)`, which is O(1) amortised.
>
> **2. Better still: use a list comprehension**
> `data = [i * 2 for i in range(100000)]` is not only more Pythonic but also faster at the interpreter level because list comprehensions are optimised in CPython.
>
> The first fix alone will reduce your runtime from potentially seconds to milliseconds for this input size.

**Assessment:** Specific diagnosis, junior-accessible explanation, concrete fixes. The persona framing produced a substantially more useful response.

---

## Verdict

Role-play prompting reliably shifts the register and specificity of outputs. It's most effective when the persona is concrete (specify experience level, specialism, and context) rather than vague ("act as an expert"). The technique is less useful for purely factual tasks where persona has no bearing on content.

---

## Common Pitfalls

**1. Vague persona specification**
"Act as an expert" is nearly useless — expert in what? For whom? With what constraints? Specify: role, experience level, audience, and task framing.

**2. Expecting personas to grant knowledge**
A "medical doctor" persona improves register and structure but does not give the model clinical knowledge it doesn't have. Always verify domain-specific factual claims independently.

**3. Forgetting the task after setting the persona**
Some prompts spend so much effort on persona setup that the actual task is underspecified. Balance persona detail with clear task instruction.
