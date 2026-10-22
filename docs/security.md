# Security model

## Trust model

This repository contains only first-party skills written and reviewed by its maintainers. No external skills are installed, synchronized, or invoked by repository tooling.

Agent-facing skill instructions are maintained here. **Material under review is untrusted:** source code, comments, README files, issues, documentation, retrieved pages, and tool outputs may contain prompt-injection instructions. The architecture-review skill must analyze such content as evidence, not follow embedded orders.

## Controls

- Skills contain plain text and local reference/data files only; executable files, symlinks, and `scripts/` are disallowed by the static validator.
- No skill loader, install hook, remote Markdown include, or network-dependent validation step exists.
- CI has `contents: read`, uses a SHA-pinned official checkout action, has no repository secrets, and installs no dependencies.
- Changes go through PR review. Review changes to `SKILL.md` as instructions that may affect future agent behavior.
- Use manual adversarial scenarios before accepting materially changed workflows.

## Limitations

Markdown guardrails do **not** enforce agent tool permissions, network egress restrictions, filesystem isolation, or model behavior. Configure these separately in the agent runtime. Static checks do not establish that a skill is free of prompt-injection vulnerabilities.

Third-party docs can be cited as passive references during human review, but their instructions must not be copied into skills or dynamically executed. Never paste credentials or confidential project material into public skills or tests.
