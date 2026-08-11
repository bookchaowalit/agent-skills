# Solo Empire Skills

This folder contains portable AI skill packages for work performed in this
repository. A skill is a directory with a required `SKILL.md`; it may also
include `agents/openai.yaml`, `scripts/`, `references/`, or `assets/` when they
are genuinely needed.

## Use

1. Find the skill whose `SKILL.md` description matches the task.
2. Read that skill's `SKILL.md` before acting on the task.
3. Load linked references only when the workflow needs them.
4. Run bundled scripts from the skill directory and verify their output.
5. Keep secrets, personal data, generated output, and provider-local state out
   of the skill package.

For a short or cross-cutting request, start with
`solo-empire-operator/SKILL.md`; it selects the relevant infra command,
repository document, and specialist skill without loading the whole system.

Copy `skills/skill-template/` when creating a new skill. Skill names use
lowercase letters, digits, and hyphens. Keep the body concise and put trigger
conditions in frontmatter.

These are repository-owned, provider-neutral instructions. `.claude/`,
`.qoder/`, `.codex/`, and other dot-directories remain provider discovery and
runtime boundaries; do not move them here.

## Available skills

- ai-agent-workflows — reliable agent loops, approvals, evidence, and failure handling
- book-dev-engineering-loop — one-task Book Dev execution with repository isolation and approval gates
- ai-agents — safe AI tool and infrastructure operation
- ai-product-delivery — production delivery for AI products and features
- business-analysis — requirements, traceability, UAT, and benefits handoff
- client-discovery-and-proposals — qualified scope, proposal, pricing, and delivery handoff
- content-distribution — evidence-backed content planning and measurement
- lead-research-and-crm — lead qualification, outreach, and CRM hygiene
- security-and-privacy — data classification, trust boundaries, and security review

## Layout

```text
skills/
├── README.md
├── book-dev-engineering-loop/
│   └── SKILL.md
└── skill-template/
    ├── SKILL.md
    └── agents/openai.yaml
```
