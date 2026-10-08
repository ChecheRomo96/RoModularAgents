# RoModular workspace instructions

This directory is a multi-repository RoModular workspace.

Before working in any repository:

1. Read `RoModularAgents/CONTRACT.md` completely.
2. Identify only the repositories explicitly placed in scope by the user.
3. Read the matching adapter under `RoModularAgents/repositories/`.
4. Read the root `AGENTS.md` of every repository in scope when it exists.
5. Use the relevant installed RoModular skill for repeatable workflows.

The expected repositories are:

- `RoModular`: ecosystem documentation and workspace orchestration.
- `RoModularAgents`: provider-neutral contracts, adapters, and skills.
- `RoModularBuild`: reusable build infrastructure.
- `CPSTL`: portable `std` vocabulary (Cross-Platform STL); bottom of the
  dependency chain.
- `Foundation`: low-level portable C++ library.
- `DspCore`: portable signal-processing library.
- `MCC`: Music Composition Core.
- `MIDILAR`: MIDI protocol data, wire-format translation, timing and devices.

Dependencies point down the chain
`CPSTL <- Foundation <- (DspCore, MCC) <- MIDILAR`.

Repository proximity does not grant cross-repository authority. Preserve
unrelated changes and do not modify a sibling repository unless the user
explicitly includes it in the current request.

Files installed under `.codex/skills/` and `.claude/skills/` are generated
workspace copies. Edit their canonical sources under `RoModularAgents/skills/`
and rerun the workspace bootstrap.
