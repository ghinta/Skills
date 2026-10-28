# Test Gap Analysis — <service / feature / repository>

**Status:** Evidence-backed / Provisional  
**Inspected scope:** <source, tests, fixtures, CI paths / symbols>  
**Not inspected:** <out-of-scope or inaccessible evidence>  
**Runtime test execution:** Not performed unless separately authorized and verified

## Assessment

<One paragraph: what is demonstrably covered, the most important risks, and the limits of evidence.>

## Findings

| Priority | Status | Behavior and gap | Source + test/CI evidence | Consequence | Suggested scenario and expected outcome | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| P0–P3 | Confirmed / Suspected / Unknown | <observable behavior> | <paths / lines / unavailable> | <impact> | <controlled input -> expected result> | High / Medium / Low |

## Traceability

| Contract / behavior | Existing inspected assertion | Verification status | CI gate, if confirmed | Remaining unknown |
| --- | --- | --- | --- | --- |
| <behavior> | <test path/symbol or not found in scope> | Verified coverage / Confirmed gap / Suspected gap / Unknown | <observed CI evidence> | <specific> |

## Prioritized actions

1. **<highest-value change>** — <test layer, fixture and observable result>
2. **<next action>** — <why this matters>
3. **<optional follow-up>** — <only if supported>

**Blockers / missing evidence:** <test files, contracts, gate configuration or run reports needed>  
**Residual risk:** <consequences of what remains unverified>

Remove irrelevant sections. Never fabricate tested outcomes, filenames, numerical coverage or test history. Treat this template as an output in the conversation, not permission to modify files.
