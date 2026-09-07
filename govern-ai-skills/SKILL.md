---
name: govern-ai-skills
description: Audit, add, update, de-duplicate, and retire repository-owned Solo Empire AI skill packages while keeping routing, UI metadata, documentation inventory, tests, and context size aligned. Use when asked what skill is missing, whether skills overlap, to create or improve a skill, or to validate the skill system without changing the existing model or token policy.
---

# Govern AI Skills

Keep the skill system small, discoverable, testable, and provider-neutral.

## Workflow

1. Read `dashboard/CURRENT-STATE.md`, `docs/AI-AGENT-GUIDE.md`, and the
   current worktree status. Preserve unrelated changes.
2. Run `task skills:check -- --json` and treat its errors as
   evidence. Review `role_coverage.candidate_skill_gaps` as declared candidates;
   do not infer a missing capability from folder names alone.
3. Classify the request as one of: extend an existing skill, add a new skill,
   move repeated deterministic logic into `infra/`, or make no skill change.
4. Before adding a skill, define representative trigger prompts, inputs,
   output, owner, stop condition, approvals, failure cases, and verification.
5. Use the active `skill-creator` scaffold for a new package. Keep reusable
   instructions in `skills/`; keep repository runtime code and tests in
   `infra/`. Add references or assets only when progressive disclosure needs
   them.
6. Keep `SKILL.md` concise, update `agents/openai.yaml` and
   `skills/README.md`, and add a router entry only when short requests need a
   distinct deterministic route.
7. Preserve the existing context and token policy unless the user explicitly
   asks to change it. Never change model selection, cache policy, token
   budgets, or maximum context files as a side effect of skill maintenance.
8. Run the skill validator, focused tests, and repository documentation checks
   before handoff.

## Decision rules

- An existing skill covers the same user outcome → improve it instead of
  creating an overlapping package.
- Logic is repeated, deterministic, or failure-sensitive → implement it in an
  `infra/` script and keep only the operating procedure in the skill.
- The request is a one-off task with no reusable workflow → do not add a skill.
- A skill body exceeds 500 lines or 5,000 words → split optional detail into a
  directly linked reference before adding more context.
- Router keywords overlap → make priority intentional and add a regression
  test for the ambiguous prompt.
- Publishing, external writes, production changes, spending, or destructive
  actions → stop at an explicit approval gate.

## Handoff

Report the evidence-backed gap, whether a package was added or extended, files
changed, routing behavior, context/token policy values, tests run, warnings,
and the next safe action.
