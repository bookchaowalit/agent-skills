---
name: book-dev-engineering-loop
description: Execute one bounded Book Dev task from the daily engineering-loop handoff with repository isolation, verification evidence, and explicit approval gates.
---

# Book Dev Engineering Loop

Use this skill when an AI agent is asked to act on the Book Dev engineering
loop. Prefer the single-candidate execution ticket first:

- `data/runtime/agent-loop/book-dev/execution/current.md`
- fallback queue: `data/runtime/agent-loop/book-dev/latest.md`

## Contract

The daily scanner is deterministic and read-only. It discovers open local Book
Dev tasks, inspects nested Git status, prepares a bounded handoff, and queues
**one** execution ticket. This skill is the execution side of that ticket and
must work on **one candidate at a time**.

```text
read execution ticket → inspect context → plan → implement
→ run narrow verification → record evidence → stop at approval gate
```

## Required first steps

1. Read `data/runtime/agent-loop/book-dev/execution/current.md` when present.
   If missing, fall back to the first candidate in
   `data/runtime/agent-loop/book-dev/latest.md` and the linked context files.
2. Confirm the exact nested repository path and run:

   ```bash
   git -C <repo> status --short
   git -C <repo> branch --show-current
   ```

3. If the working tree is already dirty, inspect the diff and preserve every
   unrelated change. Never use `git reset`, `git clean`, or an equivalent
   destructive command.
4. Check the task's acceptance evidence in the Book Dev catalog before editing.
5. Do not start a second candidate while the current execution ticket is open.

## Execution boundary

- Work only inside the selected nested repository.
- Use the repository's own README, package scripts, tests, and release rules.
- Keep the change narrow and explain why each changed file is needed.
- Do not touch the parent Solo Empire catalog or another nested repository as
  part of the implementation task.
- Do not invent a test command when the repository does not document one;
  report the missing verification path instead.

## Approval gates

Stop and ask the owner before any of the following:

- `git commit`, `git push`, merge, pull request creation, or branch deletion.
- GitHub archive, transfer, visibility change, or release/deployment.
- Reset, clean, overwrite, delete, credential use, spending, or external
  messages.
- Closing a task when the evidence is incomplete or an external dependency is
  still blocked.

Passing tests are evidence of behavior, not permission to publish or merge.

## Handoff result

Return a compact report containing:

- task ID and repository path;
- files changed and why;
- exact verification commands and pass/fail output;
- remaining blockers or unknowns;
- whether owner approval is required for the next action.

If the task is not safe to execute, record the reason and stop. Do not claim
completion from a clean tree, a generated report, or a green unrelated test.
