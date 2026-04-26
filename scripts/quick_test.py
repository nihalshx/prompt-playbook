"""
quick_test.py
=============
Quick script to test a single custom prompt against Gemini.
Useful for experimenting with technique variants during development.

Usage:
    python quick_test.py "Your prompt here"
    python quick_test.py "Your prompt here" --temperature 0.9
    python quick_test.py "Your prompt here" --runs 3
"""

import os
import sys
import argparse

try:
    import google.generativeai as genai
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: Run: pip install google-generativeai python-dotenv")
    sys.exit(1)

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-flash"


def call_gemini(prompt: str, temperature: float = 0.7) -> str:
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not set in .env or environment.")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
    config = genai.types.GenerationConfig(temperature=temperature)
    response = model.generate_content(prompt, generation_config=config)
    return response.text.strip()


def main():
    parser = argparse.ArgumentParser(description="Quick Gemini API test.")
    parser.add_argument("prompt", help="Prompt to send to Gemini.")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--runs", type=int, default=1)
    args = parser.parse_args()

    print(f"\nModel: {MODEL_NAME} | Temperature: {args.temperature}")
    print(f"\nPROMPT:\n{'─'*50}")
    print(args.prompt)
    print(f"{'─'*50}\n")

    for i in range(args.runs):
        if args.runs > 1:
            print(f"RUN {i+1}/{args.runs}:")
        print(f"{'─'*50}")
        output = call_gemini(args.prompt, args.temperature)
        print(output)
        print()


if __name__ == "__main__":
    main()
