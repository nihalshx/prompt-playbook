"""
Prompt Engineering Playbook — Technique Tester
================================================
Tests all 20 prompt engineering techniques against the Google Gemini API.
Results are printed to stdout and optionally saved to a JSON file.

Usage:
    python test_techniques.py                    # Run all techniques
    python test_techniques.py --technique 3      # Run only technique 3 (CoT)
    python test_techniques.py --output results/  # Save results to directory
    python test_techniques.py --task reasoning   # Filter by task type

Requirements:
    pip install google-generativeai python-dotenv
    Set GEMINI_API_KEY in .env file or environment variable.
"""

import os
import json
import time
import argparse
from datetime import datetime
from pathlib import Path

try:
    import google.generativeai as genai
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: Required packages not installed.")
    print("Run: pip install google-generativeai python-dotenv")
    exit(1)

# ─── Configuration ────────────────────────────────────────────────────────────

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-flash"
DEFAULT_TEMPERATURE = 0.7
RATE_LIMIT_DELAY = 1.5  # seconds between API calls


# ─── Prompt Pairs ─────────────────────────────────────────────────────────────

TECHNIQUE_PROMPTS = {
    1: {
        "name": "Zero-Shot Prompting",
        "tier": "foundational",
        "task_type": "creative_writing",
        "weak": "Write something about climate change.",
        "improved": (
            "Write a 3-sentence explanation of climate change for a Year 8 science class. "
            "Use simple vocabulary. End with one concrete action students can take this week."
        ),
    },
    2: {
        "name": "Few-Shot Prompting",
        "tier": "foundational",
        "task_type": "classification",
        "weak": (
            'Label these customer reviews as positive, negative, or neutral.\n\n'
            'Review: "The packaging was damaged but the product itself works fine."'
        ),
        "improved": (
            "Label each customer review as POSITIVE, NEGATIVE, or NEUTRAL.\n"
            "Use only these three labels — no explanations.\n\n"
            "Examples:\n"
            'Review: "Arrived quickly and exactly as described." → POSITIVE\n'
            'Review: "Stopped working after two days. Very disappointed." → NEGATIVE\n'
            'Review: "It\'s okay. Nothing special but does the job." → NEUTRAL\n\n'
            "Now label this review:\n"
            'Review: "The packaging was damaged but the product itself works fine."'
        ),
    },
    3: {
        "name": "Chain-of-Thought",
        "tier": "foundational",
        "task_type": "reasoning",
        "weak": (
            "A store sells apples for £0.40 each and oranges for £0.65 each. "
            "Sarah buys 7 apples and 4 oranges. She pays with a £10 note. "
            "How much change does she receive?"
        ),
        "improved": (
            "A store sells apples for £0.40 each and oranges for £0.65 each. "
            "Sarah buys 7 apples and 4 oranges. She pays with a £10 note. "
            "How much change does she receive?\n\n"
            "Think through this step by step before giving the final answer."
        ),
    },
    4: {
        "name": "Role-Play / Persona",
        "tier": "foundational",
        "task_type": "technical",
        "weak": "Explain why my Python code is slow.",
        "improved": (
            "You are a senior Python performance engineer with 10 years of experience "
            "optimising production codebases. A junior developer has shared this code "
            "and asked why it's slow. Diagnose the specific bottlenecks and explain "
            "each one clearly enough for a junior to understand.\n\n"
            "```python\n"
            "data = []\n"
            "for i in range(100000):\n"
            "    data = data + [i * 2]\n"
            "```"
        ),
    },
    5: {
        "name": "Structured Output",
        "tier": "foundational",
        "task_type": "extraction",
        "weak": (
            "Extract the key information from this job posting.\n\n"
            "Job posting: \"We're looking for a Senior Data Analyst to join our London team. "
            "The role offers £65,000–£75,000 per year. Candidates must have 5+ years of "
            "experience with SQL and Python. Apply by 31 July 2025.\""
        ),
        "improved": (
            "Extract the key information from this job posting and return it as a "
            "valid JSON object with exactly these fields:\n"
            "- title (string)\n"
            "- location (string)\n"
            "- salary_min (integer, in GBP, no symbols)\n"
            "- salary_max (integer, in GBP, no symbols)\n"
            "- required_skills (array of strings)\n"
            "- deadline (string, format: YYYY-MM-DD)\n\n"
            "Return only the JSON object. No explanation, no markdown fences.\n\n"
            "Job posting: \"We're looking for a Senior Data Analyst to join our London team. "
            "The role offers £65,000–£75,000 per year. Candidates must have 5+ years of "
            "experience with SQL and Python. Apply by 31 July 2025.\""
        ),
    },
    6: {
        "name": "Negative Constraints",
        "tier": "foundational",
        "task_type": "summarisation",
        "weak": "Summarise the key risks of investing in cryptocurrency.",
        "improved": (
            "Summarise the key risks of investing in cryptocurrency in 4 bullet points. "
            "Do not include any disclaimers, caveats about consulting a financial advisor, "
            "or 'not financial advice' statements. Do not add a closing sentence."
        ),
    },
    7: {
        "name": "Context Injection",
        "tier": "foundational",
        "task_type": "creative_writing",
        "weak": "Write an email to a customer explaining why their order is delayed.",
        "improved": (
            "Use the following order information to write a customer delay email:\n\n"
            "ORDER CONTEXT:\n"
            "- Customer name: Priya Sharma\n"
            "- Order number: #ORD-48821\n"
            "- Product: Ergonomic Office Chair (Black, Large)\n"
            "- Original delivery date: 18 June 2025\n"
            "- New estimated delivery date: 25 June 2025\n"
            "- Reason for delay: Port congestion at Felixstowe affecting all shipments\n"
            "- Compensation offered: £10 voucher code DELAY10\n\n"
            "Write a professional but warm email that explains the delay specifically, "
            "gives the new date, and includes the voucher. 3 paragraphs. No generic "
            "'I hope this finds you well' opener."
        ),
    },
    8: {
        "name": "Audience Specification",
        "tier": "foundational",
        "task_type": "explanation",
        "weak": "Explain what an API is.",
        "improved": (
            "Explain what an API is to a non-technical marketing manager who has heard "
            "the term in meetings and wants to understand what it means in plain English. "
            "Use a real-world analogy. Maximum 100 words. No code, no technical jargon."
        ),
    },
    9: {
        "name": "Tone Control",
        "tier": "foundational",
        "task_type": "creative_writing",
        "weak": "Write a product description for a premium noise-cancelling headphone.",
        "improved": (
            "Write a product description for a premium noise-cancelling headphone.\n\n"
            "Tone: Confident and slightly poetic. Like a luxury watch brand — understated, "
            "precise, with no exclamation marks and no superlatives like 'exceptional' or "
            "'superior.' Let the product details do the persuading, not the adjectives. "
            "60–80 words."
        ),
    },
    10: {
        "name": "Instruction Clarity",
        "tier": "foundational",
        "task_type": "editing",
        "weak": (
            "Make this email better.\n\n"
            "Dear John, I just wanted to reach out and sorry to bother you but I was "
            "wondering if maybe you had a chance to look at the proposal I sent last week. "
            "If you have any questions or anything like that please let me know. Thanks so much."
        ),
        "improved": (
            "Rewrite the following email to achieve these specific goals:\n"
            "1. Reduce length by approximately 40% — cut filler sentences\n"
            "2. Make the ask in the email explicit and move it to the opening\n"
            "3. Adopt a direct, professional tone — remove hedge phrases like "
            "'I just wanted to' and 'sorry to bother you'\n"
            "4. Keep all factual details unchanged\n\n"
            "Return only the rewritten email. Do not explain what you changed.\n\n"
            "Dear John, I just wanted to reach out and sorry to bother you but I was "
            "wondering if maybe you had a chance to look at the proposal I sent last week. "
            "If you have any questions or anything like that please let me know. Thanks so much."
        ),
    },
    11: {
        "name": "Self-Consistency",
        "tier": "advanced",
        "task_type": "reasoning",
        "weak": (
            "A train leaves City A at 09:00 travelling at 90 km/h toward City B. "
            "Another train leaves City B at 10:00 travelling at 110 km/h toward City A. "
            "The cities are 400 km apart. At what time do the trains meet?"
        ),
        "improved": (
            "A train leaves City A at 09:00 travelling at 90 km/h toward City B. "
            "Another train leaves City B at 10:00 travelling at 110 km/h toward City A. "
            "The cities are 400 km apart. At what time do the trains meet?\n\n"
            "Think step by step. Show your working. End with: ANSWER: [time in HH:MM format]"
        ),
        "runs": 5,  # Self-consistency: run multiple times
        "temperature": 0.8,
    },
    12: {
        "name": "ReAct Prompting",
        "tier": "advanced",
        "task_type": "reasoning",
        "weak": "What is the GDP per capita of the country with the highest HDI score?",
        "improved": (
            "Answer the following question using this Thought/Action/Observation format.\n"
            "Available actions: search[query], calculate[expression], finish[answer]\n\n"
            "Simulate the search results yourself — make them realistic and accurate.\n\n"
            "Question: What is the GDP per capita of the country with the highest HDI score?\n\n"
            "Begin:\nThought:"
        ),
    },
    13: {
        "name": "Step-Back Prompting",
        "tier": "advanced",
        "task_type": "reasoning",
        "weak": (
            "A 2kg ball is dropped from a height of 20 metres. What is its velocity "
            "just before it hits the ground? Ignore air resistance."
        ),
        "improved": (
            "First, explain the key physics principles that govern how objects fall under "
            "gravity and how to calculate their velocity at impact (core equations only, "
            "3–4 sentences).\n\n"
            "Then, using those principles, calculate the velocity of a 2kg ball dropped "
            "from 20 metres just before impact. Note any distractors in the problem."
        ),
    },
    14: {
        "name": "Prompt Chaining",
        "tier": "advanced",
        "task_type": "creative_writing",
        "weak": (
            "Research the pros and cons of remote work, write a balanced 500-word article "
            "with an introduction, three supporting points, and a conclusion."
        ),
        "improved": (
            "CHAIN STEP 1 of 2 — Research Phase:\n\n"
            "List 5 well-evidenced benefits and 5 well-evidenced drawbacks of remote work "
            "for knowledge workers. For each point, include one supporting statistic or "
            "data point. Format as two numbered lists. Be specific — no generic claims."
        ),
    },
    15: {
        "name": "Least-to-Most Decomposition",
        "tier": "advanced",
        "task_type": "reasoning",
        "weak": (
            "Is it legal for an employer to monitor employee emails on company devices "
            "in the UK without telling them?"
        ),
        "improved": (
            "Answer this question using least-to-most decomposition.\n"
            "First identify 3 simpler sub-questions that must be answered first, "
            "answer each one, then use those answers to address the full question.\n\n"
            "Question: Is it legal for an employer to monitor employee emails on company "
            "devices in the UK without telling them?"
        ),
    },
    16: {
        "name": "Generated Knowledge",
        "tier": "advanced",
        "task_type": "reasoning",
        "weak": "Should a startup raise venture capital or bootstrap?",
        "improved": (
            "STEP 1: List 6 key structural facts about the differences between "
            "venture-backed and bootstrapped startup trajectories — include typical "
            "dilution ranges, growth expectations, and founder control implications.\n\n"
            "STEP 2: Using those facts as your foundation, give a specific, decisive "
            "recommendation on when a startup should raise VC vs. bootstrap. "
            "Don't hedge everything — take a position."
        ),
    },
    17: {
        "name": "Calibration Prompts",
        "tier": "advanced",
        "task_type": "factual",
        "weak": "What is the approximate population of Lagos, Nigeria?",
        "improved": (
            "What is the approximate population of Lagos, Nigeria?\n\n"
            "After your answer, rate your confidence 1–5 (1=guessing, 5=certain) "
            "and identify any sources of uncertainty in your figure (e.g., "
            "metro vs. city proper, data recency, definitional issues)."
        ),
    },
    18: {
        "name": "Directional Stimulus",
        "tier": "advanced",
        "task_type": "creative_writing",
        "weak": "Write a short poem about artificial intelligence.",
        "improved": (
            "Write a short poem about artificial intelligence.\n"
            "Consider: silence, inheritance, borrowed light, the question no one asked."
        ),
    },
    19: {
        "name": "Meta-Prompting",
        "tier": "advanced",
        "task_type": "prompt_generation",
        "weak": "Write me a good prompt for summarising articles.",
        "improved": (
            "I need a high-quality prompt for an automated pipeline that summarises "
            "news articles before sending them to busy executives. Requirements:\n"
            "- Outputs should be 3–5 sentences maximum\n"
            "- Must preserve key people, organisations, and numerical figures\n"
            "- Should flag if the article is opinion vs. news reporting\n"
            "- Tone should be neutral and factual\n"
            "- Must work across articles from 200–5000 words\n\n"
            "Write two prompt variants and explain the key design choices behind each."
        ),
    },
    20: {
        "name": "Evaluation Prompts",
        "tier": "advanced",
        "task_type": "evaluation",
        "weak": (
            "Is this a good customer service response?\n\n"
            "Dear Customer, thank you for reaching out. We're sorry to hear about your "
            "experience. Your case has been escalated to our team and someone will be in "
            "touch. We appreciate your patience."
        ),
        "improved": (
            "You are a customer service quality evaluator. Score the following response "
            "on these four criteria, each scored 1–5:\n\n"
            "1. Resolution clarity (1=vague, 5=specific next steps given)\n"
            "2. Tone appropriateness (1=cold/defensive, 5=warm/professional)\n"
            "3. Accuracy (1=errors or missing info, 5=factually complete)\n"
            "4. Conciseness (1=excessive, 5=appropriately brief)\n\n"
            "For each: score + one sentence justification + one improvement suggestion.\n"
            "End with: TOTAL: [sum]/20 and OVERALL_VERDICT: PASS (≥14) or FAIL (<14).\n\n"
            "Response to evaluate:\n---\n"
            "Dear Customer, thank you for reaching out. We're sorry to hear about your "
            "experience. Your case has been escalated to our team and someone will be in "
            "touch. We appreciate your patience.\n---"
        ),
    },
}


