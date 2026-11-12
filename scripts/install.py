#!/usr/bin/env python3
"""Link the shared skill into a project or personal skill directory."""

import argparse
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "skills/breadth-first"


def install(root, host):
    hosts = ("codex", "claude") if host == "both" else (host,)
    targets = [root / (".agents" if name == "codex" else ".claude") / "skills/breadth-first"
               for name in hosts]
    # Preflight all destinations before changing any of them.
    for target in targets:
        if target.is_symlink() and target.resolve() == SOURCE:
            continue
        if target.exists() or target.is_symlink():
            raise FileExistsError(f"Preserving existing installation: {target}")
    for target in targets:
        if not target.is_symlink():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to(SOURCE, target_is_directory=True)
        print(f"Installed: {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=("codex", "claude", "both"), default="both")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--project", type=Path, help="Project root")
    group.add_argument("--personal", action="store_true", help="Install under your home directory")
    args = parser.parse_args()
    try:
        install(Path.home() if args.personal else args.project.expanduser().resolve(), args.host)
    except OSError as exc:
        parser.exit(1, f"Installation failed: {exc}\n")


if __name__ == "__main__":
    main()
