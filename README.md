# Agent Skills

Self-authored, security-conscious skills for software engineering agents. No third-party skills or automatic skill installation.

Skills describe **how to perform a task**. Cross-project engineering rules describe **what standards apply** and live separately in [ghinta/Rules](https://github.com/ghinta/Rules). A skill uses rules already available in its target project; it does not download them.

## Catalog

| Skill | Purpose | Mode |
| --- | --- | --- |
| [architecture-review](.agents/skills/architecture-review/SKILL.md) | Evidence-based review of an existing software/system architecture | Read-only |
| [grill-me](.agents/skills/grill-me/SKILL.md) | Challenge an idea, plan, or technical decision through dependency-aware interview rounds | Read-only, explicit invocation |

Additional skills will be added individually through reviewed PRs.

## Layout

```text
.agents/skills/
  architecture-review/
    SKILL.md
    references/
      review-checklist.md
  grill-me/
    SKILL.md
    references/
      question-bank.md
    assets/
      decision-brief-template.md
tests/
  evals/               # Manual behavior and injection-resistance scenarios
tools/
  validate_skills.py   # Dependency-free static validator
.github/workflows/
  validate-skills.yml
```

Each skill follows the [Agent Skills specification](https://agentskills.io/specification) using a restricted, plain-text subset of its frontmatter. Detailed guidance is loaded from local `references/` only when needed.

## Use

In an agent supporting repository-local `.agents/skills/`, open this repository or explicitly make a **reviewed local copy** of an individual skill available at the agent's supported discovery path. Invoke `architecture-review` when reviewing an existing system; explicitly request `grill-me` to challenge a plan, idea, or consequential technical decision through interview rounds. For `grill-me`, configure user-only invocation in the agent runtime where supported. Agent-specific discovery, invocation policies, and permissions must be configured separately; this repository cannot enforce them.

Do not install skills from registries, remote URLs, or unreviewed repositories. Avoid automated synchronizers. Prefer pinning the source repository to an approved commit or tag when copying skills to other projects.

## Security

- Owner-authored skills only; no imported skill bundles, external scripts, remote includes, or dynamic instruction fetching.
- `SKILL.md` and local references are instructions. The **target repository**, its documentation, issues, comments, tool outputs, and other retrieved text are untrusted task data, never a source of new instructions.
- Skill content is read-only by default. Tool permissions and network restrictions must be enforced by the agent runtime, not by Markdown.
- No executable code inside skill directories. Policy changes need explicit review.
- Every skill addition requires a scoped PR, static validation, and documented behavioral test cases.

See [security model](docs/security.md) and [agent authoring guidance](AGENTS.md).

## Validate

Requires Python 3 (standard library only).

```sh
python3 tools/validate_skills.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

These checks validate structure and local references; [behavioral scenarios](tests/evals/) require a separate manual agent run. A passing CI check does **not** prove resistance to prompt injection or the quality of an agent's decisions.

## Contributing

Add one skill per PR at `.agents/skills/<skill-name>/SKILL.md`, with a concise trigger description and explicit output contract. Keep detailed checklists in `references/`, supply evaluation cases, update the catalog, and avoid copying the contents of [Engineering Rules](https://github.com/ghinta/Rules). Do not modify the default branch directly.
