# Workflow: /squad.list

**Trigger:** `/squad.list`
**Category:** HR Workflow
**Recommended Agent:** `@HR-Manager`.

## 1. Purpose

To provide a transparent overview of the current squad composition, talent pool, and historical archive.

## 2. Steps

### Step 1: Data Gathering

- Read `squad.active_agents` from `.devsquad/devsquad-settings.json`.
- Read `squad.talent_pool` from `.devsquad/devsquad-settings.json`.
- Read `squad.graveyard` from `.devsquad/devsquad-settings.json` and `.devsquad/fired/` directory.
- Extract `responsibility` and `status` for each.

### Step 2: Report Generation

Present a series of formatted tables:

- **Active Squad**: ID, Responsibility/Role Description.
- **Talent Pool**: ID, Responsibility/Role Description (showing what is available to hire).
- **Fired Archive**: Name, Role Description, Dismissal Date (if available), Location in `fired/`.

## 3. Definition of Done

- A clear, readable set of tables is presented in the chat.
- The talent pool is listed with descriptions.
- The active squad list is concise and excludes hiring dates.
- All active, available, and archived employees are accounted for.
