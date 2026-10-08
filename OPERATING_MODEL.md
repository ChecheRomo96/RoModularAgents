# RoModular coordinated development model

## Goal

RoModular development is organized as a small, provider-neutral delivery team:
the user speaks to one ecosystem coordinator, and each repository needing work
receives a bounded repository-developer assignment. This makes ownership,
dependencies, validation, and the final report explicit without requiring a
particular AI product or multi-agent runtime.

## Roles in every delivery

| Role | Accountability | Default authority |
| --- | --- | --- |
| User | Objective, scope, priorities, and material design decisions | Approves expanded scope and publication actions |
| Ecosystem coordinator | Plan, sequencing, integration review, and consolidated report | Read-only coordination unless separately assigned repository work |
| Repository developer | Implementation and validation for one named repository | Only its explicit repository assignment |

The available developer seats correspond to the ecosystem repositories:
`RoModular`, `RoModularAgents`, `RoModularBuild`, `CPSTL`, `Foundation`,
`DspCore`, `MCC`, and `MIDILAR`. A seat is activated only when that repository
is in scope. There is no standing permission to modify all repositories.

When a repository is added to the workspace, add its repository adapter before
activating its developer seat. This keeps every assignment grounded in the
repository that owns the behavior.

Specialist roles such as architecture auditor, documentation curator, and
release auditor remain available for focused work. They advise or validate;
they do not replace a repository developer's ownership.

## How to use it

Begin a request with the desired outcome and, when known, the repositories in
scope. For example:

```text
Coordinate this delivery: add <capability>. Scope: Foundation and DspCore.
Success means <observable result>. Do not publish or change MIDILAR.
```

The coordinator returns a delivery brief and assignments, then reports only
when there is a milestone, blocker, or final result. A request involving one
repository still benefits from the same pattern: the coordinator may create a
single developer assignment and return one verified report.

Use the `romodular-coordinate-development` skill to load the protocol. The
full workflow, handoff format, and runtime-neutral execution rules live in
[workflows/coordinated-development.md](workflows/coordinated-development.md).

## Runtime mapping

The model defines responsibilities, not vendor mechanics. A compatible runtime
may use parallel agents, separate conversations, sequential role passes, or a
human coordinator. In every case it must preserve repository scope, explicit
handoffs, validation evidence, and user authorization. Codex and Claude Code
are supported consumers of the canonical skills; neither is the protocol's
owner.