# ─── API Functions ─────────────────────────────────────────────────────────────

def init_gemini():
    """Initialise the Gemini API client."""
    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY not found. Set it in .env file or as an environment variable."
        )
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel(MODEL_NAME)


def call_gemini(model, prompt: str, temperature: float = DEFAULT_TEMPERATURE) -> str:
    """Call the Gemini API and return the text response."""
    config = genai.types.GenerationConfig(temperature=temperature)
    response = model.generate_content(prompt, generation_config=config)
    return response.text.strip()


def run_self_consistency(model, prompt: str, runs: int, temperature: float) -> dict:
    """Run a prompt multiple times and return all outputs plus majority answer."""
    outputs = []
    for i in range(runs):
        print(f"    Run {i+1}/{runs}...", end=" ", flush=True)
        output = call_gemini(model, prompt, temperature=temperature)
        outputs.append(output)
        print("done")
        if i < runs - 1:
            time.sleep(RATE_LIMIT_DELAY)
    return {"all_outputs": outputs, "run_count": runs}


# ─── Testing Logic ─────────────────────────────────────────────────────────────

def test_technique(model, technique_id: int, technique: dict) -> dict:
    """Test a single technique (weak + improved prompts)."""
    print(f"\n{'='*60}")
    print(f"Testing Technique {technique_id}: {technique['name']}")
    print(f"  Tier: {technique['tier']} | Task: {technique['task_type']}")
    print(f"{'='*60}")

    result = {
        "id": technique_id,
        "name": technique["name"],
        "tier": technique["tier"],
        "task_type": technique["task_type"],
        "timestamp": datetime.now().isoformat(),
        "model": MODEL_NAME,
    }

    # --- Weak prompt ---
    print(f"\n  [WEAK] Running weak prompt...")
    try:
        weak_output = call_gemini(model, technique["weak"])
        result["weak_prompt"] = technique["weak"]
        result["weak_output"] = weak_output
        print(f"  [WEAK] Output ({len(weak_output)} chars):")
        print(f"  {weak_output[:200]}{'...' if len(weak_output) > 200 else ''}")
    except Exception as e:
        result["weak_output"] = f"ERROR: {e}"
        print(f"  [WEAK] ERROR: {e}")

    time.sleep(RATE_LIMIT_DELAY)

    # --- Improved prompt ---
    print(f"\n  [IMPROVED] Running improved prompt...")
    try:
        runs = technique.get("runs", 1)
        temperature = technique.get("temperature", DEFAULT_TEMPERATURE)

        if runs > 1:  # Self-consistency
            sc_result = run_self_consistency(model, technique["improved"], runs, temperature)
            result["improved_prompt"] = technique["improved"]
            result["improved_output"] = sc_result["all_outputs"][0]
            result["all_runs"] = sc_result["all_outputs"]
            result["run_count"] = sc_result["run_count"]
            print(f"  [IMPROVED] {runs} runs completed.")
        else:
            improved_output = call_gemini(model, technique["improved"], temperature)
            result["improved_prompt"] = technique["improved"]
            result["improved_output"] = improved_output
            print(f"  [IMPROVED] Output ({len(improved_output)} chars):")
            print(f"  {improved_output[:200]}{'...' if len(improved_output) > 200 else ''}")

    except Exception as e:
        result["improved_output"] = f"ERROR: {e}"
        print(f"  [IMPROVED] ERROR: {e}")

    return result


