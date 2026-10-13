---
name: conventional-commits
description: Writes a git commit message in the Conventional Commits format (type(scope): summary, body, footers) from the staged changes. Use when the user asks for a commit message, wants to commit their work, or mentions conventional commits.
license: MIT
---

# Conventional Commits

Write one commit message for the changes that are staged right now.

## Steps

1. Read what's staged with `git diff --cached --stat` and `git diff --cached`. If nothing is staged, say so and stop; don't stage files yourself.
2. Pick the **type** from [reference.md](reference.md). Use the one that describes the main intent of the change, not every file touched.
3. Pick an optional **scope**: the area of the codebase in one short lowercase word (for example `api`, `store`, `docs`).
4. Write the **summary**: imperative mood ("add", not "added"), lowercase start, no trailing period, at most 72 characters for the whole first line.
5. Add a **body** only when the why isn't obvious from the summary. Wrap it at 72 characters.
6. Add **footers** for breaking changes (`BREAKING CHANGE: ...`) or issue references (`Refs #123`).
7. Check the first line with `python3 scripts/check_commit_message.py "<first line>"` and fix anything it reports.

Show the message in a code block and ask before running `git commit`.

## Example

```
fix(store): keep reviewed GitHub imports in the Official list

Approved imports install from GitHub, so their source is "community";
the Official list dropped them and they showed in neither group.

Refs #300
```
