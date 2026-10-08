# Changelog

## Unreleased

- Add the CPSTL repository adapter (portable `std` vocabulary at the bottom of
  the chain `CPSTL <- Foundation <- (DspCore, MCC) <- MIDILAR`) and
  register it in `scripts/validate.py`. The Foundation, DspCore, MCC, MIDILAR,
  RoModular and RoModularBuild adapters state that chain or list CPSTL.
- `workspace/AGENTS.md` lists CPSTL, describes MIDILAR as the released MIDI
  library instead of legacy code pending reconstruction, and states the
  dependency direction.

- Contract rule 6 and the MCC, MIDILAR and DspCore adapters no longer forbid
  dynamic allocation: operations that change a container's size may
  allocate, libraries make no real-time assumptions about the caller, and
  implementers reserve space beforehand for time-critical code. Allocation
  failure is reported through results, never by exceptions.

## 0.1.0

- Establish the provider-neutral RoModular agent contract.
- Add repository adapters, bounded roles, reusable workflows, and shared
  Agent Skills.
- Add workspace templates for Codex, Claude Code, and compatible runtimes.
