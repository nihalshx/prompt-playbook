---
layout: default
title: "07 · Context Injection"
parent: Foundational Techniques
nav_order: 7
---

# Context Injection
{: .no_toc }

**Tier:** Foundational · **Task types:** Grounded writing, factual tasks, document analysis · **Difficulty:** ⭐⭐⭐☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Context injection provides the model with **relevant background information before the task** — documents, data, policies, conversation history, or factual grounding — so that the response is anchored in specific content rather than general knowledge. It is the prompt-engineering equivalent of briefing a consultant before asking them to advise.

Context injection is the foundation of Retrieval-Augmented Generation (RAG) systems at the prompt level.

---

## Use Cases

- **Document-grounded Q&A** — answering questions based on a specific policy, report, or knowledge base rather than general internet knowledge
- **Personalised outputs** — providing user-specific information (account status, past interactions) so the model responds relevantly
- **Fact-anchored writing** — supplying specific statistics, quotes, or product specifications that must appear accurately in the output

---

## Weak Prompt

```
Write an email to a customer explaining why their order is delayed.
```

### Weak Prompt Output (Gemini)

> Dear Customer,
>
> I hope this email finds you well. I am writing to inform you that your recent order has unfortunately been delayed due to unforeseen circumstances. We sincerely apologise for any inconvenience this may cause...

**Assessment:** Generic template. No specific order details, no real reason, no timeline. Not usable without significant manual editing.

---

## Improved Prompt

```
Use the following order information to write a customer delay email:

ORDER CONTEXT:
- Customer name: Priya Sharma
- Order number: #ORD-48821
- Product: Ergonomic Office Chair (Black, Large)
- Original delivery date: 18 June 2025
- New estimated delivery date: 25 June 2025
- Reason for delay: Port congestion at Felixstowe affecting all shipments
- Compensation offered: £10 voucher code DELAY10

Write a professional but warm email that explains the delay specifically,
gives the new date, and includes the voucher. 3 paragraphs. No generic
"I hope this finds you well" opener.
```

### Improved Prompt Output (Gemini)

> Subject: Update on Your Order #ORD-48821 — New Delivery Date
>
> Dear Priya,
>
> We're writing to let you know that your Ergonomic Office Chair (Black, Large) has been delayed due to port congestion at Felixstowe, which is currently affecting shipments across the industry. Your order is now expected to arrive by **25 June 2025**, one week later than originally scheduled.
>
> We understand this is frustrating, and we're sorry for the disruption to your plans. To say thank you for your patience, we'd like to offer you a **£10 voucher** — use code **DELAY10** on your next order, valid for 90 days.
>
> Your order is in the queue and we'll send tracking updates as soon as it's dispatched. If you have any questions in the meantime, please don't hesitate to contact us.

**Assessment:** Specific, accurate, personalised, directly usable. The injected context produced an output that requires no editing.

---

## Verdict

Context injection is the technique that turns LLMs from general-purpose text generators into task-specific tools. The quality of the injected context directly determines output quality — garbage in, garbage out applies here more than anywhere else. Structure your context clearly, label it explicitly, and separate it visually from the instruction.

---

## Common Pitfalls

**1. Dumping unstructured context**
Pasting a 10,000-word document and asking "answer questions about this" produces worse results than extracting and formatting the relevant sections first.

**2. Not labelling the context boundary**
The model needs to know where context ends and the task begins. Use clear labels: `CONTEXT:`, `TASK:`, or delimiter lines.

**3. Mixing stale and current context**
If your injected context contains outdated information, the model will faithfully reproduce it. Keep context fresh, especially for time-sensitive tasks.
