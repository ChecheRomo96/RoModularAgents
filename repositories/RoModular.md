# RoModular repository adapter

## Purpose

RoModular is the ecosystem documentation portal and workspace orchestrator. It
describes repository ownership, maturity, dependencies, governance, and entry
points without absorbing product code or shared build engines.

## Rules

- Keep ecosystem documentation grounded in the repositories that own the
  described behavior.
- Preserve Doxygen group hierarchy, rendered navigation, and GitHub Pages
  deployment.
- Keep the workspace repository manifest and bootstrap scripts cross-platform.
- RoModular owns workspace composition, not the shared agent contract or
  reusable engineering skills; those belong in RoModularAgents.
- RoModularBuild owns generic build mechanics. CPSTL, Foundation, DspCore,
  MCC, and MIDILAR own their source, tests, examples, packages, and release
  policy.
- Treat planned repositories or capabilities explicitly as planned.

## Validation

Rebuild Doxygen without warnings after documentation changes. Validate both
shell and PowerShell bootstrap behavior when their shared contract changes.

