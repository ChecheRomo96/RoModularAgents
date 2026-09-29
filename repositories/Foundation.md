# Foundation repository adapter

## Purpose

Foundation is the low-level portable C++ library of RoModular. Keep it
independently buildable for desktop and embedded consumers.

## Rules

- Treat presets and scripts as the supported build interface.
- Treat `tools/RoModularBuild` as a pinned read-only dependency. Shared engine
  changes belong in RoModularBuild; a gitlink update is a separate change.
- Preserve C++17 for CMake and direct source builds. Arduino source builds
  intentionally support C++11 when `ARDUINO` is defined.
- Keep embedded paths free from mandatory exceptions and full-STL assumptions.
  Do not disable heap use merely because a target is embedded.
- Preserve module selection through existing cache options.
- Export one Release library and CMake package; Debug is not distributed.
- Examples demonstrate public APIs. GoogleTest unit tests live under
  `tests/Foundation/` and run through CTest integration.
- Synchronize public headers, examples, tests, version metadata,
  `CHANGELOG.md`, and Doxygen after public API changes.
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
./scripts/validate-package.sh <preset>
./scripts/validate-examples.sh <preset> [--fresh]
./scripts/test-arduino.sh [--fqbn <board>]
./scripts/test-stm32.sh <preset> [--fresh]
./scripts/docs.sh [--fresh]
```

