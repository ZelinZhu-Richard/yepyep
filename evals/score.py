#!/usr/bin/env python3
"""Summarize graded eval runs: python3 evals/score.py evals/runs"""

import json
from collections import defaultdict
from pathlib import Path
import sys


def score(run):
    items = run["items"]
    valid = [i for i in items if i["valid"]]
    keys = {i["key"] for i in valid if i.get("key")}
    novel = {i["text"].strip().lower() for i in valid if not i.get("key")}
    distinct_all = len({i.get("key") or i["text"].strip().lower() for i in items})
    key_size = run.get("key_size")
    return {
        "distinct_valid": len(keys) + len(novel),
        "key_matched": len(keys),
        "key_recall": len(keys) / key_size if key_size else None,
        "novel_valid": len(novel),
        "invalid_listed": sum(1 for i in items if not i["valid"]),
        "duplicate_rate": 1 - distinct_all / len(items) if items else 0.0,
        "cost_usd": run.get("cost_usd"),
    }


def main(folder):
    groups = defaultdict(list)
    for path in sorted(Path(folder).glob("*.json")):
        if path.name == "example.json":
            continue
        run = json.loads(path.read_text(encoding="utf-8"))
        groups[(run["task"], run["arm"])].append(score(run))
    if not groups:
        print("No graded runs found.")
        return 1
    metrics = ["distinct_valid", "key_recall", "novel_valid", "invalid_listed",
               "duplicate_rate", "cost_usd"]
    print("task\tarm\truns\t" + "\t".join(metrics))
    for (task, arm), scores in sorted(groups.items()):
        cells = []
        for m in metrics:
            values = [s[m] for s in scores if s[m] is not None]
            if not values:
                cells.append("n/a")
                continue
            mean = sum(values) / len(values)
            cells.append(f"{mean:.2f} [{min(values):.2f}-{max(values):.2f}]")
        print(f"{task}\t{arm}\t{len(scores)}\t" + "\t".join(cells))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "evals/runs"))
