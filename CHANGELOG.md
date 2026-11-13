# Changelog

Notable changes to the skill collection are recorded here.

## Unreleased

### Changed
- Add an offline, dependency-free Rules/Skills routing drift checker, eleven unit tests, and a read-only GitHub Actions Rules comparison on PRs, main pushes, weekly runs and manual dispatch.
- Align all eight Skills in README with Rules routing and explicit invocation; generalize Security and AGENTS documentation.

### Added
- `documentation` skill: short-first technical docs, TL;DR/navigation, tables, selective Mermaid/C4, change/ADR maintenance, release-version preflight and 22 manual evaluations.
- `adr-authoring` skill for drafting, improving and superseding architectural decision records, with local lifecycle guidance, Markdown template and 18 behavioral scenarios.
- `threat-modeling` skill with STRIDE-based analysis, interactive learning, DFD-like Mermaid template, qualitative risk register and 18 manual evaluation scenarios.
- `test-gap-analysis` skill for evidence-based audit of assertions, contracts, security boundaries and CI gaps, with prioritized improvements.
- `testing-strategy` skill for risk-based verification plans, scenario traceability, CI/release gates, and manual evaluation cases.
- `grill-me` skill: critical decision interviews for ideas, plans, and technical choices; decision tree, frontier, living decision log, and optional Decision Brief.
- Manual behavioral and prompt-injection evaluation scenarios for `grill-me`; validator regression for multiple skills.
- Initial agent-neutral repository structure and security policy.
- `architecture-review` skill for evidence-based, read-only architecture reviews.
- Dependency-free validation, unit tests, and documented manual evaluation cases.
- `architecture-design` skill for option-driven architecture proposals, C4 diagrams, ADR drafts, and risk-based validation plans.
