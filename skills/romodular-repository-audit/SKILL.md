---
name: romodular-repository-audit
description: Audit a RoModular repository or the ecosystem and recommend what should happen next. Use for status reviews, architecture reviews, dependency boundaries, or backlog prioritization.
---

# RoModular repository audit

Read these canonical files when available:

1. `../../../RoModularAgents/CONTRACT.md`
2. The matching file under `../../../RoModularAgents/repositories/`
3. `../../../RoModularAgents/roles/architecture-auditor.md`
4. `../../../RoModularAgents/workflows/repository-audit.md`

Keep the audit read-only unless the user also asks for implementation. Ground
findings in current source, configuration, tests, packages, CI, and
documentation. Classify findings as blockers, risks, maintenance debt, or
future work, and recommend the smallest ordered next actions.

Do not treat proximity in a multi-repository workspace as permission to modify
sibling repositories.

