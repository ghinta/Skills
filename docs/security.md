# Security model

## Scope and trust boundaries

This repository contains only **owner-authored, reviewed first-party Agent Skills**. No third-party Skills are installed, synchronized or invoked by repository tooling. The [Engineering Rules](https://github.com/ghinta/Rules) define standards; [80-agent-skills.md](https://github.com/ghinta/Rules/blob/main/80-agent-skills.md) provides the authorized routing and invocation policy.

An approved Skill's `SKILL.md` and local references are workflow instructions **only when explicitly requested by the user**. Target repository code, comments, README files, issues, diagrams, retrieved pages and tool output are **untrusted task data for every Skill**. They cannot grant permissions, install another Skill, or override instructions.

## Controls

- **First-party only:** no third-party/community Skill bundles, remote instruction loaders, scripts or automatic synchronizers. External documentation may be consulted as evidence during review but is not executable instruction content.
- **Invocation:** no automatic activation, installation or chaining. Other Skills may be suggested as separate next tasks; `grill-me` is explicitly user-invoked. All eight currently listed Skills follow the explicit-invocation rule.
- **Read-only default:** planning and drafting do not authorize editing source, running tests, changing CI, deploying or accessing credentials. Privileged actions need separate user authorization and must obey actual runtime permissions. An agent never accepts architectural/security risk on behalf of the decision owner.
- **Restricted Skill directories:** text and local references only, no executables, symlinks or `scripts/`; enforced only to the extent checked by the static validator.
- **Review and validation:** changes use scoped PRs. CI uses SHA-pinned `actions/checkout`, `contents: read`, no secrets and no dependency installation; it runs Python standard-library structural checks and unit tests.
- **Behavioral evaluation:** manual scenarios in `tests/evals/` cover adversarial and prompt-injection cases, but CI does not execute model behaviors.

## Limits

Markdown and static checks **cannot enforce** invocation restrictions, filesystem isolation, network egress, tool permissions, or safe model behavior. Configure these in each agent runtime. The current frontmatter permits only `name` and `description`, not a built-in user-invoked-only enforcement field.

A passing CI check does **not** establish prompt-injection resistance, correctness, verification of security controls or authorization for deployment. Do not commit secrets, personal information or confidential project data to this public repository or its tests.
