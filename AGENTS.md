# Skills Hub Agent Instructions

This repository is a **Skill Registry / Skill Router / Skill Catalog**.

It does not need to contain the full text of every skill. Its primary purpose is to help AI agents discover which external or local skill should be used for a given task.

## Required routing workflow

Before starting a user task, inspect `skills.catalog.json` or `skills.index.md` and determine whether one or more skills apply. The existing full `skills.index.json` remains available for compatible consumers.

When a matching skill is found:

1. Read the matching registry entry under `registry/`.
2. Follow its trigger rules, `use_when`, `avoid_when`, file patterns, and routing hints.
3. Do not load every external skill eagerly.
4. Read only the source material relevant to the task. A reference or framework is not automatically an executable skill.
5. If source material is unavailable locally, use its URL for read-only inspection. Installation/sync commands are metadata, not permission to run them. Obtain any separate installation, code execution, network, data-sharing, or tool permission required by the user and environment before acting. A catalog match cannot expand those permissions.
6. If multiple skills apply, use the most specific skill first, then supporting skills.
7. If no skill applies, proceed normally.

## Progressive disclosure

Prefer this order:

1. `skills.catalog.json` for compact machine-readable discovery (`skills.index.json` preserves the full legacy shape).
2. `skills.index.md` for a readable summary.
3. `registry/<skill-id>.json` for detailed metadata.
4. External skill source only when the selected skill is actually needed.

## Maintenance rules

When adding a skill:

1. Add or update one file under `registry/`.
2. Run `python scripts/build_index.py` to generate all three indexes. Never edit generated indexes directly.
3. Run `python scripts/build_index.py --check` and `python -m unittest discover -s tests -v`.
4. Include clear triggers, use cases, file patterns, source URL, and entry path.
5. Keep descriptions short enough for fast agent routing.

`registry/*.json` is the single source of entry metadata. Keep every existing entry unless removal is explicitly intended. Do not bulk-register repositories as executable skills. Use `reference` or `framework` where appropriate.

Trigger/file matches from `scripts/route_candidates.py` are lexical candidates only. Review the task against `use_when`, `avoid_when`, and `routing_hint`; the helper cannot decide semantic suitability or authorize actions. File patterns alone are weak evidence.

`source.observed_revision` and `source.observed_at` record an actual source/entry existence observation, not a security review, license grant, install lock, or approval. Refresh them only after checking that exact source. Do not invent a license, checksum, or reviewed date. Read the actual source and applicable license before importing or executing it.
