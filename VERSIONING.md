# Version, release and pin policy

| Repository type | Authoritative source | Synchronized evidence |
| --- | --- | --- |
| CMake/Arduino library | `project(... VERSION ...)` | `library.properties`, public build-settings header, changelog, tag |
| Shared build infrastructure | `VERSION` | CMake metadata, changelog, tag |
| Agent guidance | `VERSION` | changelog and compatibility claims |
| Workspace portal | workspace manifests | Doxygen project number and release pins |

Workspace release pins are immutable tags in dependency order. A consumer can
accept a compatible range, but FetchContent and bootstrap installs must use a
tag. A dependency without a published tag must not be resolved from `main`.

`CHANGELOG.md` records released versions with dates; `Unreleased` is only for
changes after the latest tag. Release validation records builds, tests,
packages, documentation and embedded compile evidence separately from hardware
execution evidence.
