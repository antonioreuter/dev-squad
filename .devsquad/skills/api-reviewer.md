---
description: Expert evaluation of API surface area against the API Specification Standards.
---

# Skill: API Specification Reviewer

## 1. Objective

To ensure APIs are consistent, secure, and developer-friendly before they are published or consumed by external clients.

## 2. Required Tools

- None — this skill operates on project context and the `api-standards.md` rule.

## 3. Review Lenses

For every API endpoint or contract under review, evaluate against these dimensions:

- **Consistency**: Does it look and act like our existing endpoints? Are naming conventions, pagination patterns, and error formats uniform?
- **Efficiency**: Is it returning too much data? Is it paginated? Are N+1 query patterns avoided?
- **Safety**: Is authentication correctly applied? Are inputs validated with strict schemas (e.g., Zod)? Are IDOR risks mitigated?
- **DX (Developer Experience)**: Are the field names intuitive? Are error messages helpful and actionable? Is the OpenAPI spec complete?
- **Versioning**: Does it follow the project's versioning strategy (e.g., `API-Version` header)?

## 4. Operational Logic

1. Compare the proposed OpenAPI spec or endpoint implementation against `api-standards.md`.
2. Highlight breaking changes for existing consumers (field removals, type changes, behavior shifts).
3. Label issues as **BLOCKING** (must fix before merge) or **NIT** (optional improvement).
4. Output a structured review with a maximum of 7 key findings.

## 5. Competency Boundary

- Consult the **Senior Security Engineer** for authentication and authorization concerns.
- Consult the **Solution Architect** for cross-service API contract dependencies.
