#!/usr/bin/env python3
"""Refresh the bundled reference atomically; never rewrite skill instructions."""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile
import urllib.request

from catalog import SOURCE_URL, guard_changes, normalize

DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "references/model-catalog.json"
MAX_BYTES = 10_000_000


def download():
    request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "breadth-first-catalog/1"})
    # urllib's default context verifies HTTPS certificates and uses inherited proxies.
    with urllib.request.urlopen(request, timeout=45) as response:
        if response.status != 200:
            raise ValueError(f"Unexpected HTTP status: {response.status}")
        raw = response.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("Upstream catalog exceeds size limit")
    return raw


def refresh(destination, fetch=download):
    updated = normalize(fetch())
    if destination.exists():
        guard_changes(json.loads(destination.read_text(encoding="utf-8")), updated)
    serialized = json.dumps(updated, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    destination.parent.mkdir(parents=True, exist_ok=True)
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=destination.parent,
                                         prefix=".model-catalog-", delete=False) as handle:
            temp_path = Path(handle.name)
            handle.write(serialized)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temp_path, 0o644)
        os.replace(temp_path, destination)
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
    return updated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    try:
        result = refresh(args.output)
    except (OSError, ValueError) as exc:
        print(f"Refresh failed; existing reference unchanged: {exc}", file=sys.stderr)
        return 1
    print(f"Refreshed {len(result['models'])} estimated model prices at {result['fetched_at']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
