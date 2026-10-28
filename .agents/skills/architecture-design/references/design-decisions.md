# Architecture design: decision and diagram guidance

A selective reference, not a universal checklist. The project's own accepted rules, ADRs and constraints take precedence. Ask only questions that materially affect the architecture.

## From requirements to constraints

- **Business / use cases:** key actors, core flows, explicit non-goals, critical operations.
- **Quality attributes:** desired availability/recovery, confidentiality and data location, latency/throughput, growth, cost, portability, observability and ownership.
- **Evidence:** source for every hard target; distinguish measured facts, accepted requirements and assumptions.
- **Constraints:** existing technology, migration compatibility, team capability, hosting, licensing, external systems and approvals.

If no numbers are provided, use `TBD`, not fictitious SLAs or benchmarks.

## Compare real alternatives

For a material decision, use a compact matrix with **Option | Advantages | Costs/risks | Constraints met? | Reversibility | Unknowns**. Compare:
- simplicity and operating burden
- data ownership and integration contracts
- testability and failure isolation
- security boundaries and data-sovereignty impact
- migration effort and reversibility
- performance/resource claims only where substantiated

Typical alternatives include an existing modular application vs a new service, a simple synchronous workflow vs asynchronous messaging, or extending an approved data store vs adding another. Do not force any particular pattern.

## C4 model: what belongs at each level

- **System Context (L1):** system in scope, people, and external software systems. Label relationships with their purpose.
- **Container (L2):** software applications/services and data stores **inside** the system boundary. Label responsibilities, technologies only if known, interfaces, and interactions. C4 container does **not** mean Docker container.
- **Component (L3):** optional internal components **inside one selected container**; do not draw every class.
- **Code (L4):** generally unnecessary for an architecture proposal.
- **Dynamic/deployment diagrams:** optional for critical journeys, runtime communication, geographic/data-residency or availability issues.

Keep names consistent across levels. Do not misrepresent proposed components as existing. Prefer the project's existing diagram-as-code notation. If no rendering support exists, supply clearly labeled text diagrams, not unvalidated claims of generated assets.

## Risks, boundaries, and interfaces

For each important boundary, make the following explicit where relevant:
- Who owns the data, schema, mutations, lifecycle and access policy?
- What are the API/event/message contracts, version and error semantics?
- What is trusted? Where is identity, authorization and input validation enforced?
- Which failures are expected and how are timeout, retry, replay, idempotency and partial writes handled?
- Who operates and monitors it? How are upgrades, secrets, migrations, restores and rollback managed?
- What tests or experiments would verify that the design actually meets quality goals?

## ADR decision threshold

Draft an ADR for choices with enduring consequences: new infrastructure/data stores, cross-boundary integration patterns, significant security policy, major framework, deployment/data residency, or a compatibility-breaking change. An ADR is **not** necessary for routine implementation details.

- Use `Proposed` until a decision maker accepts it.
- Capture context and constraints, considered alternatives, recommended decision, both positive and negative consequences, and conditions for revisiting.
- Do not create filenames or edit a project's ADR directory unless specifically requested. If requested, follow local naming and lifecycle conventions.
