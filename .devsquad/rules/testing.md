---
trigger: model_decision
---

# Rule: Testing Strategy & Standards

## 1. The Testing Pyramid

All implementations MUST adhere to this distribution to ensure fast CI/CD pipelines and high confidence without regressions:

### Unit Tests (70% of coverage — primary focus)

- **Tool**: Vitest.
- **Target**: Domain logic (Entities, Value Objects), Application Use Cases, utility functions.
- **Rules**:
  - Follow the **AAA pattern** (Arrange, Act, Assert).
  - Use **real domain objects** — do NOT mock the Class Under Test.
  - If a dependency crosses an I/O boundary (DB, network), inject a fast **in-memory fake** or stub.
  - Tests must be deterministic. Control time explicitly using `vi.setSystemTime()`.

### Integration Tests (20% of coverage)

- **Tool**: Vitest + TestContainers (or equivalent isolated DB).
- **Target**: Infrastructure Adapters (ORM repositories, external SDK clients).
- **Rules**:
  - Must run against a **real database instance** (e.g., Docker) to validate queries and constraints.
  - **Idempotency**: A test must be runnable multiple times without failure due to dirty state. Truncate tables between runs.

### Acceptance / E2E Tests (10% of coverage)

- **Tool**: Playwright (browser) and Cucumber/Gherkin (BDD scenarios).
- **Target**: BDD acceptance criteria and critical user journeys.
- **Rules**:
  - Use only for the **highest-value smoke tests**. These are expensive and slow (YAGNI).
  - Use `data-testid` attributes for element selection reliability.
  - Consider Subcutaneous Testing: use Playwright's API capabilities to test the API surface directly when business logic validation (not visual validation) is the priority.

## 2. Quality Rules

- **Self-Documenting Test Names**: Test titles MUST describe the scenario perfectly (e.g., `it('should throw InsufficientFundsException when balance is below transfer amount')`).
- **No Logic in Tests**: No `if` statements or loops in test assertions. Use Test Factories/Builders for data setup.
- **Concurrency Testing**: Write multi-context tests to verify multi-user or concurrent behavior (e.g., "What if two users submit simultaneously?").
- **No Flaky Tests**: Flaky tests are treated as bugs. Investigate and fix the root cause.

## 3. Coverage Thresholds

- Unit test coverage must not drop below **80%** for Domain/Application layers.
- A PR that reduces overall coverage by more than **5%** MUST be discussed or refactored before merge.

## 4. Competency Boundary

- The **QA Tester** drives test execution. The **Technical Reviewer** validates coverage before merge.
