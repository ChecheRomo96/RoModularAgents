# RoModularAgents

RoModularAgents is the provider-neutral source of AI-assisted engineering
guidance for the RoModular ecosystem. It keeps the shared contract, bounded
roles, repository adapters, repeatable workflows, and Agent Skills used by
Codex, Claude Code, and compatible runtimes.

The repository separates four kinds of instruction:

- `CONTRACT.md` contains rules that always apply.
- `repositories/` describes repository-specific ownership and supported entry
  points.
- `skills/` contains task-specific workflows that load only when relevant.
- `roles/` and `workflows/` define the provider-neutral coordinated
  development model.

## Coordinated development

`OPERATING_MODEL.md` defines the default delivery team: one ecosystem
coordinator as the user-facing point of contact and one bounded developer
assignment for each repository that is actually in scope. The coordinator
plans and reviews handoffs; it does not receive blanket authority to edit all
repositories. The `romodular-coordinate-development` skill loads the complete
workflow, handoff format, and provider-neutral runtime rules.

Use it by stating the outcome, success criteria, repositories in scope, and
constraints. The coordinator returns a scoped plan, then a consolidated report
with validation evidence, risks, and only the decisions that need the user.

The standard `RoModularWorkspace` bootstrap installs the same `SKILL.md`
bundles into the workspace-level Codex and Claude discovery directories. The
canonical source remains this repository; generated workspace copies should
not be edited directly.

Version ownership, release evidence and workspace pins are defined in
[VERSIONING.md](VERSIONING.md). `scripts/inspect-workspace.py <repos-root>`
performs the common read-only structural inspection.

The future host-side `romodular` orchestrator is defined by the
[CLI orchestration contract](workflows/romodular-cli.md). Its first commands
are read-only workspace inspection (`doctor`, `status`, and `sync --dry-run`)
and it delegates all build and target work to repository-owned entry points.

Repository-local `AGENTS.md` files route an agent to this repository when it is
available and retain enough local guidance to remain safe and useful in a
standalone checkout.

## Validation

Run `python3 scripts/validate.py` to verify the repository adapters, skill
front matter, canonical references, required workspace templates, and text
hygiene. RoModular separately exercises workspace installation on macOS and
Windows.

## License

All rights are reserved. Viewing the repository does not grant permission to
use, copy, modify, or distribute it. See [LICENSE](LICENSE).
