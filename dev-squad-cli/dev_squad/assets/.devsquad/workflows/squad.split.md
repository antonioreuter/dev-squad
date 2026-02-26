---
description: Decomposes a technical plan into a structured 'spec/' hierarchy with features, use cases, tasks, and test plans.
---

# Workflow: /squad.split [technical_plan]

**Trigger:** `/squad.split [technical_plan_content | path_to_plan]`
**Category:** Workflow — Structural decomposition of a validated plan.

## 1. Purpose

To transition from "What we are building" (Technical Plan) to "How we are structured to build it" (Filesystem Structure). This ensures every developer has a clear, isolated workspace for their feature/use case.

## 2. Operational Loop

### Step 1: Persona Activation

- Adopt the **@Feature-Architect** persona.
- Adopt the `feature-decomposer` skill.

### Step 2: Structural Analysis

- Analyze the provided technical plan.
- Identify distinct **Features** (Major modules/vertical slices).
- Identify **Use Cases** for each Feature (Atomic user interactions or system behaviors).

### Step 3: Filesystem Execution

- Create the `spec/` folder in the project root if it doesn't exist.
- For each Feature:
  - Create `spec/[feature-slug]/feature-detail.md`.
  - For each Use Case within that Feature:
    - Create `spec/[feature-slug]/[use-case-slug]/`.
    - Generate `checklist.md` by loading `.devsquad/templates/checklist.md`.
    - Generate `tasks.md` by loading `.devsquad/templates/tasks.md`.
    - Generate `test-plan.md` by loading `.devsquad/templates/test-plan.md`.

### Step 4: Verification

- List the created structure to the Human Leader.
- Provide a summary of how many features and use cases were generated.

## 3. Re-running & Updates

- If a user provides an updated technical plan for a specific feature:
  - The agent must identify the targeted feature.
  - Refresh the files in `spec/[feature-slug]/` without affecting unrelated features.
  - If a file already has custom content, use `replace_file_content` to update only the generated sections.

## 4. Definition of Done

- All identified Features have a `spec/[feature-slug]/` directory.
- All Features have a `feature-detail.md`.
- All identified Use Cases have a sub-directory with `checklist.md`, `tasks.md`, and `test-plan.md`.
- No orphan folders or inconsistent naming.
