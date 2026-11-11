# Documentation change impact and release/version discipline

Follow the project's actual Engineering Rules, ADRs and release policy. This is a **documentation preflight**, not authorization to deploy or create tags.

## Changes to document

| Change | Required review |
| --- | --- |
| User-visible feature or bug fix | README/usage, CHANGELOG, release notes if released |
| New API, configuration or permission | Contract/setup docs, security/operations, changelog |
| Architecture, data ownership or trust boundary | Current C4 diagrams and relevant ADR; distinguish proposed from deployed |
| Migration or incompatible format | Migration, backward compatibility, recovery/rollback, breaking-change notes |
| New-code production deployment | Version/release gate, changelog, release provenance and approval |
| Documentation-only or trivial refactor | Relevant page; no artificial ADR or version bump |

Keep changes small and link to existing canonical documentation.

## Release version preflight

1. Inspect manifests, lockfiles, prior release tags, version metadata, CHANGELOG, and the project's versioning policy. Never assume all repositories use SemVer.
2. For a **substantial feature scheduled for release** or a **deployment of changed code/artifacts**, recommend a new release version **before deployment**. When SemVer is adopted, use MAJOR for incompatible public contracts, MINOR for compatible features, and PATCH for compatible fixes. Follow explicit pre-1.0 conventions.
3. If no release policy exists, propose one and request approval. An immutable commit SHA and dated changes may be the established convention for a PoC; don't silently introduce a public version.
4. **Identical artifact redeployment, environment promotion and rollback** should normally retain the existing software version. Record the deployment event separately.
5. If specifically authorized, prepare consistent changes to version manifests, applicable lockfiles, changelog, release notes and metadata. Do not guess generated lockfile changes or create a release/tag without explicit authorization.
6. For automatic deployments from main, identify whether version preparation and required approval/checks happen before merge; recommend a gate if absent rather than secretly editing CI.

## Verification and readiness

- [ ] Immutable source revision/artifact and intended version identified.
- [ ] Current documentation and diagrams describe the release candidate, not only the future target.
- [ ] CHANGELOG summarizes significant behavior, operations and breaking changes.
- [ ] Consequential ADRs are recorded and approval status verified.
- [ ] CI/test/security evidence is checked or explicitly marked Unknown.
- [ ] Migrations, backups, recovery and rollback are documented if applicable.
- [ ] Release owner, approval and deployment method are explicit.

This is a report of readiness and blockers. Never claim a deployment, test, tag or version bump happened unless verified.
