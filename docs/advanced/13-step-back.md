---
layout: default
title: "13 · Step-Back Prompting"
parent: Advanced Techniques
nav_order: 3
---

# Step-Back Prompting
{: .no_toc }

**Tier:** Advanced · **Task types:** Abstract reasoning, concept explanation, first-principles analysis · **Difficulty:** ⭐⭐⭐☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Step-back prompting asks the model to **first answer a more abstract, general version of the question**, then use that general answer to reason toward the specific answer. It forces the model to activate broader conceptual knowledge before narrowing to specifics — improving accuracy on tasks that require domain knowledge or first-principles reasoning.

The technique involves two prompts: (1) "What are the general principles governing X?" and (2) "Given those principles, answer this specific question: Y?"

---

## Use Cases

- **Physics / science problems** where the correct answer requires applying a general law to a specific scenario
- **Policy analysis** — stepping back to general principles before evaluating a specific case
- **Debugging** — identifying what category of problem applies before diagnosing a specific bug

---

## Weak Prompt (Direct Question)

```
A 2kg ball is dropped from a height of 20 metres. What is its velocity
just before it hits the ground? Ignore air resistance.
```

### Output

> Using kinematics: v² = u² + 2as = 0 + 2(9.8)(20) = 392. v = √392 ≈ **19.8 m/s**

*(Correct, but the model may struggle on less standard variants without the conceptual grounding.)*

---

## Improved Approach (Step-Back)

**Prompt 1 — Step Back:**
```
What are the key physics principles that govern how objects fall under gravity
and how to calculate their velocity at impact? Explain the core equations.
```

**Output 1:**
> Energy conservation: PE = KE at impact → mgh = ½mv² → v = √(2gh).
> Kinematic alternative: v² = u² + 2as, where u=0, a=9.8 m/s², s=height.
> Both approaches give the same result for free-fall problems.

**Prompt 2 — Apply to Specific:**
```
Using those principles, calculate the velocity of a 2kg ball dropped
from 20 metres just before impact. Show which equation you're using and why.
```

**Output 2:**
> Using energy conservation (v = √(2gh)): v = √(2 × 9.8 × 20) = √392 ≈ **19.8 m/s**.
> Note: Mass is irrelevant — the 2kg is a distractor; free-fall velocity depends only on height and g.

**Assessment:** The step-back correctly identified that mass is a distractor — something the direct prompt may not explicitly surface.

---

## Verdict

Step-back prompting is particularly effective for problems that contain irrelevant information (distractors) or where the model tends to pattern-match to surface features rather than underlying principles. The two-prompt overhead is worth it for high-stakes reasoning tasks.

---

## Common Pitfalls

**1. Using step-back on simple factual lookups**
"What is the capital of France?" does not benefit from first-principles reasoning. Reserve for genuinely complex tasks.

**2. Not connecting the step-back to the specific question**
The second prompt must explicitly reference the principles generated in the first. Don't assume the model will connect them automatically.

**3. Accepting a shallow step-back**
If the first prompt produces a vague or surface-level abstraction, the second prompt will inherit that shallowness. Push for depth: "What are the fundamental equations?" not "What is important about this topic?"
