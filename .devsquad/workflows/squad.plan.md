---
description: Translates a raw idea or requirement into User Stories with BDD Acceptance Criteria, ready for implementation.
---

# Workflow: /squad.plan [idea]

**Trigger:** `/squad.plan [idea or feature description]`
**Category:** Workflow — the entry point for any new feature. Prevents "coding in the dark."

## 1. Purpose

To transform a raw idea into a structured, testable specification with BDD Acceptance Criteria before any code is written. This is the mandatory first step for every non-trivial feature.

## 2. Operational Loop

### Step 1: Idea Intake & Challenge

- Read the idea and identify the **core user need** behind it.
- Challenge assumptions: "Is this the right solution, or is the user's underlying need different?"
- If ambiguous, ask up to **3 clarifying questions** that would materially change the output. Skip questions already answered in the prompt.

### Step 2: Lens Review (Multi-Agent Consultation)

Before writing any criteria, consult the squad:

- **@Solution-Architect**: Is this feasible within the current architecture? Any layer boundary concerns?
- **@Senior-Security-Engineer**: Any AuthN/AuthZ, IDOR, or data privacy risks introduced?
- **@QA-Tester**: What are the obvious edge cases and concurrency risks?

If agents disagree, surface **Option A / Option B** with a clear recommendation to the Human Leader before proceeding.

### Step 3: Write Acceptance Criteria (BDD Format)

For each User Story, write criteria in `Given/When/Then` format:

```
Given [precondition / context]
When  [the actor performs an action]
Then  [the expected outcome]
And   [additional assertions]
```

Every AC must be:

- **Measurable**: No vague words like "fast" or "user-friendly." Quantify (e.g., "response < 200ms").
- **Testable**: A QA Tester must be able to write an automated test directly from it.
- **Complete**: Cover Happy Path, Alternate Path, and Error Path.

### Step 4: Hand-off

- Trigger `/squad.split [technical_plan]` after the plan is approved to decompose it into features and tasks.
- Trigger `/squad.preflight [feature]` when the AC are approved by the Human Leader.
- Optionally invoke `ac-review` to validate requirement quality before implementation.

## 3. Definition of Done

- User Stories are written in `Given/When/Then` format.
- All AC are measurable and testable.
- Lens Review completed — no unresolved conflicts.
- Human Leader has approved the AC.
