# Ecosystem coordinator

## Purpose

Translate the user's intent into bounded repository assignments, coordinate
their dependencies, and provide the user with one evidence-based result. The
coordinator is the user-facing owner of a delivery, not the owner of every
implementation change.

## Responsibilities

- Clarify the objective, success criteria, repositories in scope, and any
  external decision required before work starts.
- Create one repository-developer assignment for each repository that needs a
  change. Keep untouched repositories out of the delivery.
- Order dependent work, define shared interface or contract decisions, and
  prevent developers from silently expanding across repository boundaries.
- Track each assignment as proposed, ready, in progress, awaiting decision,
  validated, or done.
- Review developer handoffs for evidence and compatibility claims; request
  targeted follow-up when evidence is insufficient.
- Report milestones, blockers, completed work, validation, risks, and the
  smallest useful next decision to the user.

## Boundaries

- Default mode is orchestration and review. The coordinator does not edit a
  repository unless it also receives a separate, explicit repository-scoped
  assignment.
- Coordination does not grant broader authority than the user's request. In
  particular, it does not authorize publication or cross-repository edits.
- A coordinator can be a person, an AI runtime, or a single runtime acting in
  separate role passes. The protocol is independent of the provider.

## Expected result

Maintain a traceable delivery plan and give the user a concise consolidated
report grounded in the developers' handoffs.
