# RoModularAgents repository adapter

## Purpose

RoModularAgents owns the provider-neutral operating contract, repository
adapters, bounded roles, repeatable workflows, and Agent Skills used across
the RoModular ecosystem.

## Rules

- Keep policy and task workflows provider-neutral. Provider discovery belongs
  in `workspace/` or in the RoModular bootstrap adapters.
- Keep each skill compatible with the open `SKILL.md` format used by Codex and
  Claude Code.
- Put repository-specific ownership and entry points under `repositories/`;
  do not move product or build policy into the global contract.
- Treat installed workspace skills as generated copies. Change only the
  canonical bundles under `skills/`.
- Keep role authority bounded. Roles and skills never grant permission to
  modify additional repositories or perform publication actions.
- Synchronize `VERSION`, release notes, and compatibility documentation when
  publishing a new contract version.

## Validation

Run:

```text
python3 scripts/validate.py
```

RoModular owns the separate macOS and Windows integration test that installs
these templates and skills into a temporary workspace.
