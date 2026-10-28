# Testing strategy — selective risk and coverage guide

Use this reference to **choose and justify** test types and priorities, not as a checklist to mechanically reproduce. Follow accepted project-specific Testing Rules and existing tools where supplied.

## Risk ranking

Prioritize failure scenarios using qualitative evidence:

| Dimension | Questions |
| --- | --- |
| Impact | Could this expose another user's records, corrupt financial/business data, break a critical journey, or cause long downtime? |
| Likelihood/exposure | Is the path frequently used, newly changed, externally controlled, shared by many services, or historically error-prone? |
| Uncertainty | Are contracts, prior failures, production behavior, test doubles, or operating conditions poorly understood? |
| Detectability/recovery | Would the defect be visible before damage, be reversible, or require costly incident recovery? |

A high-consequence scenario can be P0 even if its likelihood is unknown. Don't invent numeric risk scores. Record the reason and remaining evidence gap.

## Select the verification layer

| Layer | Choose when | Common failure or blind spot |
| --- | --- | --- |
| Focused/unit/property | Validating pure logic, invariants, calculations, transformations, state transitions | Over-mocking private implementation, missing actual boundaries |
| Component/UI | Validating component behavior, form states, interactions, keyboard/accessibility behavior | Snapshots alone miss real behavior |
| API/contract | Public API schema, permissions, error contracts, versions, event structure | Contract mocks drift from providers |
| Integration | Database transactions, file handling, auth provider, queue or real service boundaries | Requires managed test environments and cleanup |
| E2E | A few business-critical multi-component journeys, login/checkout/approval paths | Slower and more brittle; don't test all permutations here |
| Non-functional | Performance/resilience/recovery/security/accessibility when there are relevant risks or requirements | Numbers are meaningless without agreed targets and representative setup |
| Manual/exploratory | New UX, unknown failure modes, incident reproduction, rare edge cases | Requires clear scope and captured findings |

Use the lowest layer that can credibly demonstrate the desired outcome and add a boundary-level check where failure could otherwise go undetected.

## Scenario prompts (only if relevant)

- **Success and domain invariants:** correct output, cross-field consistency, legal state transitions, rounding, invalid transitions.
- **Authorization:** anonymous access, wrong role, cross-tenant or cross-resource access, escalation, revocation; assert denied access **at the trusted boundary**.
- **Bad input:** malformed, blank, oversized, duplicate, unsupported version or unexpected content.
- **Data integrity:** concurrent modification, atomicity, retries after partial failure, duplicate messages, rollback and migrations.
- **External failure:** timeout, dependency outage, partial response, queue backlog, expired token, schema compatibility.
- **Time and localization:** daylight-saving transitions, locale formats, currency/precision, deterministic time handling when applicable.
- **Operations:** restore verification, deployment smoke check, observability, job replay, degraded behavior.
- **UI:** accessibility and keyboard navigation, critical workflows, state changes, error feedback when meaningful.

For a **bug fix**, define reproducible inputs, expected regression assertion, and the intended red/green sequence. For an **integration**, prioritize contracts and failure paths. For a **migration**, include upgrade, mixed-version compatibility, data backfill, rollback safety and integrity checks.

## Data, isolation and flakiness

- Use minimal synthetic fixtures or appropriately anonymized data. Never include real secrets, customer records or unnecessary personal information in tests or reports.
- Control time, random seeds, locale and resource cleanup where relevant.
- Prefer faithful integration checks where fake providers can conceal contract drift.
- If a test flakes, diagnose the underlying nondeterminism; don't normalize flaky tests with unconditional retry or sleep.

## CI and release gates

Use the project's **existing** quality tooling unless change is justified.

- **Developer/local:** fast, focused relevant tests and static checks for rapid feedback.
- **PR/MR:** required behavior/regression checks, affected contracts and security verification where warranted; report failures clearly.
- **Scheduled/extended:** longer suites or representative non-functional tests when they meaningfully reduce risk.
- **Pre-release/deployment:** migration, rollback, critical journeys, smoke checks and recovery probes as justified by release risk.

For each proposed check note trigger, environment, expected signal, **mandatory vs. advisory**, owner and blockers. Prefer measured runtime budgets; do not claim a gate exists or passes without inspecting the actual configuration. Keep coverage, pass rate and mutation metrics as diagnostics unless explicit policy says otherwise. Other scanners and quality checks support, but do not replace, behavioral verification.

## Ownership and handoff

Align a proposed test with a concrete contract/behavior and an accountable owner when known. Preserve acceptance criteria traceability. Label which verification already exists **only if inspected**; list residual risks where validation is infeasible or deferred. A later implementation skill may author tests, but this skill remains a read-only strategy.
