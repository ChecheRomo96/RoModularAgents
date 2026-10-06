# CPSTL repository adapter

## Purpose

CPSTL (Cross-Platform STL) is the portable `std` vocabulary of RoModular:
`cpstd::vector`, `string`, `stack`, `queue`, `function`, `unique_ptr`, type
traits, iterators, algorithms and `numeric_limits` with the `std` interface on
targets with or without a C++ standard library. It is the bottom of the
dependency chain `CPSTL <- Foundation <- (DspCore, MCC) <- MIDILAR` and
depends on no other RoModular library; Foundation is planned to build on it
instead of reimplementing `std` types. Keep it independently buildable for
desktop and embedded consumers.

## Rules

- Treat `CMakePresets.json`, its included preset files and the scripts as the
  supported build interface. Initialize the pinned `tools/RoModularBuild`
  submodule in fresh checkouts and treat it as read-only.
- Keep the library C++11-compatible: Arduino cores compile it as C++11. The
  GoogleTest suites need C++17; `tests/HeaderCheck.cpp` and the examples cover
  the configured standard.
- With `CPSTL_USING_STL` every `cpstd` name is an alias of its `std`
  counterpart (`template <...> using vector = std::vector<...>`), at no cost.
  Otherwise, and always on AVR, CPSTL provides its own implementation using
  only freestanding C headers. Every public behaviour must hold in both
  modes; tests that apply only to the CPSTL implementation are guarded with
  `#if !defined(CPSTL_USING_STL)`.
- Containers never throw. Operations that change a container's size may
  allocate; in the CPSTL implementation an allocation failure leaves the
  container unchanged. Callers reserve space beforehand for time-critical
  code. Do not add exceptions or `try_` extensions.
- Preserve module and configuration selection through the `CPSTL_*` cache
  options (`CPSTL_USING_STL`, `CPSTL_ALLOCATION`, `CPSTL_VECTOR`,
  `CPSTL_STRING`, `CPSTL_STACK`, `CPSTL_QUEUE`, `CPSTL_CXX_STANDARD`) and their
  `src/CPSTL_UserSetup.h` equivalents for IDE builds.
- Keep public headers, examples, tests, `CHANGELOG.md`, `README.md` and the
  version in `CMakeLists.txt`, `library.properties` and
  `src/CPSTL_BuildSettings.h` synchronized.
- A change to a `cpstd` interface affects every RoModular library above it;
  report such changes to the user before making them.
- Separate compile/link validation from hardware or simulator execution
  evidence.

## Entry points

Use the matching PowerShell script on Windows (`test-arduino` is Bash only):

```text
./scripts/configure.sh <preset> [--fresh] [-- <cmake-options>]
./scripts/build.sh <preset> [--fresh] [--config <configuration>] [--examples-on]
./scripts/test.sh <preset> [--fresh] [--config <configuration>]
./scripts/install.sh <preset>
./scripts/clean.sh <preset> [--dist]
./scripts/test-arduino.sh [--fqbn <board>]... [-- <arduino-cli options>]
```

Presets: `linux_gcc_x64`, `linux_clang_x64`, `linux_gcc_arm64`,
`linux_clang_arm64`, `macos_arm64`, `macos_x64`, `windows_msvc_x64`,
`windows_clang_x64` and `atmega328p_avrgcc_avr5`, which builds the library and
the self-checking `CPSTLAvrSmoke` firmware (run its `.hex` under simavr and
look for `CPSTL AVR smoke: PASS`). Validate the C, CPP and STD allocation
modes, `-DCPSTL_USING_STL=ON`, and C++11 through C++20 through
`-DCPSTL_CXX_STANDARD=`.
