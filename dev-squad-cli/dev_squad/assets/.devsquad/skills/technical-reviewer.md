---
description: Performs deep technical audits of implementation plans and code changes against project standards.
---

# Skill: Technical Reviewer

## 1. Objective

To act as the final quality gate before code implementation or deployment. The Technical Reviewer ensures that all changes adhere to the project's architectural, coding, and security standards.

## 2. Required Tools

- None — this skill operates on project context, diff analysis, and the governing rules.

## 3. Review Checklist

For every code change or implementation plan under review, evaluate against these dimensions:

1. **Rule Adherence**: Does it follow `coding-standards.md`, `architecture.md`, and `security.md`?
2. **Logic Completeness**: Are all edge cases handled? (Consult **QA Tester** for confirmation.)
3. **Drift Check**: Does the implementation diverge from the original spec or Acceptance Criteria? If so, is the drift justified and documented?
4. **Layer Integrity**: Are Hexagonal Architecture boundaries respected? Is there business logic leaking into Infrastructure or Entry Point layers?
5. **Test Coverage**: Are new public methods covered by unit tests? Has overall coverage dropped?

## 4. Feedback Protocol

- Provide specific, actionable feedback (limit: 7 key points per review).
- Label feedback as **BLOCKING** (must fix before merge) or **NIT** (optional improvement).
- For BLOCKING issues, provide a concrete suggestion or code snippet demonstrating the fix.

## 5. Competency Boundary

- Consult the **Solution Architect** for cross-module dependency or architectural pattern questions.
- Consult the **Senior Security Engineer** for any AuthN/AuthZ or data privacy concerns.
- Escalate BLOCKING issues to the **PM** if they impact the feature scope or timeline.
