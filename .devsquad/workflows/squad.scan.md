---
description: Performs a deep scan of the repository structure and updates the project inventory.
---

# Workflow: /squad.scan

**Trigger:** `/squad.scan`
**Category:** Discovery & Strategy
**Authority:** `@Project-Manager`

## 1. Purpose

The `/squad.scan` workflow instructs the squad to build an accurate, up-to-date inventory of the current repository, identifying frameworks, languages, architectural patterns, and potential security gaps.

## 2. Important Instruction for the Agent

The actual scanning logic is executed by a native CLI command: `dev-squad scan`.

**If you have terminal/CLI execution capabilities:**

1. Propose and execute the command `dev-squad scan` in the background.
2. Wait for the command to finish.
3. Read the generated files located in `.devsquad/knowledge/inventory/` (e.g., `stack.md`, `structure.md`, `gaps.md`).
4. Provide the user with a high-level summary of the findings.

**If you DO NOT have terminal/CLI execution capabilities:**

1. Explicitly ask the user to open their terminal and run `dev-squad scan`.
2. Wait for the user to confirm they have done so.
3. Read the generated files located in `.devsquad/knowledge/inventory/` (e.g., `stack.md`, `structure.md`, `gaps.md`).
4. Provide the user with a high-level summary of the findings.

## 3. Definition of Done

- The CLI scanner has successfully run.
- The `.devsquad/knowledge/inventory/` files have been read.
- The Human Leader has received a synthesized summary of the repository's status.
