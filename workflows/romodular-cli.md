# RoModular CLI orchestration contract

## Purpose

`romodular` is a host-side workspace orchestrator. It discovers the
repositories in a RoModular checkout, reports their state, and delegates
repository work to each repository's documented scripts and CMake presets. It
does not replace RoModularBuild, own a microcontroller SDK, or implement a
second build/test/package system.

The CLI runs on a developer host. Firmware images (`.elf`, `.hex`, `.bin`,
and equivalent formats) remain artifacts of a consumer repository's target,
toolchain, linker, startup code, and board profile.

## Initial command contract

| Command | Default behavior | May change state |
| --- | --- | --- |
| `romodular doctor` | Inspect the workspace layout, required repositories, Git availability, configured remotes, submodule state, and host tools reported by repository capabilities. | No |
| `romodular status` | Report repository branch, cleanliness, local relation to its configured upstream, version evidence, release pins, and dependency order. | No |
| `romodular sync --dry-run` | Show the exact safe fast-forward updates that would be attempted after fetching configured remotes. | No |

The first release must require `--dry-run` for `sync`; it must not provide an
implicit mutating synchronization command. A later `sync --apply` requires a
separate, documented safety contract and explicit user invocation.

All commands default to the current workspace, or accept an explicit
`--workspace <path>`. They fail with a clear diagnostic when invoked outside a
workspace or when a required repository is missing. A check that cannot be
performed, such as an unavailable network remote, is reported as unavailable
rather than silently treated as current.

## Delegation boundary

For build, test, documentation, package, flash, and hardware operations, the
CLI must discover a repository capability and invoke its supported wrapper or
CMake preset. It may pass through documented arguments and expose the command
that it will run, but it must not duplicate configuration flags, toolchain
files, platform SDK selection, artifact naming, or test policy.

```text
romodular build <repository> <preset>
        -> repository-supported configure/build/test wrapper or preset
        -> RoModularBuild mechanics where that repository uses them
        -> repository-owned host or embedded artifact
```

Board and MCU support belongs to consumer-project profiles. A profile owns the
toolchain, CPU/FPU/ABI settings, linker script, startup code, SDK or HAL,
flashing procedure, and hardware evidence. CPSTL remains a portable
freestanding library; it must not gain MCU-family-specific behavior merely for
CLI discovery.

## Safety and output rules

- Every command states the workspace path and repository set it inspected.
- Read-only commands never run configure, build, test, documentation, flash,
  install, Git checkout, merge, reset, clean, commit, tag, push, or publish.
- A proposed mutating command prints an execution plan before making changes
  and refuses dirty repositories unless its repository-specific contract
  explicitly supports the operation.
- The CLI never converts a remote tracking ref into proof that GitHub or any
  other server is reachable. It labels local-ref and freshly-fetched evidence
  distinctly.
- Human-readable output is the default. A stable machine-readable format may
  be added only with a versioned schema.

## Workspace evidence

The initial implementation reads the workspace manifest, release pins, and
dependency graph owned by RoModular; it does not recreate those facts in a
second manifest. RoModularAgents' `scripts/inspect-workspace.py` remains the
canonical read-only structural baseline until the CLI is implemented. CLI
output should preserve the dependency order:

```text
CPSTL <- Foundation <- (DspCore, MCC) <- MIDILAR
```

## Acceptance criteria for the first implementation

1. `doctor`, `status`, and `sync --dry-run` operate without modifying the
   workspace or invoking a repository build.
2. Their behavior is verified against a clean workspace, a dirty repository,
   a detached or missing upstream, a missing repository, and an unavailable
   remote.
3. `status` identifies whether each result derives from local refs or a
   successful fetch.
4. The command contract is exercised on macOS, Linux, and Windows using the
   repository-supported shell and PowerShell entry points.
5. Any future build or target command proves delegation by testing an existing
   repository script or preset rather than reimplementing its logic.
