# Delegation Brief and Plan Templates

Use these templates from `skills/subagent-orchestration/SKILL.md`. Fill every
field; write `none` instead of deleting a field so the worker knows it was
considered.

## Plan tree

Keep the plan in the main agent's context (or a scratchpad file for long work).
IDs are stable so briefs and handoffs can reference them.

```yaml
goal:
  id: G1
  outcome: "One sentence: what is true for the user when this is done"
  success_criteria:
    - "Checkable statement 1"
  constraints:
    - "Repository boundary, approval gate, or policy that applies"
  non_goals:
    - "What this work deliberately does not change"
tasks:
  - id: T1
    outcome: "One verifiable outcome"
    depends_on: []
    subtasks:
      - id: T1.1
        role: solo-explorer        # or main when the orchestrator does it
        parallel_group: A          # same group = dispatch together
        deliverable: "What comes back (paths, findings, diff, test result)"
        status: planned            # planned|running|complete|blocked
```

## Delegation brief

Send this as the sub-agent prompt. Keep it in English or Thai consistently;
keep paths, commands, and identifiers verbatim.

```markdown
# Brief <subtask id>: <short title>

## Goal context
- Goal <G id>: <outcome sentence>
- Task <T id>: <task outcome>
- Why this subtask matters: <how its result is used next>

## Assignment
<One paragraph: exactly what to do and the single deliverable.>

## Known facts
- <fact with path:line or command evidence the parent already has>

## Scope
- In: <files, directories, symbols, URLs>
- Out: <what must not be read, changed, or run>

## Steps
1. <concrete step with exact path, pattern, or command>
2. <...>

## Constraints
- Role boundary: <read-only | may edit listed files only>
- Never print, copy, or request credentials, tokens, cookies, or private payloads.
- No push, deploy, publish, external message, or spending.

## Acceptance criteria
- [ ] <checkable statement>
- [ ] <checkable statement>

## Verification
- `<exact command>` → expected: <result>

## Budget
- Read at most <N> files and <M> tool calls; stop and report when exceeded.

## Output
Return the `solo-empire.subagent-handoff.v1` JSON envelope with role fields
<list from sub-agent-handoff.md> and these extras: <optional extra keys>.

## Stop conditions
Return `blocked` or `needs_parent` when <ambiguity, missing access,
conflicting evidence, boundary crossing, or approval needed>.
```

## Example: weak versus strong Haiku brief

Weak: "Look into how hooks work and tell me what's wrong."

Strong (abridged):

```markdown
# Brief T1.1: Map PreToolUse decision path

## Goal context
- Goal G1: Bypass mode stops prompting for policy rules.
- Task T1: Find every place a hook decision is produced.

## Assignment
List each function that returns a PreToolUse decision and the exact output
shape it emits per harness.

## Scope
- In: infra/scripts/agent/harness_hooks.py, infra/scripts/agent/copilot_hooks.py
- Out: everything else; do not run tests.

## Steps
1. Search `permissionDecision` and `def policy_decision` in the two files.
2. For each hit, record path:line and the returned values.

## Acceptance criteria
- [ ] Every `permissionDecision` producer is listed with path:line.
- [ ] Claude, Codex, and Gemini output shapes are each stated.

## Budget
- At most 2 files and 8 tool calls.

## Output
Handoff v1 with explorer fields: findings, relevant_paths, hypothesis,
recommended_change.
```
