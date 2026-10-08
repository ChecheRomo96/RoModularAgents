# MCC repository adapter

## Purpose

MCC is the portable music-theory library. Preserve the dependency direction
`Foundation <- MCC <- MIDILAR` and keep it independently buildable for desktop
and embedded consumers. CPSTL is below Foundation
(`CPSTL <- Foundation <- (DspCore, MCC) <- MIDILAR`); MCC reaches it only
through Foundation.

## Rules

- Treat presets and scripts as the supported build interface.
- Initialize the pinned `tools/RoModularBuild` submodule in fresh checkouts.
- Treat RoModularBuild as read-only while working in MCC.
- Preserve C++17 and keep embedded code exception-free and independent of
  mandatory full-STL facilities. Operations that change a container's size
  may allocate; libraries make no real-time assumptions about the caller, and
  implementers reserve space beforehand for time-critical code. Allocation
  failure is reported through results.
- Keep musical invariants aligned with
  `docs/Topics/Specification/MusicDomain.dox` and `ACTION_PLAN.md`.
- Preserve module selection through `MCC_*` cache options.
- Export one Release library and CMake package; Debug is not distributed.
- Examples demonstrate public APIs. GoogleTest unit tests live under
  `tests/MCC/` and run through CTest integration.
- Synchronize public headers, examples, tests, version metadata, action plan,
  and Doxygen after public API changes.
- Separate compile/link validation from hardware execution evidence.

## Entry points

Use the matching PowerShell script on Windows:

```text
./scripts/configure.sh <preset> [--fresh] [-- <cmake-options>]
./scripts/build.sh <preset> [--fresh] [--config <configuration>]
./scripts/test.sh <preset> [--fresh] [--config <configuration>]
./scripts/install.sh <preset>
./scripts/export.sh <preset> [--fresh] [-- <cmake-options>]
./scripts/test-package.sh <preset> [--fresh]
./scripts/docs.sh [--fresh]
```
