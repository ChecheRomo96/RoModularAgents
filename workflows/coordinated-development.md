# Coordinated development workflow

Use this workflow when a request may involve more than one RoModular
repository, needs ongoing coordination, or when the user asks for a clear
development operating model.

## Team topology

The coordinator is the sole default interface to the user. A developer is an
instance of the repository-developer role, not a new permanent account. Start
only the instances needed by the current request.

```text
User
  |
  v
Ecosystem coordinator
  |-- RoModular developer
  |-- RoModularAgents developer
  |-- RoModularBuild developer
  |-- CPSTL developer
  |-- Foundation developer
  |-- DspCore developer
  |-- MCC developer
  `-- MIDILAR developer
```

The repository adapters remain the authority for ownership and supported
entry points. The coordinator and developer roles add routing and reporting;
they do not replace those adapters.

## 1. Intake and plan

The coordinator records a delivery brief before dispatching work:

```text
Objective:
Success criteria:
Repositories in scope:
Repositories explicitly out of scope:
Constraints and non-goals:
Decisions needed from the user:
```

It then makes a dependency-ordered assignment for every repository in scope.
Each assignment names the repository, expected outcome, permitted files or
areas when known, required validation, dependencies, and a handoff condition.
An unclear scope or design decision is reported to the user before work that
would make that decision irreversible.

## 2. Repository execution

Each developer reads the contract, its repository adapter, local instructions,
and the relevant task skill. It works only within its assignment and returns a
handoff rather than coordinating directly with other developers:

```text
Repository:
Assignment outcome:
Changed areas:
Validation executed and result:
Validation unavailable:
Compatibility or integration impact:
Blockers or decisions needed:
Handoff state: ready | awaiting decision | incomplete
```

The developer must report a cross-repository conflict to the coordinator. The
coordinator decides whether to split work into another explicit assignment,
sequence it, or ask the user for a decision.

## 3. Integration and user report

The coordinator checks that handoffs satisfy the delivery brief and that any
shared interface claims have evidence from every affected repository. It does
not label a delivery complete merely because every developer stopped.

At a meaningful milestone, blocker, or completion, the coordinator reports:

```text
Delivery status:
Result against success criteria:
Repository handoffs and validation:
Risks, limitations, and unavailable checks:
Decision needed from the user, if any:
Next bounded action:
```

Do not emit routine status messages when nothing actionable changed. Preserve
the detailed handoffs as durable repository documentation only when they
contain knowledge that belongs to a repository; transient coordination state
belongs to the active delivery, not to source files.

## Provider-neutral execution

This model works with a multi-agent runtime, a single-agent command-line tool,
or a human-led process. A runtime may map each developer instance to an
isolated agent, a separate task, or sequential role passes. It must preserve
the same scope, handoff, validation, and authorization boundaries.

Provider bootstrap and installation instructions belong in workspace adapters.
Do not encode provider-specific agent IDs, commands, prompts, or account
assumptions in this workflow.
