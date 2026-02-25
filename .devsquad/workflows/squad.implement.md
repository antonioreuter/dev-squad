---
description: Executes a single atomic implementation task with strict TDD and architectural rigor.
---

# Workflow: /squad.implement [task_id]

**Trigger:** `/squad.implement [task_id]` (e.g., `/squad.implement T001`)
**Category:** Workflow — the core coding engine. Never implement multiple tasks at once.

## 1. Purpose

To execute one, and only one, implementation task from the feature breakdown. It guarantees that code is written layer-by-layer, tested immediately, and self-reviewed against the project's always-on rules before moving to the next task.

## 2. Prerequisites

- The feature must have passed the `/squad.preflight` pre-flight gate.
- The `task_id` must exist in the generated task list.

## 3. The Execution Loop

### Step 1: Context Hydration

- Read the specific task description for `[task_id]`.
- Map the task to its target **Hexagonal Architecture layer** (Domain, Application, Infrastructure, or Entry-Point).
- **Rule Check**: Mentally review `coding-standards.md` for clean code rules and `security.md` if handling inputs/data.

### Step 2: Test-Driven Development (TDD)

- **Do not write implementation code yet.**
- Write the unit test(s) for the expected behavior first (using Vitest or the project's framework).
- The test must map to the BDD Acceptance Criteria covered by this task.
- Run the test to confirm it fails (if shell execution is permitted by the Human Leader).

### Step 3: Implementation

- Write the implementation code to make the test pass.
- Follow the "Tell, Don't Ask" principle and ensure Rich Domain Models (no anemic data bags).
- Do not introduce `any` types in TypeScript.
- Do not catch exceptions just to log them; either handle them or let them bubble up.

### Step 4: Self-Review

Before declaring the task done, the `@Lead-Developer` must verify:

- [ ] Are all SOLID principles respected?
- [ ] Is there any business logic leaking into the Infrastructure or API layers?
- [ ] Do the tests pass?
- [ ] Is the code concise and DRY? (YAGNI check)

### Step 5: Wrap & Commit

- Propose a git commit message referencing the task ID:
  ```
  feat(module): [T001] implement patient search query
  ```
- Ask the Human Leader for permission to execute the next task.

## 4. Definition of Done

- Test is written and passing.
- Code avoids layer violations and adheres to clean code standards.
- Git commit proposed.
