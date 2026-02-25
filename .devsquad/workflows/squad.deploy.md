---
description: Orchestrates a full, safe release to production — from pre-flight checks to post-deployment verification.
---

# Workflow: /squad.deploy [service_name?]

**Trigger:** `/squad.deploy` or `/squad.deploy [service_name]`
**Category:** Workflow — owned by the DevOps SRE. No deployment proceeds without completing every step.

## 1. Purpose

To ensure every release to production is safe, verified, and immediately observable. No "cowboy deployments." Every step is a gate — a failure stops the pipeline and triggers a rollback decision.

## 2. Steps

### Step 1: Pre-Deployment Gate

- [ ] Run linting: `npm run lint` — must pass with zero errors.
- [ ] Run unit + integration tests: `npm test` — must pass with zero failures.
- [ ] Run security scan (`npm audit` / `Semgrep`) — no High/Critical unmitigated vulnerabilities.
- [ ] Confirm all Acceptance Criteria for the target feature are checked off.

### Step 2: Build & Package

- Build the application artifacts (compile, bundle, package Lambda functions or container images).
- Confirm build exits with zero errors.

### Step 3: Infrastructure Review

- Verify AWS authentication: `aws sts get-caller-identity`.
- Run infrastructure diff to preview changes before applying:
  - CDK: `npx cdk diff`
  - Terraform: `terraform plan`
- **Gate**: Review the diff output. If unexpected resource deletions or replacements appear, **STOP and escalate** to `@Solution-Architect` before proceeding.

### Step 4: Deploy

- Apply infrastructure changes: `npx cdk deploy` or `terraform apply`.
- Deploy application artifacts (Lambda, container, static assets).

### Step 5: Post-Deployment Verification

- [ ] Run smoke tests against the production endpoint.
- [ ] Run E2E Playwright tests for critical user journeys.
- [ ] Verify CloudWatch Synthetics canaries are green.
- [ ] Confirm application metrics (error rate, latency p99) are within SLO thresholds.

### Step 6: Rollback Protocol (if Step 5 fails)

- Immediately trigger rollback to the previous known-good version.
- Document: what failed, at which step, and the error output.
- Create a bug ticket before ending the incident.

## 3. Collaboration

- **Triggers**: `@Lead-Developer` (code ready), `@Human-Leader` (release approval).
- **Consults**: `@Solution-Architect` (infra diff surprises), `@Senior-Security-Engineer` (vulnerability blocks).
- **Reports to**: `@Human-Leader` (deployment status), `cost-estimator` skill (if new AWS resources were added).
