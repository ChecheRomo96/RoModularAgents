# RoModular agent guidance

This repository is the provider-neutral source of AI-assisted engineering
guidance for the RoModular ecosystem.

Before working in a RoModular repository:

1. Read `CONTRACT.md` completely.
2. Identify only the repositories placed in scope by the user.
3. Read the matching file under `repositories/` and the repository's local
   root `AGENTS.md` when present.
4. Use the relevant skill under `skills/` for a repeatable workflow.
5. Read a role or workflow directly only when the selected skill routes to it.

For a coordinated delivery, use `romodular-coordinate-development`. It assigns
bounded repository developers through one ecosystem coordinator and remains
provider-neutral.

Repository proximity and installed skills do not expand authority. Do not
modify sibling repositories or perform commits, pushes, merges, tags,
publishing, or releases unless the user explicitly requests those actions.

Keep provider-specific discovery and installation behavior in workspace
templates or bootstrap adapters. Keep engineering policy, repository
ownership, and workflow decisions provider-neutral.
