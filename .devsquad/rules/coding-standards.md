---
trigger: model_decision
---

# Rule: Coding Standards, Clean Code & SOLID

## 0. Development Philosophy

- **Human-Centric Code**: Write code that is easy to read and maintain by humans first, machines second.
- **Don't Reinvent the Wheel**: Check for well-established, maintained dependencies before writing custom solutions.
- **YAGNI (You Ain't Gonna Need It)**: Code only what is strictly necessary. Avoid speculative over-engineering.
- **KISS (Keep It Simple, Stupid)**: If a solution feels complex, it probably is. Refactor for clarity.
- **Idiomatic Code**: Use the best practices and idiomatic patterns of the language and framework in use.

## 1. Object-Oriented Paradigm

- **Encapsulation First**: Data and behavior coexist in Domain entities. OO over pure functional mapping.
- **Tell, Don't Ask**: Do not ask an object for its data to make a decision externally; tell the object what to do with its own data. This preserves encapsulation.
- **Rich Domain Models**: No anemic models (getters/setters only). Entities guard their invariants and expose behavioral methods that validate state transitions.
- **Composition over Inheritance**: Prefer "Has-A" over "Is-A." Deep inheritance hierarchies are forbidden.
- **Fail Fast (Guard Clauses)**: Validate method arguments and state at the very beginning of a method. Throw domain-specific exceptions early to avoid deep `else` nesting.
- **Dependency Injection**: Always inject dependencies (Adapters, Repositories) into Application Use Cases via constructors. No global state in business logic.
- **Performance**: Favor high-performance algorithms. Be conscious of time and space complexity in hot paths.

## 2. SOLID Principles

- **SRP (Single Responsibility Principle)**: A class or function should have one — and only one — reason to change. If a class handles both business logic and data persistence, it has two reasons to change and MUST be split. Monitor cyclomatic complexity: high complexity (> 10) is a direct signal of an SRP violation.

- **OCP (Open-Closed Principle)**: Modules should be open for extension but closed for modification. Adding a new behavior should not require editing existing, tested code. Use **Strategy**, **Decorator**, or **Plugin** patterns for varying behaviors (e.g., different payment processors, notification channels, export formats) so each variant is a new class, not a new `if` branch.

- **LSP (Liskov Substitution Principle)**: Subtypes must be fully and transparently substitutable for their base types. If a subclass overrides a method in a way that changes its contract (e.g., throws an exception the parent never did, or returns null when the parent always returned a value), it is an LSP violation. Prefer interfaces over abstract classes to make contracts explicit.

- **ISP (Interface Segregation Principle)**: Do not force clients to depend on methods they will never use. Split fat interfaces into focused, role-specific ones. For example, instead of one `UserRepository` with 10 methods, define `ReadUserPort` (for queries) and `WriteUserPort` (for mutations) separately. A Use Case that only reads should only know about `ReadUserPort`.

- **DIP (Dependency Inversion Principle)**: High-level modules (Application Use Cases) MUST NOT depend directly on low-level modules (Prisma ORM, AWS SDK, HTTP clients). Both must depend on abstractions (Port Interfaces defined in the Application layer). This is the foundation of the Hexagonal Architecture: the Domain and Application layers never import infrastructure packages.

## 3. Clean Code Rules

- **Maximum 3 Arguments**: Functions with 4 or more arguments MUST be refactored to accept a Parameter Object (DTO/Options Object). Long argument lists are hard to read, easy to mis-order, and indicate the function is doing too much.

- **No Flag Arguments**: Boolean arguments that split a function's behavior into two paths are forbidden. A function `send(isUrgent: boolean)` is actually two functions: `sendUrgent()` and `sendNormal()`. Split them. One function — one behavior.

- **Command-Query Separation (CQS)**: A method must be either a **Command** (performs an action, mutates state, returns nothing/void) OR a **Query** (returns data, has zero side effects). Never both. Mixing them makes code unpredictable and hard to test. Example: `getUser()` should never update a counter inside itself.

- **Naming Conventions**:
  - Variables/Functions: `camelCase`. Classes/Types: `PascalCase`. Constants: `UPPER_SNAKE_CASE`. Files: `kebab-case.ts`.
  - Use intention-revealing names. Verbs for methods (`calculateTotal`, `sendNotification`), Nouns for classes (`OrderService`, `UserRepository`). Avoid abbreviations and single-letter variables outside of loop counters.

- **Exceptions over Error Codes**: Use domain-specific, named exceptions (e.g., `UserNotFoundException`, `InsufficientFundsException`) inside the Domain and Application core. Map them to HTTP status codes (404, 400, 422) only at the Entry Point (controller/handler) layer. Never return raw error codes from a Domain method.

- **Don't Repeat Yourself (DRY)**: Centralize logic to avoid duplication — but beware of premature abstraction. The wrong abstraction is worse than duplication. Only abstract when a pattern is proven and stable (the "Rule of Three": abstract after the third repetition, not the first).

- **No Logic in Tests**: No `if` statements, loops, or conditional assertions in test bodies. Use Test Factories and Builders to set up the required state. Test code must be linear and obvious.

- **Self-Documenting Tests**: Test names must describe the full scenario in plain language (e.g., `it('should throw InsufficientFundsException when balance is below the transfer amount')`). A failing test name should tell you _exactly_ what broke, without reading the test body.

## 4. Formatting & Tooling

- Use Prettier/ESLint project defaults. Mandatory 2-space indentation. Trailing commas for cleaner git diffs.
- Strict TypeScript — no `any`. Use interfaces and types for every data boundary.

## 5. Competency Boundary

- Enforced by the **Lead Developer** and verified by the **Technical Reviewer** skill before any PR merge.
