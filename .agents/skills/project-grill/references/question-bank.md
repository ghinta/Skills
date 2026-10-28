# Project Grill — selective question bank

This is a prompt bank, **not** a form and not a mandatory checklist. Select questions with the greatest impact on the current decision frontier. Do not ask questions the user has already answered. Ask for decisions, not discoverable facts. Each question should identify its prerequisites and the consequence of a wrong answer.

## 1. Problem and opportunity (root)

- What concrete pain point exists, for whom, and how do we know? What observation could disprove it?
- What happens if nothing is built? Can a process, configuration, or existing product solve enough of the problem?
- What outcome would make the project worth continuing? Which metric is observable and at what point?

## 2. Users and scope (requires problem and target)

- Who will use it first, and who decides whether it succeeds? Are these the same person?
- What is the smallest end-to-end workflow proving value? What is explicitly out of the MVP?
- Which stated feature is actually a proposed solution rather than a user requirement?
- What happens for an unsupported scenario, an empty dataset, or a failed operation?

## 3. Data and trust (requires user journey and data flow)

- What categories of data are handled, who owns them, and who may access or delete them?
- Which trust boundaries exist (users, services, external providers, AI/agent tools, tenants)?
- Is sending data to an external service allowed? If unknown, prefer a no-external-transfer assumption until confirmed.
- Which privacy, retention, auditability, or regional deployment constraints are real requirements?

## 4. Feasibility and technical choices (requires quality attributes)

- What must be proven before choosing a framework, database, model, or cloud provider?
- Could an existing supported tool meet the needs? Is custom development justified?
- What would invalidate the proposed technical approach? Is a bounded experiment cheaper than committing now?
- What coupling or irreversible migration does the decision introduce?

## 5. Reliability and operations (requires critical workflows)

- What failure is unacceptable? What availability or recovery objective is actually needed?
- Who will operate, monitor, patch, back up, and support this system after release?
- What happens when dependencies fail, traffic changes, or recovery is needed?
- What is the minimum viable deployment, logging, and rollback plan?

## 6. Time, cost, dependencies, and ownership

- Who can decide on scope, access, budget, delivery, and acceptance? Who is a blocker?
- What does the estimate assume, and what uncertainty would dominate it?
- What external approvals, data access, licenses, integrations, or procurement steps may block delivery?
- What can be deliberately deferred without creating a security or data-migration problem?

## 7. Risks, experiments, and stop criteria

- What are the three most damaging ways this initiative can fail?
- Which assumption is both uncertain and expensive if wrong? How can it be tested cheaply?
- Under what observation should the team pivot, reduce scope, or cancel?
- What evidence would support a go/no-go decision at the next checkpoint?

## Decision-dependency examples

- **Target user -> core workflow -> MVP -> architecture trade-offs**. Do not choose a framework before understanding the work.
- **Data sensitivity -> data location/authorization -> integration choices**. Do not propose external processing when data export is not approved.
- **Failure impact -> recovery goals -> deployment complexity**. Do not prescribe HA without a real resilience requirement.
- **Success measure -> validation experiment -> delivery scope**. Do not claim an MVP proves value without a testable outcome.

## Recommendation discipline

Provide a provisional default, supporting rationale, realistic alternative, and what evidence would change the recommendation. When data is missing, prefer minimal reversible commitments. Resist both uncritical agreement and reflexive skepticism.
