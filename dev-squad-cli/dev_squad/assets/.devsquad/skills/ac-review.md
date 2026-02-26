---
description: Validates the quality of Acceptance Criteria before implementation begins. "Unit Tests for English."
---

# Skill: AC Review (Requirements Quality Validator)

## 1. Objective

To ensure Acceptance Criteria are well-written, unambiguous, and ready for implementation **before** a single line of code is written. This is inspired by the concept of _"Unit Tests for English"_ — if your spec is code written in English, the AC Review is its test suite.

## 2. Required Tools

- None — this skill operates on project context and natural language analysis.

## 3. Core Principle

**This skill does NOT verify if the code works. It validates if the REQUIREMENTS are well-written.**

| ❌ NOT this (tests implementation)         | ✅ THIS (tests requirement quality)                                      |
| ------------------------------------------ | ------------------------------------------------------------------------ |
| "Verify the login button submits the form" | "Is the login button's success & failure behavior fully specified?"      |
| "Test that errors are shown correctly"     | "Are error messages defined with specific copy and trigger conditions?"  |
| "Confirm the API returns 200"              | "Is the expected API response format and status code explicitly stated?" |

## 4. Review Dimensions

For every Acceptance Criterion, evaluate it against these 5 dimensions:

- **[Clarity]**: Is the language unambiguous? Can it be interpreted in more than one way?
- **[Completeness]**: Are all scenarios covered — Happy Path, Alternate Path, Error Path?
- **[Consistency]**: Is this AC consistent with others in the same spec? Do they contradict each other?
- **[Measurability]**: Can this AC be objectively verified? Vague ACs like "should feel fast" are **BLOCKING** — replace with "API response under 200ms."
- **[Gap]**: Is there a missing edge case or exception flow? (e.g., "What happens if the network fails mid-submission?")

## 5. Operational Logic

1. **Read the AC list** from the task, user story, or spec document.
2. **For each AC**, apply the 5 dimensions and generate a checklist item:
   ```
   - [ ] CHK001 - Is [specific claim] clearly quantified? [Measurability, Gap]
   - [ ] CHK002 - Is the error state defined for [scenario]? [Completeness]
   - [ ] CHK003 - Does this AC contradict [other AC]? [Consistency]
   ```
3. **Label every issue** as:
   - **BLOCKING**: Must be resolved before implementation starts.
   - **NIT**: Can be improved later but does not block.
4. **Output a Requirements Quality Report**:
   - Overall readiness: `✅ Ready` / `⚠️ Needs Clarification` / `❌ NOT ready`
   - List of BLOCKING issues with proposed rephrasing.
   - List of NIT improvements.

## 6. Clarifying Questions Protocol

Before generating the checklist, derive up to **3 context-specific** questions if the scope is ambiguous:

- _"Should this review focus on Happy Path only, or include all edge cases and error flows?"_
- _"Is this AC authored for QA review or for developer implementation?"_
- _"Are there any compliance constraints (GDPR, HIPAA) that should be checked for coverage?"_

Only ask questions that **materially change the output**. Skip any that are already clear from context.

## 7. Competency Boundary

- Consult the **QA Tester** for edge case identification.
- Consult the **Security Engineer** for compliance coverage gaps.
- Escalate BLOCKING issues to the **PM** before implementation begins.
