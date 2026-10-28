# Proposed Architecture — <system / initiative>

**Status:** Proposed / Provisional  
**Decision owner:** <known owner, otherwise "not assigned">  
**Scope:** <new system or bounded change; explicit non-goals>

## 1. Requirements and assumptions

| Item | Requirement / assumption | Evidence / owner | Confidence |
| --- | --- | --- | --- |
| <functional or quality goal> | <specific goal, or TBD> | <provided source / unknown> | <confirmed / assumed> |

## 2. Architectural options

| Option | Benefits | Costs and risks | Key constraints | Reversibility |
| --- | --- | --- | --- | --- |
| <simpler/incremental> | <...> | <...> | <...> | <...> |
| <alternative> | <...> | <...> | <...> | <...> |

**Recommended direction:** <reasoned recommendation, pending approval if not accepted>

## 3. Target design (to-be)

**System boundaries and responsibilities:** <people, components, external systems>  
**Data ownership and consistency:** <who writes what; invariants>  
**Trust boundaries:** <where authn/authz/input validation applies>

### C4 — System Context
<Diagram in the project's approved text notation, or concise labeled description; show people and external systems.>

### C4 — Container
<Diagram showing applications/services and data stores inside the system boundary; label proposed relationships.>

### C4 — Component (only if justified)
<One container's internal components, otherwise omit.>

## 4. Interfaces, runtime behavior and quality attributes

| Concern | Proposed mechanism | Failure / trade-off | Verification |
| --- | --- | --- | --- |
| <contract / security / resilience / operations> | <...> | <...> | <test / experiment / review> |

Include significant critical-flow or deployment diagrams only when needed.

## 5. Decisions requiring approval

- <ADR subject, recommended option, reason, owner>; draft as **Proposed** using the ADR template.

## 6. Risks, experiments, and incremental delivery

| Risk / missing fact | Consequence | Least-cost validation | Owner |
| --- | --- | --- | --- |
| <...> | <...> | <...> | <...> |

**Delivery slices:** <small independently verifiable increments; no implementation by this skill>  
**Acceptance / decision gates:** <what must be confirmed before committing to the next phase>

Remove sections that add no value. Label the whole design **provisional** if pivotal requirements are unknown. This is an output template, not permission to write project files.
