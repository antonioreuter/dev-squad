---
description: Initiates the implementation phase of a feature, resolving all unknowns before any code is written.
---

# Workflow: /squad.preflight [feature_name]

**Trigger:** `/squad.preflight [feature_name]`
**Category:** Workflow — prevents "coding in the dark" and architectural drift.

## 1. Purpose

This workflow is the mandatory pre-flight check before writing a single line of code. It ensures unknowns are resolved, Acceptance Criteria are validated, and the squad is aligned.

## 2. Prerequisites (Soft Check)

Verify the following exist or create a lightweight version if not:

- **Acceptance Criteria** — from `/squad.plan` or inline.
- **Architectural context** — known layer boundaries, new modules, or external dependencies.
- **Test strategy** — at minimum, Happy Path + 2-3 edge cases.

If a prerequisite is missing and cannot be quickly drafted, flag to the **Human Leader** before proceeding.

## 3. Steps

### Phase 0: Research & Clarification (Resolve Unknowns First)

Before any design or code decision is locked in, identify and resolve all ambiguities.

1. **Extract Unknowns**: Review AC and implementation context. For every ambiguity, generate a research task.
2. **Resolve Findings**: For each unknown, document a concise decision record:
   ```
   - Decision: [What was chosen]
   - Rationale: [Why this was chosen]
   - Alternatives Considered: [What else was evaluated and why ruled out]
   ```
3. **Gate**: Do NOT proceed to Phase 1 until all `NEEDS CLARIFICATION` items are resolved. If a decision requires human input, surface it with "Option A / Option B" and a clear recommendation.

### Phase 1: Context Discovery

- Read the task description and all associated Acceptance Criteria.
- Identify the **Bounded Context** (which module does this belong to?).
- Review relevant rules: `architecture.md`, `coding-standards.md`, `security.md`.
- Run **`ac-review`** on the AC — no BLOCKING issues may remain before coding begins.

### Phase 2: Squad Briefing

- **@Lead-Developer**: Confirmed as primary implementer, layer-by-layer per `architecture.md`.
- **@QA-Tester**: Prepare test scaffolds based on AC and `testing.md` pyramid.
- **@Solution-Architect**: Consult before touching cross-module boundaries or infrastructure.

### Phase 3: Kickoff

- Begin implementation with the **Domain layer first** (pure logic, zero external dependencies).
- Run tests (`npm test` or equivalent) to confirm environment is green before writing new code.
- Commit incrementally, referencing Task IDs: `feat(patient): T002 implement PatientSearchQuery`.

## 4. Definition of Done

- All Phase 0 unknowns resolved and documented.
- AC passed `ac-review` — no BLOCKING issues.
- First Domain-layer commit in place.
- Test suites initialized.
