# Prompt Engineering Playbook

A practitioner-oriented reference for **20 prompt engineering techniques** — each documented with original before-and-after examples, real Google Gemini API test results, honest verdicts, and documented failure modes.

🌐 **Live site:** https://nihalshx.github.io/prompt-playbook

---

## What's Inside

### 20 Documented Techniques

**Foundational (10):**
1. Zero-Shot Prompting
2. Few-Shot Prompting
3. Chain-of-Thought
4. Role-Play / Persona
5. Structured Output
6. Negative Constraints
7. Context Injection
8. Audience Specification
9. Tone Control
10. Instruction Clarity

**Advanced (10):**
11. Self-Consistency
12. ReAct Prompting
13. Step-Back Prompting
14. Prompt Chaining
15. Least-to-Most Decomposition
16. Generated Knowledge
17. Calibration Prompts
18. Directional Stimulus
19. Meta-Prompting
20. Evaluation Prompts

### Each Technique Page Includes

| Section | Content |
|---|---|
| **Definition** | Plain-English explanation |
| **Use Cases** | 3 practical scenarios |
| **Weak Prompt** | Underperforming example + why it fails |
| **Improved Prompt** | Same task, technique applied |
| **LLM Outputs** | Actual Gemini API responses for both |
| **Verdict** | Honest 2-sentence assessment |
| **Pitfalls** | Common mistakes and how to avoid them |

### Findings Summary

A data-driven synthesis of which techniques work best for which task types, with a full effectiveness matrix and recommended technique stacks.

---

## Project Structure

```
prompt-engineering-playbook/
├── _config.yml                   # Jekyll / Just the Docs config
├── Gemfile                       # Ruby dependencies
├── index.md                      # Home page
├── docs/
│   ├── foundational/
│   │   ├── index.md
│   │   ├── 01-zero-shot.md
│   │   ├── 02-few-shot.md
│   │   ├── 03-chain-of-thought.md
│   │   ├── 04-role-play.md
│   │   ├── 05-structured-output.md
│   │   ├── 06-negative-constraints.md
│   │   ├── 07-context-injection.md
│   │   ├── 08-audience-specification.md
│   │   ├── 09-tone-control.md
│   │   └── 10-instruction-clarity.md
│   ├── advanced/
│   │   ├── index.md
│   │   ├── 11-self-consistency.md
│   │   ├── 12-react-prompting.md
│   │   ├── 13-step-back.md
│   │   ├── 14-prompt-chaining.md
│   │   ├── 15-least-to-most.md
│   │   ├── 16-generated-knowledge.md
│   │   ├── 17-calibration-prompts.md
│   │   ├── 18-directional-stimulus.md
│   │   ├── 19-meta-prompting.md
│   │   └── 20-evaluation-prompts.md
│   └── findings-summary.md
├── scripts/
│   ├── test_techniques.py        # Main test runner (all 20 techniques)
│   ├── compare_outputs.py        # Results viewer + Markdown exporter
│   ├── quick_test.py             # Single prompt quick test
│   ├── requirements.txt
│   └── README.md
└── assets/
    └── css/
        └── custom.scss
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Site | GitHub Pages |
| Theme | [Just the Docs](https://just-the-docs.com/) (Jekyll) |
| LLM | Google Gemini (`gemini-1.5-flash`) |
| Testing Scripts | Python 3.11+ |
| SDK | `google-generativeai` |

---

## Deploying to GitHub Pages

### Option 1: Remote Theme (Recommended)

1. Fork this repository
2. Go to **Settings → Pages**
3. Set source to `Deploy from a branch` → `main` → `/ (root)`
4. Update `_config.yml`: change `url` and `baseurl` to your GitHub username
5. Your site will be live at `https://nihalshx.github.io/prompt-playbook`

### Option 2: Local Development

```bash
# Install Ruby dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Open http://localhost:4000
```

---

## Running the API Tests

```bash
cd scripts

# Install Python dependencies
pip install -r requirements.txt

# Set your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > .env

# Run all 20 techniques
python test_techniques.py

# Run a specific technique
python test_techniques.py --technique 3

# View results
python compare_outputs.py results/results_*.json
```

Get a free Gemini API key at: https://aistudio.google.com/app/apikey

---

## Motivation

This project was built to address the absence of practitioner-oriented, example-first prompt engineering resources. Most available documentation is either purely academic or superficially lists technique names without worked examples or honest failure-mode analysis.

Every technique in this playbook was tested hands-on. Verdicts reflect real observed behaviour, not theoretical performance claims.

---

## Licence

MIT. Use freely, attribution appreciated.
