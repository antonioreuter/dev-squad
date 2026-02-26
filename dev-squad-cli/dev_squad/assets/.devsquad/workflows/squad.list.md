---
description: Lists current squad, talent pool, and fired archive.
---

# Workflow: /squad.list

**Trigger:** `/squad.list`
**Category:** HR Workflow
**Recommended Agent:** `@HR-Manager`.

## 1. Purpose

To provide a transparent overview of the current squad composition, talent pool, and historical archive.

## 2. Steps

### Step 1: Data Gathering (MANDATORY JSON SOURCE)

- **DO NOT** search for or reference `project.md` or `specs/project.md`. These are deprecated and deleted.
- **MUST** read exclusively from `.devsquad/devsquad-settings.json`.
- Read `squad.active_agents`.
- Read `squad.talent_pool`.
- Read `squad.graveyard` (Note: This key may be optional or empty; skip gracefully if not found).
- Check `.devsquad/fired/` directory for historical context.

### Step 2: Report Generation (3 MANDATORY SECTIONS)

Present the output in three distinct sections:

1.  **ACTIVE SQUAD**: Table with ID and Responsibility. (Sourced from `squad.active_agents`).
2.  **TALENT POOL**: Table with ID and Responsibility. (Sourced from `squad.talent_pool`).
3.  **FIRED ARCHIVE**: List or table of archived agents. (Sourced from `squad.graveyard` and `fired/` directory).

## 3. Definition of Done

- A clear, readable set of tables is presented in the chat.
- The talent pool is listed with descriptions.
- The active squad list is concise and excludes hiring dates.
- All active, available, and archived employees are accounted for.
