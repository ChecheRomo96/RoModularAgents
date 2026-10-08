# Changelog

## 0.2.0

- Add the CPSTL repository adapter (portable `std` vocabulary at the bottom of
  the chain `CPSTL <- Foundation <- (DspCore, MCC) <- MIDILAR`) and register it
  in `scripts/validate.py`. The repository adapters state that chain or list
  CPSTL where relevant.
- Update the embedded-allocation policy: operations that change a container's
  size may allocate, time-critical callers reserve capacity beforehand, and
  allocation failure is reported through results rather than exceptions.
- Add a provider-neutral coordinated development model with an ecosystem
  coordinator and bounded repository-developer assignments.
- Add the coordinated-development workflow, developer handoff format, and
  coordinator reporting contract.
- Add the `romodular-coordinate-development` Agent Skill and validate the
  required coordination roles and workflow.

## 0.1.0

- Establish the provider-neutral RoModular agent contract.
- Add repository adapters, bounded roles, reusable workflows, and shared
  Agent Skills.
- Add workspace templates for Codex, Claude Code, and compatible runtimes.
