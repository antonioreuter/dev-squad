---
description: Decomposes implementation plans into atomic, actionable tasks with embedded Acceptance Criteria, parallelism markers, and traceability IDs.
---

# Skill: Task Generator

## 1. Objective

To break down high-level technical specifications or ideas into granular, developer-ready tasks that are immediately executable without additional context.

## 2. Required Tools

- None — this skill operates on project context and specification analysis.

## 3. Input

- A feature description, idea, or Acceptance Criteria list.
- Optionally: an implementation plan or architectural notes.

## 4. Strict Task Format (REQUIRED)

Every execution MUST load and follow the standardized format in `.devsquad/templates/tasks.md`.

**Core Format Components:**

1. **Checkbox**: Always `- [ ]` — enables progress tracking.
2. **Task ID**: Sequential `T001, T002, T003...` in execution order.
3. **`[P]` marker**: Include ONLY if the task can run in **parallel** (touches different files or has no dependency on an incomplete task). Omit if sequential.
4. **`[US1]` label**: Maps the task to its parent User Story (`[US1]`, `[US2]`, etc.). Omit for Setup tasks with no parent story.
5. **Description**: Clear, action-oriented verb + exact layer or file path.

**Examples:**

```
- [ ] T001 Create module directory structure in src/modules/[module]/
- [ ] T002 [P] [US1] Implement User entity with invariant guards in domain/user.entity.ts
- [ ] T003 [P] [US1] Implement UserRepository port interface in application/ports/user.repository.ts
- [ ] T004 [US1] Implement PrismaUserAdapter in infrastructure/prisma-user.adapter.ts
- [ ] T005 [P] [US2] Add POST /users endpoint in entry-points/api/users.controller.ts
```

**Common mistakes to avoid:**

- ❌ `- [ ] Create User model` — missing Task ID and layer path.
- ❌ `T002 [US1] Implement service` — missing checkbox.
- ❌ `- [ ] T003 Implement everything` — not atomic, no file path.

## 5. Phase Structure

Organize tasks into logical phases:

- **Phase 1 — Setup**: Project structure, DB migrations, environment config. No `[US]` label.
- **Phase 2 — Foundation**: Shared/blocking prerequisites (base classes, shared types). No `[US]` label.
- **Phase 3+ — User Stories**: One phase per User Story in priority order (`[US1]`, `[US2]`...). Within each: Domain → Application → Infrastructure → Entry Points.
- **Final Phase — Polish**: Cross-cutting concerns (error handling, logging, observability).

## 6. Output Summary

After the task list, always provide:

- **Total task count** and count per User Story.
- **Parallelism opportunities**: Which tasks can run concurrently.
- **Suggested MVP scope**: Typically Phase 1 + Phase 2 + `[US1]` tasks only.

## 7. Competency Boundary

Consult the **Solution Architect** if the decomposition requires a significant architectural change not covered in the original scope.
