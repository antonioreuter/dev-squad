---
description: Handles the structural decomposition of technical plans into a standardized 'spec/' directory hierarchy with boilerplate documentation.
---

# Skill: Feature Decomposer

## 1. Objective

To automate the translation of high-level features and use cases into a structured filesystem layout in the `spec/` directory, ensuring every piece of work has a traceable home and clear initial documentation.

## 2. Required Tools

- `write_to_file`: To create the markdown files and directory structure.
- `list_dir`: To check for existing structures and avoid overwriting unless intended.

## 3. Directory Structure Standards

Every execution MUST enforce the following hierarchy:

```text
spec/
└── [feature-slug]/
    ├── feature-detail.md
    └── [use-case-slug]/
        ├── checklist.md
        ├── tasks.md
        └── test-plan.md
```

- **Feature Slug**: Lowercase, kebab-case (e.g., `user-authentication`).
- **Use Case Slug**: Lowercase, kebab-case (e.g., `login-with-oauth2`).

## 4. Boilerplate Templates (REQUIRED)

### `feature-detail.md`

- **Context**: Why are we building this?
- **User Needs**: What the user wants to achieve.
- **Architectural Notes**: Any specific layer or pattern considerations.

### `checklist.md` (BDD Format)

- **Scenario**: Descriptive scenario name.
- **Given/When/Then**: Clear acceptance criteria list.

### `tasks.md`

- **Atomic Tasks**: Following the `[T001] [P] [US1]` format.
- **File Paths**: Explicit paths for implementation.

### `test-plan.md`

- **Positive Paths**: Standard success scenarios.
- **Negative Paths**: Error handling, invalid inputs.
- **Boundary Conditions**: Edge cases, rate limits, max sizes.

## 5. Execution Logic

1. **Intake**: Parse the provided technical plan or feature list.
2. **Sanitize**: Slugify feature and use case names.
3. **Verify**: Check `spec/[feature-slug]` existence.
4. **Create**:
   - Write `feature-detail.md` if it doesn't exist or if an update is requested.
   - For each use case, create the folder and populate the 3 mandatory files (`checklist`, `tasks`, `test-plan`).
5. **Sync**: If the user provides a modified tech plan for an existing feature, update the relevant files while preserving any manually added context if possible (using `replace_file_content` logic).

## 6. Competency Boundary

Consult the **Senior Software Engineer** or **Lead Developer** for the specific content of `tasks.md` to ensure technical accuracy.
