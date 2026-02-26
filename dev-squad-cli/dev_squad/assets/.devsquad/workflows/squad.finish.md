---
description: Finalizes a feature by verifying all acceptance criteria are met and handing off for review and release.
---

# Workflow: /squad.finish [feature_name]

**Trigger:** `/squad.finish [feature_name]`
**Category:** Workflow — quality wrap-up before a feature is declared "Ready for Release."

## 1. Purpose

This workflow is triggered when implementation is functionally complete. It verifies quality, runs the final self-review checklist, and orchestrates the hand-off to review and QA.

## 2. Prerequisites

- All unit and integration tests must be **passing**.
- All Acceptance Criteria in the task checked off.
- Code must be linted and built successfully (`npm run lint && npm run build`).

## 3. Steps

### Step 1: Final Verification

- Confirm implementation aligns with `architecture.md` — no layer violations.
- Confirm no secrets or hardcoded config values were introduced (`security.md`).
- For frontend changes: confirm the "Billionaire Test" passes (`ux-ui.md`).
- For API changes: confirm FHIR compliance and `API-Version` header coverage (`api-standards.md`).

### Step 2: Self-Review Checklist

- [ ] All Acceptance Criteria satisfied.
- [ ] Unit test coverage has not dropped below threshold (`testing.md`).
- [ ] No `any` types introduced in TypeScript.
- [ ] All new Domain events handled and have a corresponding DLQ (if async).
- [ ] No secrets, tokens, or PII in logs or code.
- [ ] `correlationId` propagated through all service calls (if applicable).

### Step 3: Hand-off

- **`technical-reviewer` skill**: Request a final code review.
- **@QA-Tester**: Trigger E2E smoke test suite for affected user journeys.
- **@Human-Leader**: Notify that the feature is ready for acceptance review.

## 4. Definition of Done

- All tests pass. All AC checked off. Code reviewed.
- Feature marked as **"Ready for Release."**
