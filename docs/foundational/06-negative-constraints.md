---
layout: default
title: "06 · Negative Constraints"
parent: Foundational Techniques
nav_order: 6
---

# Negative Constraints
{: .no_toc }

**Tier:** Foundational · **Task types:** Scoping, content filtering, format control · **Difficulty:** ⭐⭐☆☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Negative constraints explicitly tell the model **what to exclude, avoid, or not do** in its response. While most prompts focus on what the model should produce, negative constraints are often equally important: they eliminate default behaviours that would otherwise appear — filler phrases, caveats, irrelevant tangents, or unwanted formats.

Used alongside positive instructions, negative constraints tighten the output scope significantly.

---

## Use Cases

- **Removing boilerplate** — eliminating "Great question!" openers, unnecessary caveats, or closing pleasantries from professional outputs
- **Scoping content** — preventing the model from including information that's off-topic, too advanced, or outside a defined domain
- **Format enforcement** — blocking the model from using bullet points when you need prose, or from using headers when you need plain text

---

## Weak Prompt

```
Summarise the key risks of investing in cryptocurrency.
```

### Weak Prompt Output (Gemini)

> Cryptocurrency investing carries several significant risks that potential investors should carefully consider before committing funds. These include high price volatility, regulatory uncertainty, security risks such as hacks and scams, lack of consumer protections, liquidity issues with smaller coins, and the potential for total loss of investment. It's important to do thorough research and only invest what you can afford to lose. As always, this is not financial advice and you should consult a qualified financial advisor before making any investment decisions.

**Assessment:** The last two sentences are filler. The "not financial advice" disclaimer and "consult a financial advisor" are default model behaviours, not requested content.

---

## Improved Prompt

```
Summarise the key risks of investing in cryptocurrency in 4 bullet points.
Do not include any disclaimers, caveats about consulting a financial advisor,
or "not financial advice" statements. Do not add a closing sentence.
```

### Improved Prompt Output (Gemini)

> - **Extreme price volatility:** Cryptocurrency values can drop 50–90% in months, making it unsuitable for capital preservation.
> - **Regulatory risk:** Governments worldwide may restrict or ban crypto assets, potentially rendering holdings worthless or illiquid.
> - **Security vulnerabilities:** Exchange hacks, wallet theft, and phishing scams have resulted in billions in losses with no recourse.
> - **Liquidity risk:** Smaller altcoins may have insufficient trading volume to exit positions at desired prices.

**Assessment:** Focused, no filler, directly usable. Four points as requested.

---

## Verdict

Negative constraints are underused but highly effective. They're especially valuable when you know the model's default behaviours (disclaimer-adding, hedge-filling, pleasantry-inserting) and want to suppress them. The technique is most powerful in combination with positive instructions — tell the model what to do AND what not to do.

---

## Common Pitfalls

**1. Using negatives ambiguously**
"Don't be too technical" is vague. "Use no jargon that a non-engineer would not understand" is specific. Make negatives as precise as your positive instructions.

**2. Over-constraining to the point of impossibility**
Stacking too many negative constraints can produce stilted, constrained output that's technically compliant but unreadable. Test iteratively.

**3. Assuming negatives always hold**
LLMs sometimes violate negative constraints, especially on longer outputs. For critical exclusions (e.g., no personally identifiable information), always validate programmatically.
