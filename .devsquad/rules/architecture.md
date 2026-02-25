---
trigger: model_decision
---

# Rule: Application Architecture (Hexagonal / Ports & Adapters)

## 1. Core Philosophy

Every feature MUST follow strict layer isolation. The architecture consists of four layers, each with a single direction of dependency (inward only):

```
Entry Points  →  Application  →  Domain
Infrastructure  →  Application  →  Domain
```

## 2. Layer Definitions

### Domain (Inner Layer — Zero Dependencies)

Pure business logic. No framework imports. No external libraries.

- **Contains**: Entities, Value Objects, Domain Services, Repository Interfaces (Ports), Domain Events.
- **Rule**: If it cannot be tested in pure TypeScript with no mocks, it belongs to a different layer.

### Application (Middle Layer)

Orchestrates the business rules. Depends ONLY on the Domain.

- **Contains**: Use Cases (Command/Query Handlers), Input/Output Ports (Interfaces), DTOs.
- **Rule**: A Use Case invokes Domain logic and coordinates Adapters via Port interfaces only.

### Infrastructure (Outer Layer)

Implements the Ports defined by the Application layer.

- **Contains**: ORM Adapters (Prisma), Cloud SDK clients (AWS SDK), External API clients.
- **Rule**: All cross-cutting concerns (logging, transactions) live here, not in the Domain.

### Entry Points (Outermost Layer)

The interface between the system and the external world.

- **Contains**: API Controllers, Lambda Handlers, CLI Commands, UI Components.
- **Rule**: Entry Points translate external requests into Application UseCase calls. No business logic here.

## 3. Bounded Context Rules

- Each module is self-contained with a well-defined **Public API** (an index/barrel file exporting only what other modules need).
- **No Direct Cross-Module Imports**: Modules communicate via **Integration Events** (flattened DTOs with primitive types only) or via a Public API interface. Never by directly querying another module's repository or database table.
- **Transactional Outbox Pattern MUST be used**: Events MUST NOT be published directly to an external bus (e.g., SQS/SNS) inside the same DB transaction as the domain change. Persist the event to an `Outbox` table first, then use a relay process to publish it, guaranteeing at-least-once delivery consistency.

## 4. Event-Driven Architecture (EDA)

- **Domain Events**: Used within a single Bounded Context. Published by Entities on state change, handled by listeners in the same module.
- **Integration Events**: Used across module boundaries. Must use "Flattened DTOs" (primitive types only) to prevent domain model leakage.
- **Event Resilience**: All async event consumers MUST have a Dead Letter Queue (DLQ) and MUST be fully idempotent (processing the same event twice must produce the same result).

## 5. Structural Layout

```
src/
  modules/
    [module-name]/       # Bounded Context (Hexagonal)
      domain/            # Pure logic & Entities
      application/       # Use Cases & Port interfaces
      infrastructure/    # Adapters (ORM, Cloud SDK)
  shared/                # Generic Kernel (Base Classes, Errors, Utils)
  entry-points/          # Controllers, Lambda Handlers, CLI
```

## 6. Competency Boundary

- The **Solution Architect** is the final authority on these rules.
- Breaking a layer boundary MUST be flagged for **Human Review** with a documented ADR (Architecture Decision Record).
