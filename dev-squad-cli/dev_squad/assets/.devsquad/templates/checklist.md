# Technical Checklist: [FEATURE NAME]

**Purpose**: [Brief description of what this checklist verifies]
**Traceability**: [Link to spec.md / FR-xxx]

## [Category 1: Shared Infrastructure]

- [ ] CHK001 [Actionable item, e.g., Verify DB migrations are idempotent]
- [ ] CHK002 [Actionable item]

## [Category 2: User Story 1 (P1)]

- **Trigger**: [Action: e.g., Submit 'Update' form]
- [ ] CHK003 **Status**: [e.g., 200 OK]
- [ ] CHK004 **Data**: [e.g., Record updated in 'users' table]
- [ ] CHK005 **Side Effects**: [e.g., Cache invalidated]

## [Category 3: Security & Performance]

- [ ] CHK006 **AuthN**: [e.g., Verify user cannot update others' profiles]
- [ ] CHK007 **Load**: [e.g., Verify response < 200ms with 10 concurrent users]

---

**Note**: Checklist items are numbered sequentially (CHK001...) for easy reference.
