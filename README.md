# RoModularAgents

RoModularAgents is the provider-neutral source of AI-assisted engineering
guidance for the RoModular ecosystem. It keeps the shared contract, bounded
roles, repository adapters, repeatable workflows, and Agent Skills used by
Codex, Claude Code, and compatible runtimes.

The repository separates three kinds of instruction:

- `CONTRACT.md` contains rules that always apply.
- `repositories/` describes repository-specific ownership and supported entry
  points.
- `skills/` contains task-specific workflows that load only when relevant.

The standard `RoModularWorkspace` bootstrap installs the same `SKILL.md`
bundles into the workspace-level Codex and Claude discovery directories. The
canonical source remains this repository; generated workspace copies should
not be edited directly.

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
