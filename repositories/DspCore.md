# DspCore repository adapter

## Purpose

DspCore is the portable signal-processing library. Preserve the dependency
direction `Foundation <- DspCore <- MIDILAR` and keep it independently
buildable for desktop and embedded consumers. CPSTL is below
Foundation (`CPSTL <- Foundation <- (DspCore, MCC) <- MIDILAR`); DspCore
reaches it only through Foundation.

## Rules

- Treat presets and scripts as the supported build interface.
- Initialize the pinned `tools/RoModularBuild` submodule in fresh checkouts.
- Treat RoModularBuild as read-only while working in DspCore.
- Preserve C++17 and keep embedded code exception-free and independent of
  mandatory full-STL facilities. Operations that change a container's size
  may allocate; libraries make no real-time assumptions about the caller, and
  implementers reserve space beforehand for time-critical code. Allocation
  failure is reported through results.
- Keep MIDI concepts in MIDILAR and music theory in MCC; only signal
  processing belongs in DspCore.
- Follow `ACTION_PLAN.md` phase by phase; each phase needs the user's
  approval.
- Preserve module selection through `DSPCORE_*` cache options.
- Export one Release library and CMake package; Debug is not distributed.
- Examples demonstrate public APIs. GoogleTest unit tests live under
  `tests/DspCore/` and run through CTest integration.
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
./scripts/test-arduino.sh [--fqbn <board>] [--foundation <dir>]
./scripts/docs.sh [--fresh]
```
