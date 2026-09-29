---
name: romodular-release-readiness
description: Determine whether a RoModular repository is ready for a release. Use for version, API, CI, package, documentation, artifact, and platform-readiness audits.
---

# Audit RoModular release readiness

Read these canonical files when available:

1. `../../../RoModularAgents/CONTRACT.md`
2. The matching file under `../../../RoModularAgents/repositories/`
3. `../../../RoModularAgents/roles/release-auditor.md`
4. `../../../RoModularAgents/workflows/release.md`

Audit the intended version and branch without changing release state. Verify
metadata, public API changes, changelog, licensing, generated documentation,
supported builds and tests, installation, downstream package consumption, CI,
and package contents. Record compile-only embedded validation separately from
hardware execution.

Return `ready`, `conditionally ready`, or `not ready` with explicit evidence
and unresolved blockers. Publishing requires separate user authorization.

