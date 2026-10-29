# Test gap analysis — selective review heuristics

Use only for relevant behaviors. This reference is not a required checklist and does not replace project-local testing rules.

## Trace evidence

For a high-risk behavior, follow the chain:
1. **Expected contract / source implementation:** feature, endpoint, invariant or requirement with file/path.
2. **Test setup:** fixture, actor and role, state, parameter, dependency, trigger.
3. **Assertion:** expected observable result, persisted effect, rejection or failure handling.
4. **Boundary realism:** mock vs real provider/database/identity or contract check.
5. **Enforcement:** applicable required CI test job, trigger/path filters, skip/xfail and result evidence if available.

An uninspected stage is an evidence gap, not automatically proof of a testing defect.

## Patterns worth investigating

| Observed pattern | Possible weakness | Targeted follow-up |
| --- | --- | --- |
| Assertion checks only successful status / non-null | Wrong content or state change still passes | Assert precise output, business invariant, state or error contract |
| Snapshot-only tests | Behavior may change without a meaningful failure | Targeted state and interaction assertions |
| Excessive internal mocking | Provider contract drift or actual integration failure | Real-boundary integration or consumer/provider contract verification |
| Only authorized actor exercised | Cross-tenant or wrong-role access is unchecked | Explicit denial cases at server-side authorization boundary |
| No invalid transition, concurrent write or repeat call | Integrity and idempotency issues could be missed | Failure, transactional, concurrency and replay cases |
| Regression test misses original bug input | Defect can return undetected | Precise pre-fix reproduction and expected post-fix behavior |
| Uncontrolled clock, randomness or locale | Nondeterminism / flaky builds | Controlled time/locale; clear synchronization and cleanup |
| Migration tested only with empty data | Backfill, versioning or rollback not verified | Representative synthetic migration and mixed-version cases |
| Required test skipped/xfail or not wired into CI | Merge gate cannot detect regression | Inspect condition, identify contract and propose enforceable gate |
| Tests exist but contain no meaningful assertion | Executed code without behavior protection | Explain what regression test would fail on |

Treat these as **hypotheses** until verified against actual source and test logic.

## Evidence status vs priority

- **Verified coverage:** inspected, credible assertions; *execution success remains unverified* unless run evidence exists.
- **Confirmed gap:** concrete tested behavior or enforced gate demonstrably insufficient.
- **Suspected gap:** test not located in bounded inspection or evidence incomplete.
- **Unknown:** outside scope or inaccessible.

Assess **impact (P0–P3)** separately from confidence (High/Medium/Low). A serious *potential* security failure is not automatically a confirmed vulnerability.

## Recommendations

For each high-value test proposal, include:
- Controlled **given/when/then** inputs and observable expected outcome.
- Focused unit/component/contract/integration/E2E layer chosen by the actual boundary.
- Synthetic or anonymized fixtures and reliable isolation.
- PR/MR or release check that should enforce the behavior where warranted.
- Minimal verification step to confirm both the gap and improvement.

Never prescribe real credentials or private production records. Diagnose flakiness rather than masking it. A strong test is more useful than several shallow ones.