def run_tests(technique_ids: list, output_dir: str = None) -> list:
    """Run tests for the specified technique IDs."""
    print(f"\nPrompt Engineering Playbook — Technique Tester")
    print(f"Model: {MODEL_NAME}")
    print(f"Techniques to test: {technique_ids}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    model = init_gemini()
    results = []

    for technique_id in technique_ids:
        if technique_id not in TECHNIQUE_PROMPTS:
            print(f"WARNING: Technique {technique_id} not found. Skipping.")
            continue

        technique = TECHNIQUE_PROMPTS[technique_id]
        result = test_technique(model, technique_id, technique)
        results.append(result)

        # Rate limit between techniques
        if technique_id != technique_ids[-1]:
            time.sleep(RATE_LIMIT_DELAY)

    if output_dir:
        save_results(results, output_dir)

    print(f"\n{'='*60}")
    print(f"Testing complete. {len(results)} technique(s) tested.")
    return results


def save_results(results: list, output_dir: str):
    """Save results to a JSON file."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = Path(output_dir) / f"results_{timestamp}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to: {output_path}")


# ─── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Test prompt engineering techniques against the Gemini API."
    )
    parser.add_argument(
        "--technique",
        type=int,
        help="Run only this technique number (1–20). Omit to run all.",
    )
    parser.add_argument(
        "--tier",
        choices=["foundational", "advanced"],
        help="Run only techniques from this tier.",
    )
    parser.add_argument(
        "--task",
        help="Run only techniques with this task type.",
    )
    parser.add_argument(
        "--output",
        default="results/",
        help="Directory to save JSON results (default: results/).",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Don't save results to disk.",
    )

    args = parser.parse_args()

    # Filter techniques
    if args.technique:
        ids = [args.technique]
    else:
        ids = list(TECHNIQUE_PROMPTS.keys())

    if args.tier:
        ids = [i for i in ids if TECHNIQUE_PROMPTS[i].get("tier") == args.tier]

    if args.task:
        ids = [i for i in ids if TECHNIQUE_PROMPTS[i].get("task_type") == args.task]

    if not ids:
        print("No techniques match the specified filters.")
        return

    output_dir = None if args.no_save else args.output
    run_tests(ids, output_dir)


if __name__ == "__main__":
    main()
