# Skills Hub

Skills Hub is a lightweight registry, router, and catalog for reusable AI skills.

The goal is **not** to copy every skill package into this repository. Instead, this hub tells AI agents:

- what skills are available,
- what each skill is useful for,
- which keywords, situations, and file patterns should trigger a skill,
- where the full skill package lives,
- and how to install or sync the skill when it is not available locally.

## How agents should use this repository

1. Read [`AGENTS.md`](./AGENTS.md) for routing behavior.
2. Inspect [`skills.catalog.json`](./skills.catalog.json) or [`skills.index.md`](./skills.index.md) before starting a task. [`skills.index.json`](./skills.index.json) preserves the original full JSON shape for existing consumers.
3. Select only the skills that match the current task.
4. Open the matching file under [`registry/`](./registry/) for detailed routing metadata.
5. Read only relevant external material. Reading a registry entry does not authorize installation, execution, uploads, or expanded tools. Installation commands are informational and never executed by this hub's helpers.

## Registry types

| Type | Meaning |
|---|---|
| `skill-package` | A skill package with a documented entry point; inspect its compatibility before loading. |
| `skill-kit` | A collection of related skill modules, usually with its own index. |
| `reference` | A specification or reference document for skill systems. |
| `framework` | A methodology or workflow collection that can inform AI work but is not necessarily a direct skill package. |

## Current catalog

See [`skills.index.md`](./skills.index.md) for the human-readable catalog and [`skills.index.json`](./skills.index.json) for the machine-readable index.

## Maintain the catalog

Python 3.10+ is required for the maintenance helpers. Use your approved development environment; these dependencies are not installed into skill consumers or Laravel applications.

```sh
python -m pip install -r requirements-dev.txt
python scripts/build_index.py
python scripts/build_index.py --check
python -m unittest discover -s tests -v
```

- Edit only `registry/*.json` for entry metadata. The generator validates [`schemas/registry.schema.json`](./schemas/registry.schema.json), sorts entries by filename, and writes deterministic JSON/Markdown indexes without timestamps or network access.
- `--check` is read-only and fails on invalid entries, missing/escaping local entry paths, or stale generated files. CI runs the same checks and routing regression cases.
- The full index retains `schema_version: 0.1.0` and all existing entry fields. The compact catalog is an additive opt-in discovery surface, not a breaking replacement.
- All 10 original entries remain. The five NDF Chinese triggers previously present only in the full index now live in the registry as well.

## Explain routing candidates

```sh
python scripts/route_candidates.py '國發基金的估值與投委會審查'
python scripts/route_candidates.py 'Laravel authorization' --file app/Models/User.php --task-type testing
```

This offline helper reports matched triggers, paths, and task types together with `use_when` / `avoid_when`. It is a lexical candidate finder, not an autonomous installer or a semantic agent evaluation. Broad file matches require context review; adjacent-domain negative cases test token boundaries, not every possible ambiguity. Framework and reference classifications are preserved.

## Source observations and trust

On 2026-10-25, all 10 source entries (including the Playwright `skills/` directory) were checked at the exact commit recorded as `source.observed_revision`. `source.observed_at` is the observation date. Open a snapshot as `SOURCE_URL/blob/OBSERVED_REVISION/ENTRY` (use `tree` for directories).

These observations are not a package lockfile, a security audit, a statement of standard compliance, or permission to install/update/run. They do not assert the source is still current. License and package hashes are intentionally absent when not established. Before importing source material, verify its applicable license and notices; before execution, inspect the relevant files and honor the user's/environment's permissions. No third-party skill code is copied or executed by the catalog maintenance checks.

## Revision History

### 2026-10-25

- Made `registry/*.json` the single editable source and added schema validation, deterministic index generation, read-only drift checks, and CI.
- Preserved the 10 existing entries and legacy full JSON interface; added a compact discovery catalog and restored the five missing NDF Chinese triggers.
- Recorded verified source commit/entry observations without inventing licenses, hashes, security-review claims, or installation approval.
- Added an offline lexical candidate helper and positive/negative routing fixtures, with explicit read/install/run boundaries.
- Validation: 14 Python unit tests (including schema rejection and routing subcases), index `--check`, Python compilation, and `git diff --check` passed locally. All 10 remote source entry paths were checked at the recorded commits. External skill execution, semantic agent evaluation, and application/runtime testing were not performed; CI status is reported separately on the PR.
