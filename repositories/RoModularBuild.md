# RoModularBuild repository adapter

## Purpose

RoModularBuild is project-independent build infrastructure. Keep it reusable
by Foundation, MCC, and future consumers without importing product policy.

## Rules

- Preserve the one-way dependency from consumers to RoModularBuild.
- Treat `VERSION` as the authoritative version and synchronize contracts,
  changelog, tags, and compatibility claims.
- Keep shared presets hidden with the `romodular_` prefix and shared cache
  variables under `ROMODULAR_`.
- Keep public presets, feature defaults, packaging, releases, firmware, linker
  scripts, SDK integration, flashing, and hardware evidence in consumers.
- Preserve Bash and PowerShell workflow parity.
- Treat `actions/` as reusable CI primitives, not complete consumer workflows.
- Consumers pin tagged revisions; never move a consumer gitlink incidentally.

## Validation

Use `./scripts/validate.sh` or `.\scripts\validate.ps1`. State when Windows,
PowerShell, a cross-compiler, or consumer validation was unavailable.

