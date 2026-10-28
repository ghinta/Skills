# Test Strategy — <feature / change / system>

**Status:** Proposed / Provisional  
**Scope:** <affected workflows, components and boundaries>  
**Out of scope:** <excluded checks>  
**Evidence:** <requirements, ADRs, inspected tests/CI, or "not available">

## Assumptions and quality goals

| Item | Confirmed / assumed | Source / owner | Uncertainty |
| --- | --- | --- | --- |
| <behavior or target> | <known fact or assumption> | <path, specification or unknown> | <TBD if unavailable> |

## High-priority risks

| Risk / failure mode | Impact and exposure | Priority (P0–P3) | Evidence / open question |
| --- | --- | --- | --- |
| <risk> | <why it matters> | <P0–P3> | <facts vs. assumptions> |

## Test traceability matrix

| Requirement / risk | Concrete scenario and expected observable result | Layer | Priority | Data / environment | Existing / proposed / unknown | Gate |
| --- | --- | --- | --- | --- | --- | --- |
| <contract or invariant> | <trigger/input -> expected state, output or rejection> | <unit / contract / integration / E2E / other> | <P0–P3> | <minimal fixture/setup> | <verified existing or proposal> | <PR/MR, scheduled, release, manual> |

## Test environment and isolation

- **Fixtures and privacy:** <synthetic data, roles, identity, anonymization>
- **Dependencies:** <real boundary, controlled substitutes, cleanup>
- **Determinism:** <time, randomness, concurrency and isolation>
- **Unavailable environments / evidence:** <unknown>

## CI/release quality gates

| Stage | Checks | Required or advisory | Failure signal | Owner / blocker |
| --- | --- | --- | --- | --- |
| Local | <fast feedback> | <...> | <...> | <...> |
| PR/MR | <focused regression and contracts> | <...> | <...> | <...> |
| Scheduled / pre-release | <only justified slower checks> | <...> | <...> | <...> |

## Implementation order and residual risks

1. <highest-risk executable check to implement>
2. <next relevant check>
3. <critical boundary or extended verification>

**Residual risks / deferrals:** <what remains unverified and why>  
**Release or acceptance gate:** <observable criterion or TBD>  
**Reported verification:** <"Planning only; no tests executed" unless actual separate results are supplied>

Delete irrelevant placeholders and sections. Do not fabricate test outcomes, measured thresholds, existing tools or permissions. The template is for a **proposed plan**, not authorization to edit files or run pipelines.
