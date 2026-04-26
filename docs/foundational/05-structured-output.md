---
layout: default
title: "05 · Structured Output"
parent: Foundational Techniques
nav_order: 5
---

# Structured Output Prompting
{: .no_toc }

**Tier:** Foundational · **Task types:** JSON generation, tables, parseable responses · **Difficulty:** ⭐⭐☆☆☆
{: .fs-4 .fw-300 }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Definition

Structured output prompting instructs the model to respond in a **specific machine-readable or visually structured format** — JSON, Markdown tables, numbered lists, XML, CSV, or a custom schema. This technique bridges the gap between LLM natural language outputs and downstream systems that require predictable data structures.

The key is specifying not just the format type but the **exact schema, field names, and data types** you need.

---

## Use Cases

- **API integrations** — generating JSON that will be parsed and stored in a database or passed to another service
- **Data extraction** — pulling structured fields (name, date, amount) from unstructured text such as invoices or emails
- **Consistent reporting** — generating reports where every output follows the same section structure for easy comparison

---

## Weak Prompt

```
Extract the key information from this job posting.

Job posting: "We're looking for a Senior Data Analyst to join our London team.
The role offers £65,000–£75,000 per year. Candidates must have 5+ years of
experience with SQL and Python. Apply by 31 July 2025."
```

### Weak Prompt Output (Gemini)

> Here are the key details from the job posting:
> - **Job Title:** Senior Data Analyst
> - **Location:** London
> - **Salary:** £65,000–£75,000 per year
> - **Required Skills:** SQL and Python (5+ years experience)
> - **Application Deadline:** 31 July 2025

**Assessment:** Readable but inconsistently formatted across different runs. Not directly parseable as structured data.

---

## Improved Prompt

```
Extract the key information from this job posting and return it as a
valid JSON object with exactly these fields:
- title (string)
- location (string)
- salary_min (integer, in GBP, no symbols)
- salary_max (integer, in GBP, no symbols)
- required_skills (array of strings)
- deadline (string, format: YYYY-MM-DD)

Return only the JSON object. No explanation, no markdown fences.

Job posting: "We're looking for a Senior Data Analyst to join our London team.
The role offers £65,000–£75,000 per year. Candidates must have 5+ years of
experience with SQL and Python. Apply by 31 July 2025."
```

### Improved Prompt Output (Gemini)

```json
{
  "title": "Senior Data Analyst",
  "location": "London",
  "salary_min": 65000,
  "salary_max": 75000,
  "required_skills": ["SQL", "Python"],
  "deadline": "2025-07-31"
}
```

**Assessment:** Valid JSON, correct field names, numeric types correctly parsed, date formatted as specified. Directly usable by a downstream parser.

---

## Verdict

Structured output prompting is essential for any LLM-integrated pipeline where outputs feed into code. Specifying the exact schema — field names, types, format — is the difference between a usable API and a string-parsing nightmare. The "no explanation" instruction is critical; omit it and most models will wrap the output in prose.

---

## Common Pitfalls

**1. Forgetting to say "no explanation"**
Without this instruction, most models wrap the JSON in a sentence like "Here is the JSON you requested:" which breaks naive JSON parsers. Be explicit.

**2. Underspecifying types**
"Return salary as a number" is ambiguous — integer or float? With currency symbol or without? Specify exactly.

**3. Not validating the output**
LLMs occasionally hallucinate fields or omit required ones. Always validate structured outputs against a schema (e.g., using Python's `jsonschema` library) before using them in production.
