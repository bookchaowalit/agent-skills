---
name: security-and-privacy
description: Review and improve security and privacy for Solo Empire workflows, client work, agents, integrations, secrets, authentication, permissions, personal data, dependencies, and deployments. Use before releasing a workflow or when investigating a possible exposure, unsafe tool, or boundary violation.
---

# Security and Privacy

Reduce exposure, make trust boundaries visible, and stop unsafe actions before they become incidents.

## Review workflow

1. Classify the data as public, internal, client-confidential, personal, regulated, or secret. Minimize collection and define retention for anything non-public.
2. Map trust boundaries, owners, entry points, data stores, external services, nested repositories, and human approvals. Pay special attention to `infra/.env`, `accounts/`, the `bookchaowalit-freelance/` client repositories, `data/raw/`, backups, and generated reports.
3. Threat-model authentication, authorization, prompt or code injection, SSRF, unsafe file paths, webhook spoofing, excessive permissions, dependency risk, data leakage, replay, and destructive operations.
4. Apply least privilege, allowlists, schema validation, output encoding, timeouts, rate limits, idempotency, redaction, audit events, and safe error messages.
5. Keep secrets in approved environment or secret-management mechanisms. Never print, commit, paste into prompts, or place credentials in fixtures, logs, screenshots, or documentation.
6. Protect client boundaries: use the client's own `bookchaowalit-freelance/<client>` repository, avoid cross-client data access, and do not modify nested repositories unless they are explicitly in scope.
7. Verify with available tests, typechecks, dependency or secret scans, migration backups, and a manual review of permissions and logs. Record checks that could not run.
8. If an incident is suspected, contain access, revoke or rotate exposed credentials, preserve relevant evidence, assess affected data, and follow the repository or client notification policy.

## Stop conditions

Pause and ask for direction when the requested action needs an unapproved secret, bypasses authorization, exposes private data, sends an external message, changes production, or deletes/overwrites data without a recoverable plan.

## Handoff

Report the risk, affected boundary, evidence, severity rationale, mitigation, remaining uncertainty, owner, and verification performed. Do not include the sensitive value itself.
