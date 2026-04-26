"""
compare_outputs.py
==================
Reads saved test results and prints a formatted side-by-side comparison
of weak vs. improved prompt outputs for each technique.

Usage:
    python compare_outputs.py results/results_20250601_120000.json
    python compare_outputs.py results/results_20250601_120000.json --technique 3
    python compare_outputs.py results/results_20250601_120000.json --export md
"""

import json
import argparse
from pathlib import Path

DIVIDER = "─" * 70


def format_output(text: str, max_lines: int = 15) -> str:
    """Truncate output to max_lines for display."""
    lines = text.split("\n")
    if len(lines) > max_lines:
        return "\n".join(lines[:max_lines]) + f"\n... [{len(lines) - max_lines} more lines]"
    return text


def print_comparison(result: dict):
    """Print a single technique comparison."""
    print(f"\n{'='*70}")
    print(f"  #{result['id']} — {result['name'].upper()}")
    print(f"  Tier: {result['tier']} | Task: {result['task_type']}")
    print(f"  Model: {result.get('model', 'unknown')} | Tested: {result.get('timestamp', 'unknown')}")
    print(f"{'='*70}")

    print(f"\n{'WEAK PROMPT':^70}")
    print(DIVIDER)
    print(result.get("weak_prompt", "[not recorded]"))
    print(f"\n{'WEAK OUTPUT':^70}")
    print(DIVIDER)
    print(format_output(result.get("weak_output", "[no output]")))

    print(f"\n{'IMPROVED PROMPT':^70}")
    print(DIVIDER)
    print(result.get("improved_prompt", "[not recorded]"))
    print(f"\n{'IMPROVED OUTPUT':^70}")
    print(DIVIDER)
    improved = result.get("improved_output", "[no output]")
    print(format_output(improved))

    # Self-consistency: show all runs
    if "all_runs" in result:
        print(f"\n{'ALL RUNS (Self-Consistency)':^70}")
        print(DIVIDER)
        for i, run in enumerate(result["all_runs"], 1):
            print(f"\n  Run {i}:")
            print(f"  {run[:200]}{'...' if len(run) > 200 else ''}")


def export_markdown(results: list, output_path: str):
    """Export results as a Markdown file."""
    lines = ["# Prompt Engineering Playbook — Test Results\n"]

    for r in results:
        lines.append(f"## #{r['id']} — {r['name']}\n")
        lines.append(f"**Tier:** {r['tier']} | **Task:** {r['task_type']}\n")

        lines.append("### Weak Prompt\n")
        lines.append(f"```\n{r.get('weak_prompt', '')}\n```\n")
        lines.append("### Weak Output\n")
        lines.append(f"```\n{r.get('weak_output', '')}\n```\n")

        lines.append("### Improved Prompt\n")
        lines.append(f"```\n{r.get('improved_prompt', '')}\n```\n")
        lines.append("### Improved Output\n")
        lines.append(f"```\n{r.get('improved_output', '')}\n```\n")

        if "all_runs" in r:
            lines.append("### All Runs (Self-Consistency)\n")
            for i, run in enumerate(r["all_runs"], 1):
                lines.append(f"**Run {i}:** {run}\n\n")

        lines.append("---\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Exported to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Compare weak vs improved prompt outputs.")
    parser.add_argument("results_file", help="Path to results JSON file.")
    parser.add_argument("--technique", type=int, help="Show only this technique number.")
    parser.add_argument(
        "--export",
        choices=["md", "json"],
        help="Export results in specified format.",
    )
    args = parser.parse_args()

    results_path = Path(args.results_file)
    if not results_path.exists():
        print(f"ERROR: File not found: {results_path}")
        return

    with open(results_path, encoding="utf-8") as f:
        results = json.load(f)

    if args.technique:
        results = [r for r in results if r["id"] == args.technique]
        if not results:
            print(f"Technique {args.technique} not found in results.")
            return

    if args.export == "md":
        export_path = results_path.with_suffix(".md")
        export_markdown(results, str(export_path))
        return

    print(f"\nLoaded {len(results)} result(s) from {results_path.name}")
    for result in results:
        print_comparison(result)

    print(f"\n{'='*70}")
    print(f"End of results — {len(results)} technique(s) compared.")


if __name__ == "__main__":
    main()
