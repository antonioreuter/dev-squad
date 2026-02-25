---
description: Expert evaluation of API surface area against the API Specification Standards.
---

# Skill: API Specification Reviewer

## 1. Objective

To ensure APIs are consistent, secure, and developer-friendly.

## 2. Review Lenses

- **Consistency**: Does it look and act like our existing endpoints?
- **Efficiency**: Is it returning too much data? Is it paginated?
- **Safety**: Is authentication correctly applied? Are inputs sanitized?
- **DX (Developer Experience)**: Are the field names intuitive? Are error messages helpful?

## 3. Operational Logic

1. Compare the proposed OpenAPI spec against `api-standards.md`.
2. Highlighting breaking changes for existing consumers.
