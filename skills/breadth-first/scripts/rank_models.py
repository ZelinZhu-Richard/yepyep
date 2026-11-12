#!/usr/bin/env python3
"""Estimate token cost for exact available IDs supplied by the calling agent."""

import argparse
import json
from pathlib import Path
import sys

from catalog import rank


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path,
                        default=Path(__file__).resolve().parents[1] / "references/model-catalog.json")
    parser.add_argument("--model", action="append", required=True,
                        help="Exact available model ID; repeat for each candidate")
    parser.add_argument("--input-tokens", type=int, default=4000)
    parser.add_argument("--output-tokens", type=int, default=1000)
    args = parser.parse_args()
    try:
        result = rank(json.loads(args.catalog.read_text(encoding="utf-8")), args.model,
                      args.input_tokens, args.output_tokens)
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "unavailable", "reason": str(exc)}))
        return 2
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0 if result["ranked"] else 2


if __name__ == "__main__":
    sys.exit(main())
