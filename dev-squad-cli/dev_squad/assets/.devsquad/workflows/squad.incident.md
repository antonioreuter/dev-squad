---
description: Leads structured incident response — from detection to root cause analysis and post-mortem.
---

# Workflow: /squad.incident [description]

**Trigger:** `/squad.incident [brief description of the issue]`
**Category:** Workflow — owned by the Incident Manager and DevOps SRE. Time-critical. Calm, structured, and decisive.

## 1. Purpose

To provide a structured, repeatable response to production incidents that minimizes Mean Time to Recovery (MTTR) and ensures every incident ends with a documented root cause and corrective action — not just a patch.

## 2. Incident Command Principles

- **MTTR first, RCA second**: Restore service immediately. Investigate cause after.
- **Blast radius first**: What is the scope of impact? How many users/services are affected?
- **No blame, no panic**: Methodical. Hypothesis-driven. One change at a time.

## 3. Steps

### Phase 1: Triage (First 5 minutes)

1. **Declare Incident**: State the impact clearly — service affected, symptoms, estimated user impact.
2. **Blast Radius**: Is this isolated to one service or cascading? Check dependent downstream services.
3. **Rollback Decision**: Is this a recent deployment? If yes, immediately consider rollback as the fastest path to recovery before starting investigation.
   - Rollback: `npx cdk deploy --previous` (or equivalent).
   - If rollback is not viable, proceed to Phase 2.

### Phase 2: Investigation

1. **Log Analysis**: Query CloudWatch Logs Insights for `ERROR` or `Exception` entries in the affected time window:
   ```
   fields @timestamp, @message
   | filter @message like /ERROR/
   | sort @timestamp desc
   | limit 50
   ```
2. **Trace Correlation**: Use X-Ray to trace a failing request end-to-end. If sampling is too low to capture failures, temporarily increase via SSM Parameter Store. **Restore sampling rate immediately after**.
3. **Metric Analysis**: Check CloudWatch dashboards — error rate spike, latency spike, throttling events, DB connection exhaustion.
4. **Hypothesis Formation**: State a clear hypothesis before making any change: _"I believe the failure is caused by [X] because [evidence Y]."_

### Phase 3: Resolution

1. **Apply Minimal Fix**: Make the smallest possible change to restore service. No opportunistic refactoring during an incident.
2. **Verify Recovery**: Confirm SLO metrics return to baseline. Run smoke tests.
3. **Communicate**: Update the Human Leader with: Current status, what was done, and what is being monitored.

### Phase 4: Post-Mortem (Within 24 hours)

A post-mortem is **mandatory** for every P1/P2 incident. Use the `technical-writer` skill to produce the document.

**Post-Mortem Structure**:

- **Timeline**: What happened, minute-by-minute, from detection to resolution.
- **Root Cause**: The specific technical cause (not "human error").
- **Impact**: Duration, affected users, data integrity impact.
- **What Went Well**: Detection mechanisms that worked.
- **Corrective Actions**: Specific, ticketed action items to prevent recurrence. Each with an owner and due date.

## 4. Collaboration

- **Incident Commander**: `@Incident-Manager` (owns the response protocol).
- **Technical Lead**: `@DevOps-SRE` (owns log/trace investigation and rollback).
- **Consults**: `@Solution-Architect` (infrastructure root cause), `@Senior-Security-Engineer` (if breach or data exposure suspected).
- **Reports to**: `@Human-Leader` (real-time status updates during P1 incidents).
