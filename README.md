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
2. Inspect [`skills.index.md`](./skills.index.md) or [`skills.index.json`](./skills.index.json) before starting a task.
3. Select only the skills that match the current task.
4. Open the matching file under [`registry/`](./registry/) for detailed routing metadata.
5. Load the external skill package only when the registry entry indicates it is needed.

## Registry types

| Type | Meaning |
|---|---|
| `skill-package` | A directly usable skill package with a specific entry point such as `SKILL.md`. |
| `skill-kit` | A collection of related skill modules, usually with its own index. |
| `reference` | A specification or reference document for skill systems. |
| `framework` | A methodology or workflow collection that can inform AI work but is not necessarily a direct skill package. |

## Current catalog

See [`skills.index.md`](./skills.index.md) for the human-readable catalog and [`skills.index.json`](./skills.index.json) for the machine-readable index.
