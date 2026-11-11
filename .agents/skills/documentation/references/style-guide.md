# Documentation style — compact, navigable, evidenced

This is project-specific authoring guidance inspired by patterns in the owner's own repositories (including concise Rules indices, domain-focused docs in ÖPUL, C4 diagrams in Bor AG reports, and operational docs in FrischeTische). **Do not copy those repositories' domain text into unrelated projects.** Existing project conventions take precedence.

## Prefer short-first writing

- Open with **what this is, who it serves, and its current state**. Avoid lengthy motivations before the answer.
- For **substantial pages**, place **TL;DR** (or `Kurzfassung` in German) before detailed sections: 2–5 specific sentences or a few bullets. For an already short README, a short opening paragraph may suffice instead of a redundant TL;DR.
- Provide only steps someone needs to act: minimal setup, exact paths/configuration, quick verification, and obvious limitations. Explain **why** when it affects a decision, otherwise link to an ADR.
- Use the project's predominant language and terminology. Do not translate APIs, commands, identifiers or filenames for style alone.
- Use short paragraphs and descriptive headings; avoid repeated boilerplate, filler, aspirational claims, or duplicate explanations of what the code does.

## Navigation and file boundaries

| Document | Keep here | Move/link elsewhere |
| --- | --- | --- |
| `README.md` | Purpose, status, quickstart, minimal usage, docs index | Detailed API, architecture, operations, lengthy troubleshooting |
| `docs/README.md` | Small index by audience/task | Duplicated guides or entire manuals |
| `docs/architecture/` | Current vs target boundaries, C4, data flows, ADR index | Large implementation logs |
| `docs/operations/` | Deployment, configuration, backup/restore, recovery | General product overview |
| `docs/changes/` | Feature rationale, scope, evidence and verification (if project uses it) | Repeated changelog entries |
| `CHANGELOG.md` | Concise released/unreleased changes and breaking notes | Full implementation diaries or duplicate ADR rationale |

**Heuristic, not a rigid limit:** around five or more top-level sections or a long scrolling page merits a **linked table of contents**, especially for a single cohesive topic. If readers have distinct tasks (setup, API, architecture, deployment) split into topic-focused pages and keep an index. Inspect existing project organization before creating new folders.

## Tables and diagrams

- Prefer tables for option comparison, ownership, endpoints, settings, test matrices and release status. Avoid huge prose cells; break out complex explanation under the table.
- Prefer **Mermaid** source for diagrams on GitHub. A diagram must answer a concrete reader question; include a one-line caption/purpose, understandable node names and labeled relationships.
- Use **C4 System Context** for people/external systems and **C4 Container** for deployable applications and datastores when useful. A C4 container is not automatically a Docker container or Pod. Add Component/Dynamic/Deployment views only when they remove meaningful ambiguity.
- Distinguish **current/as-is** from **proposed/to-be** and cite actual code/diagram sources when relevant. Never use a proposed diagram as proof of deployed infrastructure.
- Plain text flow or a compact table may be more useful than a diagram for small features. Never generate decorative or redundant visuals.

## Freshness and claims

- Keep **one canonical explanation** per topic; update references instead of duplicating content in README, docs and ADRs.
- Maintain links and diagrams alongside the code/config changes that make them obsolete.
- Label time-sensitive operational details with evidence/revision when necessary, and avoid stale claims of current deployments.
- Prefer specific, verifiable results and unknowns over unconfirmed success or unnecessary certainty.
