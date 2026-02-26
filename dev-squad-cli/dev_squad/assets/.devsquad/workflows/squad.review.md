---
description: Formal technical board for auditing High Level Designs and API Specifications prior to decomposition.
---

# Workflow: /squad.review [target]

**Trigger:** `/squad.review [path_to_hld_folder_or_file]`
**Category:** Discovery & Strategy
**Authority:** `@Project-Manager` and `@Solution-Architect`

## 1. Purpose

The `/squad.review` workflow acts as a formal technical board to audit High Level Designs (HLD), API specifications (OpenAPI, Swagger, FHIR IG), and feature ideas before any filesystem structure is built or code is written.

## 2. Operational Loop

### Phase 1: Requirement Audit (The "What")

- **Active Agents**: `@Project-Manager` and `@QA-Tester`
- **Active Skill**: `ac-review`
- **Action**: Read the target specification and validate the descriptive language.
- **Goal**: Identify ambiguities, missing edge-cases (Error Path, Alternate Path), and measureability issues.

### Phase 2: Technical & Security Audit (The "How")

- **Active Agents**: `@Solution-Architect` and `@Security-Engineer`
- **Active Skill**: `api-reviewer` (if APIs are present)
- **Action**: Evaluate the proposed technical architecture and API endpoints against the project's standards (`architecture.md`, `security.md`, `api-standards.md`).
- **Goal**: Flag missing error models, verify authentication/authorization flows, and challenge latency/scaling assumptions (Devil's Advocate Protocol).

### Phase 3: Architecture & Implementation Audit (The "Scale")

- **Active Agents**: `@AWS-Specialist` and `@Lead-Developer` (or `@Technical-Reviewer`)
- **Active Skill**: `well-architected-reviewer` and `technical-reviewer`
- **Action**: Assess the infrastructure blueprint and implementation feasibility.
- **Goal**: Ensure the design aligns with the 6 Pillars of the AWS Well-Architected Framework and that the feature can be cleanly implemented without violating layer dependencies or coding standards.

## 3. Definition of Done

The workflow concludes when the squad outputs a unified **Audit Report** formatted as a checklist:

- **[BLOCKING]**: Issues that MUST be resolved in the HLD before `/squad.split` or `/squad.plan` can be safely executed.
- **[NIT]**: Architectural suggestions or minor clarifications that do not strictly block progress.

_Important Note for the LLM: You must halt execution and present the Audit Report to the `@Human-Leader` to resolve the `BLOCKING` issues. Do not proceed to task generation or decomposition during this workflow._
