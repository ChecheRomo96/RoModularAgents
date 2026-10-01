# MIDILAR repository adapter

## Purpose

MIDILAR owns MIDI protocol data, parsing, routing, timing, transports and
devices. It is being rebuilt from scratch on the `rebuild` branch, following
its `ACTION_PLAN.md`, and merges into `main` once stable.

## Rules

- Preserve `Foundation <- MCC <- MIDILAR`. General utilities belong in
  Foundation, music theory in MCC, and signal processing in the future DSPCore
  library; only MIDI concepts belong in MIDILAR.
- Work on the `rebuild` branch, one approved `ACTION_PLAN.md` phase at a time.
  The removed legacy code is design input from the Git history, not code to
  restore.
- Treat presets and scripts as the supported build interface, with Bash and
  PowerShell parity. Treat the pinned `tools/RoModularBuild` as read-only.
- Real-time paths never allocate memory dynamically and never throw
  exceptions; value types are trivially copyable with compile-time size
  budgets.
- Keep the MIDI-domain specification ahead of the code, and keep public
  headers, examples, tests, version metadata, `ACTION_PLAN.md`, `CHANGELOG.md`
  and Doxygen synchronized.
- Separate compile/link validation from hardware execution evidence.

## Entry points

Use the matching PowerShell script on Windows:

```text
./scripts/configure.sh <preset> [--fresh] [-- <cmake-options>]
./scripts/build.sh <preset> [--fresh] [--config <configuration>] [--examples-on]
./scripts/test.sh <preset> [--fresh] [--config <configuration>]
./scripts/install.sh <preset>
./scripts/export.sh <preset> [--fresh] [--examples-on]
./scripts/test-package.sh <preset> [--fresh]
./scripts/test-arduino.sh [--fqbn <board>] [--foundation <dir>] [--mcc <dir>]
./scripts/analyze.sh <preset> [--fresh]
./scripts/docs.sh [--fresh]
```
