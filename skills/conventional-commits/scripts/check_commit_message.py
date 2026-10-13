#!/usr/bin/env python3
"""Check a commit message's first line against Conventional Commits.

Usage: check_commit_message.py "<first line>"
Prints "ok" and exits 0, or prints each problem and exits 1.
"""

import re
import sys

TYPES = ("feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert")
PATTERN = re.compile(r"^(?P<type>[a-z]+)(?:\((?P<scope>[a-z0-9-]+)\))?(?P<breaking>!)?: (?P<summary>.+)$")


def problems(line: str) -> list[str]:
    found = []
    match = PATTERN.match(line)
    if not match:
        return ['first line must look like "type(scope): summary"']
    if match["type"] not in TYPES:
        found.append(f'unknown type "{match["type"]}"; use one of: {", ".join(TYPES)}')
    summary = match["summary"]
    if summary[0].isupper():
        found.append("start the summary with a lowercase letter")
    if summary.endswith("."):
        found.append("drop the trailing period")
    if len(line) > 72:
        found.append(f"first line is {len(line)} characters; keep it to 72")
    return found


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    issues = problems(sys.argv[1].strip())
    for issue in issues:
        print(f"- {issue}")
    if not issues:
        print("ok")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
