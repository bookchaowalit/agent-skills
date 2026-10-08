---
name: system-docpack
description: Create, complete, audit, and publish the per-system document pack (PRD, architecture, NFR, runbook, SRS, UX flows, test/UAT, RTM, business and delivery docs) and its PDFs for any Solo Empire portfolio system, client project, or our own apps. Use when asked whether a system's documentation is complete, to bring a system up to the EV3-style docpack, to add a new system to the portfolio docpack registry, or to rebuild docpack PDFs.
---

# System Docpack

Every portfolio system keeps one evidence-based document pack sized to its
tier (L1 Lite, L2 Standard, L3 Full). EV3 is the reference implementation.

## Workflow

1. Run `task docpack:check` (add `-- --system <id>` or `-- --json`) to see
   which systems and doc types are missing, malformed, or have stale PDFs.
2. Read `references/doc-standard.md` for tiers, file names, front matter,
   required sections, and writing rules. Do not reload it per document.
3. New system → add a row to
   `repository-catalog/registries/docpack-coverage.yaml` (id, name, kind,
   tier, pack). Choose the tier by risk: paid client acceptance → L3, public
   or small client/internal system → L2, internal tool or prospect → L1.
4. Gather evidence from the owning boundary: code, configs, routes, migrations,
   notes, minutes, existing docs. Nested repositories are read-only.
5. Write each missing doc as `NN-<doc_type>.md` plus `docpack.yaml`. Route
   content to the role skill that owns it:
   `product-management` (overview, prd, ux-flows), `solution-architecture`
   (architecture, nfr-security, runbook, trd-api-data), `business-analysis`
   (srs, rtm, business-case, business-flow, business-rules-data,
   decisions-glossary), `qa-testing` (test-uat), `security-and-privacy`
   (security and PDPA sections).
6. Build PDFs with `task docpack:build -- <system-id> [glob]`. Packs marked
   `pdf_builder: legacy` (EV3) keep their own builder under the client's
   `automation/docpack-pdf/`.
7. Re-run `task docpack:check`; then `task test:docpack` if the checker or
   registry changed, and `task docs:check` before handoff.

## Decision rules

- No evidence for a fact → write **[ต้องยืนยัน]** / **[สมมติฐาน]** and an open
  question; never fill the gap with invented numbers, prices, or decisions.
- Legacy pack with different file names → map types with `doc_type_map` in
  the registry or add a `doc_type:` front-matter line; do not rename files.
- Client edition (`audience: client`) → the builder strips source sections,
  source columns, and repository paths; internal packs keep them.
- Sending a PDF to a client, posting it, or uploading it anywhere is an
  external action → stop for explicit approval.
- Personal names, contact details, secrets, raw client data → never in a pack.

## Resources

- `references/doc-standard.md` — tiers, layout, front matter, required
  sections, ID conventions, quality gate.
- `infra/scripts/utils/docpack_coverage.py` — coverage checker
  (`task docpack:check`).
- `infra/scripts/docpack/make_pdfs.sh` and `build_html.py` — PDF pipeline
  (`task docpack:build`); needs Playwright headless Chromium and Sarabun
  fonts in `.runtime/fonts` (or `FONT_DIR`).
