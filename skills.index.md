# Skills Hub Index

This repository is a routing index for reusable AI skills. It helps agents decide which skill to use without eagerly loading every skill package.

## Routing policy

1. Inspect this file or `skills.index.json` before starting a task.
2. Match the user request against skill descriptions, triggers, task types, and file patterns.
3. Read the matching file under `registry/`.
4. Load or install the external skill package only when the selected skill is relevant.
5. If multiple skills apply, use the most specific skill first.

## Available skills

| Skill | Type | Use when | Source |
|---|---|---|---|
| `docx-template` | `skill-package` | Generating company-style Word / DOCX documents from Markdown, plain text, or JSON. | <https://github.com/kuanntw/word-skills> |
| `human-tone-zh` | `skill-package` | Rewriting Traditional Chinese text to sound more natural, human, and less AI-like. | <https://github.com/kuanntw/human-tone-skills> |
| `karpathy-guidelines` | `skill-package` | Planning, implementing, or reviewing simple, surgical, verifiable code changes. | <https://github.com/kuanntw/andrej-karpathy-skills> |
| `laravel-vibe` | `skill-kit` | Building or reviewing Laravel APIs, Livewire components, multilingual features, tests, releases, and app architecture. | <https://github.com/kuanntw/laravel-skills> |
| `logo-skills` | `skill-package` | Creating, reviewing, refining, or packaging logos and brand identity deliverables. | <https://github.com/kuanntw/logo-skills> |
| `playwright-readonly` | `skill-kit` | Writing or running safe read-only Playwright browser regression tests and UI checks. | <https://github.com/kuanntw/playwright-skills> |
| `skills-spec` | `reference` | Designing or validating skill package structure, metadata, schema, or registry behavior. | <https://github.com/kuanntw/skills-spec> |
| `ui-ux-web-guidelines` | `skill-package` | Designing or reviewing web UI, UX, responsive layout, forms, helper text, and accessibility. | <https://github.com/kuanntw/ui-ux-skills> |
| `vibe-coding-skills` | `framework` | Structuring AI-assisted coding workflows, context, atomic tasks, memory, and collaboration patterns. | <https://github.com/kuanntw/vibe-coding-skills> |

## Laravel Vibe subskills

The `laravel-vibe` kit includes these subskills:

- `project-framing`
- `static-assets-and-external-resources`
- `feature-architecture`
- `api-design`
- `livewire-component-architecture`
- `livewire-forms-and-tables`
- `livewire-testing`
- `livewire-performance-and-pitfalls`
- `multilingual-strategy`
- `tenant-translation-override`
- `data-and-eloquent`
- `testing-and-quality`
- `spec-consistency-and-coverage`
- `release-and-observability`
- `operation-manual`
- `ai-collaboration-playbook`

## Playwright Read-Only subskills

The `playwright-readonly` kit includes these subskills:

- `readonly-core`
- `readonly-adapters/template`

## Skill type guide

| Type | Meaning |
|---|---|
| `skill-package` | A directly usable skill package with a specific entry point such as `SKILL.md`. |
| `skill-kit` | A collection of related skill modules, usually with its own index. |
| `reference` | A specification or reference document for skill systems. |
| `framework` | A methodology or workflow collection that can inform AI work but is not necessarily a direct skill package. |
