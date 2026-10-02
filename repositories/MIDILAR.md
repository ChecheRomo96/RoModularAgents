# MIDILAR repository adapter

## Purpose

MIDILAR owns MIDI protocol data, wire-format translation (MIDI 1.0 bytes, USB
MIDI 1.0 events, UMP), timing and devices. It was rebuilt from scratch and
released as 0.2.0 on `main`; its `ACTION_PLAN.md` lists the remaining phases
(MIDI-CI is deferred).

## Rules

- Preserve `Foundation <- MCC <- MIDILAR`. General utilities belong in
  Foundation, music theory in MCC, and signal processing in DspCore; only MIDI
  concepts belong in MIDILAR. Hardware transports (UART, USB stacks, desktop
  MIDI APIs) are separate libraries built on MIDILAR's translations.
- Work on `main`, one approved `ACTION_PLAN.md` phase at a time. The removed
  legacy code is design input from the Git history, not code to restore.
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
