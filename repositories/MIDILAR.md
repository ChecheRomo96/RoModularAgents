# MIDILAR repository adapter

## Purpose

MIDILAR owns MIDI protocol, transport, routing, device, and real-time
music-technology concerns. The current repository is legacy code pending a
deliberate reconstruction.

## Rules

- Preserve `Foundation <- MCC <- MIDILAR`. General utilities belong in
  Foundation and music-theory concepts belong in MCC.
- Treat source, examples, tests, CMake files, and documentation as migration
  evidence. Do not broadly rewrite or delete them before understanding their
  behavior and replacement destination.
- MIDILAR has not adopted RoModularBuild. Do not introduce a partial migration
  without an explicit task and validation plan.
- Preserve the current C++17 requirement until compatibility is documented and
  tested.
- Keep real-time and embedded paths allocation-conscious, exception-free where
  the target requires it, and free from mandatory full-STL assumptions.
- Keep Arduino and desktop examples aligned around shared public API examples;
  tests remain under `tests/`.
- Verify legacy documentation and package claims against implementation.
- `CMakeCache.txt` is currently tracked. Its removal is a deliberate cleanup,
  not incidental generated-file deletion.

## Current entry points

```text
cmake -B build -S . -DMIDILAR_TESTING=ON -DMIDILAR_EXAMPLES=ON
cmake --build build
ctest --test-dir build
```

The current presets are legacy convenience configurations, not yet a
RoModularBuild compatibility contract.

