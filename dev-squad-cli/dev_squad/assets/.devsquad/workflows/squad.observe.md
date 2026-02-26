---
description: Sets up full observability for a service — instrumentation, SLOs, alarms, and dashboards.
---

# Workflow: /squad.observe [service_name]

**Trigger:** `/squad.observe [service_name]`
**Category:** Workflow — owned by the DevOps SRE. Run after a new service is deployed or when observability gaps are identified.

## 1. Purpose

To ensure every service running in production is fully observable — logs, metrics, traces, SLOs, and alarms — so that issues are detected before users report them.

> **Core Belief**: If it's not monitored, it doesn't exist.

## 2. Steps

### Step 1: Instrument the Code

- Add **OpenTelemetry** (OTel) SDK to the service.
- Enforce **structured JSON logging** on every log line, including:
  - `correlationId` — propagated from the incoming request header.
  - `service` — the service name.
  - `level` — `info`, `warn`, `error`.
  - `timestamp` — ISO 8601.
- Ensure **NO PII** appears in any log line (`security.md` compliance).

### Step 2: Define SLOs

- Identify the key SLIs (Service Level Indicators):
  - **Availability**: `1 - (error_rate)` — target ≥ 99.9%.
  - **Latency**: p99 response time — define target per endpoint based on business requirements.
- Configure **AWS Application Signals** SLO definitions.
- Deploy SLO dashboards in CloudWatch.

### Step 3: Configure Alarms

- Create **composite CloudWatch alarms** covering:
  - Error rate threshold (e.g., > 1% 5xx over 5 minutes).
  - Latency threshold (e.g., p99 > 500ms over 3 consecutive periods).
  - Resource utilization (Lambda concurrency throttles, DB connection pool exhaustion).
- Map all alarms to the appropriate on-call channel (Slack, PagerDuty, SNS).

### Step 4: Distributed Tracing

- Enable **AWS X-Ray** (or OTel-compatible tracer) with conservative sampling rates.
- **Cost control**: Keep sampling at ≤ 5% in production. Only increase temporarily during active troubleshooting via SSM Parameter Store — always restore after.

### Step 5: Real User Monitoring (RUM)

- If the service has a user-facing UI, configure **CloudWatch RUM**:
  - Track Core Web Vitals (LCP, FID, CLS).
  - Set performance budget alerts (e.g., LCP > 2.5s triggers a warning).

### Step 6: Validate

- Trigger a synthetic test request and confirm:
  - Log entry appears in CloudWatch Logs with correct structure.
  - Trace appears in X-Ray.
  - SLO metrics are reporting correctly.

## 3. Collaboration

- **Triggers**: `@Lead-Developer` (new service deployed), `@Human-Leader` (observability gap identified).
- **Consults**: `@Solution-Architect` (resource limits and architecture), `@Senior-Security-Engineer` (PII in logs validation).
