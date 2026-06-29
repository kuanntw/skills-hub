# Skills Hub Agent Instructions

This repository is a **Skill Registry / Skill Router / Skill Catalog**.

It does not need to contain the full text of every skill. Its primary purpose is to help AI agents discover which external or local skill should be used for a given task.

## Required routing workflow

Before starting a user task, inspect `skills.index.md` or `skills.index.json` and determine whether one or more skills apply.

When a matching skill is found:

1. Read the matching registry entry under `registry/`.
2. Follow its trigger rules, `use_when`, `avoid_when`, file patterns, and routing hints.
3. Do not load every external skill eagerly.
4. Load or install only the skill packages that are relevant to the current task.
5. If the full skill package is not available locally, use the registry entry's source URL and install/sync instructions.
6. If multiple skills apply, use the most specific skill first, then supporting skills.
7. If no skill applies, proceed normally.

## Progressive disclosure

Prefer this order:

1. `skills.index.json` for machine-readable routing.
2. `skills.index.md` for a readable summary.
3. `registry/<skill-id>.json` for detailed metadata.
4. External skill source only when the selected skill is actually needed.

## Maintenance rules

When adding a skill:

1. Add or update one file under `registry/`.
2. Add the skill to `skills.index.json`.
3. Add the skill to `skills.index.md`.
4. Include clear triggers, use cases, file patterns, source URL, and entry path.
5. Keep descriptions short enough for fast agent routing.
