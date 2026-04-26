---
layout: default
title: "16 · Generated Knowledge"
parent: Advanced Techniques
nav_order: 6
---

# Generated Knowledge Prompting
{: .no_toc }

**Tier:** Advanced · **Task types:** Factual accuracy, reasoning priming, expert-level responses · **Difficulty:** ⭐⭐⭐☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Generated knowledge prompting asks the model to **first generate relevant facts or context** about a topic before answering a question about it. By activating domain knowledge explicitly before the task, the model is better primed to produce accurate, specific answers — rather than drawing on whatever associations are most statistically prominent in training.

The technique is a prompt-level analogue to retrieval-augmented generation, using the model's own knowledge as the retrieval source.

---

## Use Cases

- **Accuracy-sensitive factual tasks** where the model is prone to confident hallucination in domain areas
- **Nuanced opinion questions** that benefit from the model first articulating relevant considerations before taking a position
- **Writing tasks requiring specific expertise** — priming with domain knowledge before writing produces more authoritative output

---

## Weak Prompt

```
Should a startup raise venture capital or bootstrap?
```

### Weak Output

> Whether to raise venture capital or bootstrap depends on your goals, runway, and market opportunity. VC funding provides capital and network but dilutes ownership...

**Assessment:** Generic advice that provides no new insight. The model defaulted to surface-level considerations without engaging with the structural trade-offs.

---

## Improved Prompt (Two-Step Generated Knowledge)

**Step 1 — Generate Knowledge:**
```
List 8 key facts about the structural differences between venture-backed and
bootstrapped startup trajectories, including typical growth rates, dilution,
time-to-exit, founder control, and failure modes. Be specific and cite
realistic ranges where possible.
```

**Step 1 Output (Gemini):**
> 1. VC-backed companies typically raise at 20–35% dilution per round; founders often own 10–20% at Series B.
> 2. Bootstrapped SaaS companies median ARR growth: ~50% YoY. VC-backed: pressure for 3× annual growth.
> 3. Median time to VC exit: 8–10 years; bootstrapped founders can take profits from year 1.
> 4. VC funds require a "venture-scale" outcome (10×+ return) — most markets don't support this.
> 5. Bootstrapped companies have 90%+ founder decision autonomy; VC-backed cede board seats typically from Series A.
> 6. 75% of VC-backed startups fail to return investor capital; many bootstrapped businesses are cash-flow positive.
> 7. VC is structurally suited to winner-take-all markets; bootstrapping suits niche, sustainable, or services businesses.
> 8. Down rounds and bridge notes are common VC dynamics that create significant founder dilution beyond initial terms.

**Step 2 — Answer the Question:**
```
Using these facts as your foundation, give a structured recommendation on
when a startup should raise VC vs. bootstrap. Be specific and decisive —
don't hedge everything.
```

**Step 2 Output (Gemini):**
> **Bootstrap if:** You're building in a niche, capital-efficient, or services market; you value founder control; your business can reach profitability within 24 months on revenue alone; or you want optionality over exit timing.
>
> **Raise VC if:** You're competing in a winner-take-all market where speed of scale determines who survives; your business requires significant upfront capital that revenue cannot fund; and you accept that you're optimising for a large-exit scenario — not lifestyle income.
>
> **The honest default:** Most startups should not raise VC. VC is a product with specific terms (high growth, large exit, dilution) that suits a narrow set of businesses. The bootstrapped path is harder in year 1 and more controlled in year 5.

**Assessment:** The answer is specific, decisive, and grounded in real structural considerations activated in Step 1.

---

## Verdict

Generated knowledge dramatically improves the specificity and accuracy of responses in domains where the model holds relevant knowledge but doesn't automatically surface it in a single-step prompt. The technique is essentially asking the model to do its own research before answering — the overhead is one extra prompt, and the output quality gain is significant.

---

## Common Pitfalls

**1. Hallucinated "facts" in Step 1**
The model may generate plausible but inaccurate knowledge. Verify key figures independently, especially for quantitative claims.

**2. Not referencing Step 1 in Step 2**
The second prompt must explicitly instruct the model to use the generated knowledge as a foundation — otherwise it may ignore it.

**3. Using generated knowledge on simple tasks**
Adding a knowledge-generation step to a simple factual question adds latency and cost without benefit. Reserve for complex, nuanced, or domain-specific tasks.
