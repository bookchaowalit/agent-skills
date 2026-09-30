---
name: unused-file-cleanup
description: Find tracked files, scripts, and modules in the Solo Empire root repository that nothing references, verify each candidate, and propose or apply an approved, scoped cleanup. Use when asked to find or remove unused, dead, orphaned, or stale files (for example "หาไฟล์ที่ไม่ได้ใช้", "ลบไฟล์ที่ไม่ได้ใช้", "dead code", "orphan files").
---

# Unused File Cleanup

## Overview

`task cleanup:unused` runs a read-only scan that lists tracked files whose
filename (or module stem for code) appears in no other tracked text file. The
scan never deletes, moves, or stages anything. A candidate is only a lead:
every removal needs verification and explicit approval.

## Workflow

- [ ] Run `task cleanup:unused -- --kind code` first (scripts and modules), then
      `task cleanup:unused -- <path-prefix>` for a focused area. Use `--json`
      when the result feeds another step.
- [ ] Verify each candidate before classifying it:
  - `rg -n "<stem>"` across the repo, including dynamic forms (glob patterns,
    string-built paths, `run-python3` wrappers, `importlib`, CLI names).
  - Check scheduled or external callers: Taskfiles under `infra/tasks/`,
    `.github/workflows/`, cron/systemd/Task Scheduler definitions, Docker and
    compose files, and `package.json` scripts.
  - `git log --oneline -3 -- <path>` for intent; a recent commit usually means
    work in progress.
- [ ] Classify every candidate as `keep`, `archive`, or `delete`, with a
      one-line reason, and present the table to the user.
- [ ] Apply only the rows the user approves: `git rm <path>` per file (never
      `git add .`), or `git mv` into `infra/scripts/archive/one-off/` for
      archive. Update any doc or catalog that listed the file.
- [ ] Run the checks for the touched area (`task test`, `task typecheck`,
      `task docs:check`), then commit only the scoped paths.

## Decision rules

- Referenced only by dynamic paths, a scheduler, or an external system → `keep`.
- Product or content asset (`catalog/`, `media/`, client deliverables,
  templates, `.docx`) → `keep`; these are consumed by people, not code.
- One-off fix or migration script already applied → `archive` or `delete`.
- Duplicate of a newer file (`*_v2`, `*-old`, `copy`) → `delete` after
  confirming the newer file is the one referenced.
- Last commit within 14 days → ask before any action.
- Anything under `data/`, `artifacts/`, `diary/`, nested repositories, or
  generated sub-agent files → out of scope; the scan already excludes them.
- Never delete without an explicit yes in chat for that set of files.

## Resources

- `infra/scripts/utils/unused_files.py` — the read-only scanner
  (contract `solo-empire.unused-files.v1`); run through `task cleanup:unused`.
