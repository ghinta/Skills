# STRIDE reference — questions for threat discovery

This is original, compact guidance based on the established **STRIDE** threat taxonomy and OWASP-style system decomposition. Use it as a **prompting aid**, not a requirement to invent a threat in every category. Prefer risks grounded in the actual assets, actors, flows and trust boundaries.

## Diagram-first discovery

List:
- **E (External entity):** people, organizations and third-party systems outside the modeled system.
- **P (Process):** active application/service components performing work.
- **D (Data store):** data at rest and its ownership.
- **F (Flow):** data/control exchange, with source, destination, sensitivity and purpose.
- **TB (Trust boundary):** where identities, privileges, policies, tenancy, hosts, networks or data-governance assumptions change.
- **A (Asset):** valuable information, ability or operation requiring protection.

A trust boundary should identify **why** one side cannot safely trust the other. Do not equate a Docker container, namespace, network segment or diagram subgraph with a guaranteed security boundary.

## STRIDE discovery prompts

| Category | Property at risk | Ask at a relevant element/flow | Defensive concept to examine |
| --- | --- | --- | --- |
| **S — Spoofing** | Authenticity | Could a sender or identity be mistaken for another at this boundary? | Strong identity verification and trustworthy service identity |
| **T — Tampering** | Integrity | Could untrusted data or a state transition be modified without proper checks? | Input validation, integrity protection, invariant enforcement |
| **R — Repudiation** | Accountability | Could a significant action become impossible to attribute or investigate? | Tamper-resistant, proportionate audit records with privacy controls |
| **I — Information Disclosure** | Confidentiality | Could sensitive data cross to an unauthorized principal, tenant, log or destination? | Server-side authorization, least-privilege access, minimization and transport/storage protections |
| **D — Denial of Service** | Availability | Could bounded failures or resource exhaustion prevent legitimate operation? | Input/resource limits, isolation, timeouts, resilience, observability |
| **E — Elevation of Privilege** | Authorization | Could a less-privileged principal or component cross a privileged boundary? | Enforce privileges at trusted boundary, minimal capabilities, separation of duties |

For each plausible scenario identify: **threat actor/capability**, **target asset**, **affected element/flow and trust assumption**, **consequence**, **evidence**, **current control (if verified)**, and a **defensive test**. Keep scenarios conceptual and non-operational; no commands, exploit strings or attack walkthroughs.

## Extensions (only when relevant)

- **Personal data:** ask about linkability, unintended inference, collection minimization, retention, secondary use and transparency. STRIDE alone is not a privacy threat model; a **LINDDUN** exercise can deepen the analysis.
- **LLM, RAG and coding agents:** examine boundaries among user instructions, retrieved documents, repository files, model output, tool-call parameters and the actual privilege enforcement point. Treat prompt injection, leakage, excessive agency, source integrity, untrusted outputs and resource exhaustion as possible scenarios; never treat a system prompt as authorization enforcement.
- **Supply chain:** ask who supplies artifacts/models/dependencies, who can update them, and what approvals, pinning and provenance checks apply.
- **Operational boundaries:** privileged automation, backups, recovery and service-to-service identity may require analysis even when not on the user-facing request path.

## Traceability and humility

- Reuse existing approved system/flow IDs where available; otherwise assign stable IDs such as `F-01`, `TB-01`, `TH-001`.
- No threat is **confirmed** merely because its STRIDE category applies.
- Do not assume mitigation from a diagram label (for example, an "auth" box does not prove authorization checks).
- Do not claim a full STRIDE assessment if major components or boundaries were inaccessible. Record the omitted scope explicitly.
