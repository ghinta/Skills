# ADR lifecycle and review checklist

Use the target repository's conventions first. This is original guidance informed by established lightweight ADR and MADR-style practices, not a copied third-party skill.

## Decision threshold

Write an ADR for durable trade-offs involving infrastructure, technology, integration, data ownership, security, compatibility, or significant operating cost. Avoid ADRs for trivial implementation choices or repeated explanations of an already accepted decision.

## Status model

| Status | Meaning | Evidence needed |
| --- | --- | --- |
| Proposed | A choice and rationale await approval | Author's proposal, decision drivers and alternatives |
| Accepted | An authorized decision was made | Explicit evidence of approval under local governance |
| Rejected | A proposal was considered but not adopted | Recorded rejection; preserve why |
| Superseded | An accepted decision has been replaced | Reference the newer accepted ADR; preserve history |
| Deprecated | Decision is phased out, if local policy supports it | Transition and owner approved or documented |

Status is **not** implementation progress: an Accepted decision can be unimplemented.

## Numbering and location

- Inspect existing `docs/architecture/adr/`, `docs/adr/`, indices and naming patterns before proposing a file.
- If the current numbering cannot be established, use `ADR-XXXX`; never pretend to reserve a number.
- Keep accepted ADRs immutable in their substantive rationale. For a changed decision, draft a new **Proposed** ADR with `Supersedes: ADR-...`. Mark the old one Superseded only after the replacement is formally accepted.
- Maintain traceability to verified issues, PRs, documentation and decisions; don't invent links.
- Preserve Rejected and Superseded records, which explain historical choices.

## ADR quality review

- Why is a decision needed now? Which requirements and constraints matter?
- What alternatives (including status quo when reasonable) were actually considered?
- Does the chosen option address decision drivers? Are costs, disadvantages and compatibility consequences explicit?
- What is the responsible approval path? Are owner, status and date evidenced?
- What observation would invalidate this decision? What experiment, metric or change triggers reconsideration?
- Are related ADRs and effects on contracts, data, security and operation correctly linked?

If a whole architecture is undefined, the user may need architecture-design first; don't invent an architecture merely to fill an ADR.
