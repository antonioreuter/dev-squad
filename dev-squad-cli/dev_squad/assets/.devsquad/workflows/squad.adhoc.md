---
description: Handles technical debt, ad-hoc assignments, and urgent refactors with a lightweight planning and approval flow.
---

# Workflow: /squad.adhoc [request]

**Trigger:** `/squad.adhoc [detailed description of the debt or task]`
**Category:** Workflow — Surgical execution of non-feature work.

## 1. Purpose

To provide a rapid but rigorous path for paying technical debt and executing ad-hoc technical assignments without the overhead of a full feature planning session, while maintaining mandatory testing and human oversight.

## 2. Operational Loop

### Step 1: Persona Activation

- Adopt the **@AdHoc-Expert** persona.
- Adopt the `troubleshooter` and `lead-developer` skills.

### Step 2: Lightweight Planning

- Analyze the request and identify the affected components.
- **Blast Radius Assessment**: List files and modules influenced by the proposed change.
- **Testing Strategy**: Define the specific tests required to verify the fix and prevent regressions.
- Generate a summary including the "Why," "How," and "Verification Plan."

### Step 3: PM Review & HL Approval

- Output the plan to the squad chat.
- Tag the **@Project-Manager** for a "Consistency Review."
- Tag the **@Human-Leader** for "Final Approval."
- **STOP**: Wait for "APPROVED" from the Human Leader.

### Step 4: Red-Green Execution

- Once approved, generate atomic tasks following the `[T001] [P] [US1]` format.
- **Mandatory First Task**: Create/Update the test suite to capture the current (debted) or intended state.
- **Mandatory Final Task**: Run the full regression suite.

## 3. Definition of Done

- The technical debt is resolved or the ad-hoc task is implemented.
- All new and existing tests pass.
- NO regressions introduced in the identified "Blast Radius."
- The change is documented in the project logs.
