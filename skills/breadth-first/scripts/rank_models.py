#!/usr/bin/env python3
"""Estimate token cost for exact available IDs supplied by the calling agent."""

import argparse
import json
from pathlib import Path
import sys

from catalog import rank

REFERENCES = Path(__file__).resolve().parents[1] / "references"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=REFERENCES / "model-catalog.json")
    parser.add_argument("--aliases", type=Path, default=REFERENCES / "host-aliases.json",
                        help="Host alias map; a missing file disables alias resolution")
    parser.add_argument("--model", action="append", required=True,
                        help="Available model ID or host alias; repeat for each candidate")
    parser.add_argument("--input-tokens", type=int, default=60000,
                        help="Per-packet input estimate (search workers read whole pages)")
    parser.add_argument("--output-tokens", type=int, default=3000)
    args = parser.parse_args()
    try:
        alias_map = (json.loads(args.aliases.read_text(encoding="utf-8"))
                     if args.aliases.is_file() else None)
        result = rank(json.loads(args.catalog.read_text(encoding="utf-8")), args.model,
                      args.input_tokens, args.output_tokens, alias_map=alias_map)
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "unavailable", "reason": str(exc)}))
        return 2
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0 if result["ranked"] else 2


if __name__ == "__main__":
    sys.exit(main())
