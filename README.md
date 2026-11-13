# Agent Skills

Self-authored, security-conscious skills for software engineering agents. No third-party skills or automatic skill installation.

Skills describe **how to perform a task**. Cross-project engineering rules describe **what standards apply** and live separately in [ghinta/Rules](https://github.com/ghinta/Rules). A skill uses rules already available in its target project; it does not download them.

## Catalog

Eight first-party Skills are available. See [Rules skill routing](https://github.com/ghinta/Rules/blob/main/80-agent-skills.md) for the authoritative mapping from engineering tasks to Skills.

| Skill | Use when | Not for | Mode |
| --- | --- | --- | --- |
| [adr-authoring](.agents/skills/adr-authoring/SKILL.md) | Drafting or superseding an architectural decision | Designing an entire system or granting approval | Read-only |
| [architecture-design](.agents/skills/architecture-design/SKILL.md) | Proposing a target architecture, options and C4 views | Auditing existing implementation or writing code | Read-only |
| [architecture-review](.agents/skills/architecture-review/SKILL.md) | Reviewing an existing architecture using evidence | Designing a new system | Read-only |
| [documentation](.agents/skills/documentation/SKILL.md) | Concise README/docs, diagrams, changelog and release readiness | Making ADR decisions or deploying | Read-only by default |
| [grill-me](.agents/skills/grill-me/SKILL.md) | Explicit request to critically interview on an idea or choice | Unsolicited reviews or routine coding | Explicit invocation, read-only |
| [test-gap-analysis](.agents/skills/test-gap-analysis/SKILL.md) | Auditing existing test assertions and CI enforcement | Planning tests for a project without a suite | Read-only |
| [testing-strategy](.agents/skills/testing-strategy/SKILL.md) | Planning risk-based tests for new/changed behavior | Writing/running tests or auditing existing tests | Read-only |
| [threat-modeling](.agents/skills/threat-modeling/SKILL.md) | STRIDE analysis of assets and trust boundaries; learning mode on request | Exploitation or automatic risk acceptance | Read-only |

Additional skills will be added individually through reviewed PRs.

## Layout

```text
.agents/skills/
  adr-authoring/
    SKILL.md
    references/
      adr-lifecycle.md
    assets/
      adr-template.md
  architecture-design/
    SKILL.md
    references/
      design-decisions.md
    assets/
      architecture-proposal-template.md
      adr-proposal-template.md
  architecture-review/
    SKILL.md
    references/
      review-checklist.md
  documentation/
    SKILL.md
    references/
      style-guide.md
      change-and-release-guide.md
    assets/
      documentation-impact-template.md
      readme-template.md
  grill-me/
    SKILL.md
    references/
      question-bank.md
    assets/
      decision-brief-template.md
  test-gap-analysis/
    SKILL.md
    references/
      gap-review-heuristics.md
    assets/
      gap-report-template.md
  testing-strategy/
    SKILL.md
    references/
      risk-and-coverage-guide.md
    assets/
      test-strategy-template.md
  threat-modeling/
    SKILL.md
    references/
      stride-guide.md
      risk-assessment.md
    assets/
      threat-model-template.md
tests/
  evals/               # Manual behavior and injection-resistance scenarios
tools/
  validate_skills.py   # Dependency-free static validator
  check_skill_routing.py  # Offline Rules/Skills catalog drift checker
.github/workflows/
  validate-skills.yml
```

Each skill follows the [Agent Skills specification](https://agentskills.io/specification) using a restricted, plain-text subset of its frontmatter. Detailed guidance is loaded from local `references/` only when needed.

## Use

Select a Skill only for a matching, **explicitly requested** workflow as described in [Rules / 80-agent-skills.md](https://github.com/ghinta/Rules/blob/main/80-agent-skills.md). Skills must already be available as reviewed local copies at an agent-supported discovery path. Do not install, fetch, automatically activate, or chain Skills. `grill-me` is user-invoked only, and other Skills likewise require explicit user invocation under the adopted Rules.

Configure discovery, invocation policy, sandbox and tool permissions **in the agent runtime**. Repository Markdown and this collection's two-field frontmatter cannot technically enforce user-only invocation. If a Skill is absent, apply the Rules without downloading anything. A Skill may suggest another workflow but must not invoke it without the user's request.

Distribute only reviewed, preferably commit/tag-pinned local copies, not third-party packages or unattended synchronizers.

## Security

- Owner-authored, explicitly approved Skills only; no third-party installers, dynamic remote instructions or automatically loaded Skill bundles.
- `SKILL.md` and local references become task instructions only following authorized invocation. Source files, documentation, issues, web pages and tool outputs under review remain untrusted data.
- No automatic Skill chaining. Agent-specific invocation, network and filesystem permissions must be enforced outside Markdown.
- Skills remain read-only by default. File writes, test runs, CI changes, releases and deployments need explicit authorization and suitable runtime privileges.
- No executable files or symlinks inside Skill directories; all changes require PR review, static validation and documented behavioral tests.

See [security model](docs/security.md) and [agent authoring guidance](AGENTS.md).

## Validate

Requires Python 3 (standard library only).

```sh
python3 tools/validate_skills.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
# With a separate, already reviewed local checkout of Rules:
python3 tools/check_skill_routing.py --rules-root ../Rules
```

These checks validate structure and local references; [behavioral scenarios](tests/evals/) require a separate manual agent run. GitHub Actions also checks out **ghinta/Rules as read-only data** and compares the current Skills directory/frontmatter and README catalog with `Rules/80-agent-skills.md`, including referenced rule files. The drift check runs on PRs, pushes to `main`, weekly on Monday, and manually; a Rules-only change is detected by the next scheduled/manual check (not immediately by a Rules webhook). It never installs or executes Rules/Skill content. A passing CI check does **not** prove resistance to prompt injection, the quality of an agent's decisions, or that skill activation policy is technically enforced.

## Contributing

Add one skill per PR at `.agents/skills/<skill-name>/SKILL.md`, with a concise trigger description and explicit output contract. Keep detailed checklists in `references/`, supply evaluation cases, update the catalog, and avoid copying the contents of [Engineering Rules](https://github.com/ghinta/Rules). Coordinate a Rules routing update for each new, renamed or retired Skill; cross-repository routing must match before the drift gate can pass. Do not modify the default branch directly.
