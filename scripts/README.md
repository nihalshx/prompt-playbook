# Prompt Engineering Playbook — Python Scripts

Scripts for testing all 20 techniques against the Google Gemini API.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your API key:**
   Create a `.env` file in the `scripts/` directory:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
   Get a free key at: https://aistudio.google.com/app/apikey

## Scripts

### `test_techniques.py` — Main test runner

Runs weak and improved prompt pairs through the Gemini API.

```bash
# Run all 20 techniques
python test_techniques.py

# Run a single technique
python test_techniques.py --technique 3

# Run all foundational techniques
python test_techniques.py --tier foundational

# Run all reasoning tasks
python test_techniques.py --task reasoning

# Save results to a custom directory
python test_techniques.py --output my_results/

# Run without saving to disk
python test_techniques.py --no-save
```

### `compare_outputs.py` — Results viewer

Loads saved results and displays formatted comparisons.

```bash
# View all results
python compare_outputs.py results/results_20250601_120000.json

# View a single technique
python compare_outputs.py results/results_20250601_120000.json --technique 5

# Export as Markdown
python compare_outputs.py results/results_20250601_120000.json --export md
```

### `quick_test.py` — Single prompt tester

Test a custom prompt instantly.

```bash
python quick_test.py "Explain quantum entanglement in one sentence."
python quick_test.py "Write a haiku about APIs." --temperature 1.0
python quick_test.py "What is 15% of 340?" --runs 5
```

## Results Format

Results are saved as JSON with this structure:

```json
[
  {
    "id": 1,
    "name": "Zero-Shot Prompting",
    "tier": "foundational",
    "task_type": "creative_writing",
    "timestamp": "2025-06-01T12:00:00",
    "model": "gemini-1.5-flash",
    "weak_prompt": "...",
    "weak_output": "...",
    "improved_prompt": "...",
    "improved_output": "..."
  }
]
```

## Rate Limits

The scripts include a 1.5-second delay between API calls to stay within free tier rate limits. Adjust `RATE_LIMIT_DELAY` in `test_techniques.py` if needed.

## Notes

- All techniques are tested at temperature 0.7 by default, except self-consistency (Technique 11), which uses 0.8 for meaningful variation across runs.
- Self-consistency runs 5 API calls for the improved prompt — plan accordingly for free tier quotas.
- Results may vary across runs due to model temperature and updates.
