# Qualitative risk assessment and disposition

Use a small, transparent **qualitative** model. These terms are planning aids, not CVSS, likelihood statistics, or a universal organizational risk policy. Apply the project's documented risk methodology when locally available.

## Separate evidence from risk

Record for each `TH-001`:
- **Evidence level:** `Hypothesis` (possible given an assumption), `Design-supported` (architecture or configuration confirms the relevant pathway), `Observed weakness` (specific missing/ineffective control evidenced), or `Demonstrated failure` (supported by an actual authorized test or incident report). These labels must never imply a test was run by this skill.
- **Impact:** `Critical`, `High`, `Medium`, `Low` or `Unknown`, based on plausible confidentiality, integrity, availability, operational and legal consequences. Don't invent regulatory violations.
- **Exposure:** `High`, `Medium`, `Low` or `Unknown`: reachability, attacker capability, affected principals, shared boundary and constraints. **Unknown is not Low**.
- **Confidence:** `High`, `Medium` or `Low`, measuring how well the scenario is evidenced, not its seriousness.
- **Inherent risk:** qualitative priority **before** considering controls, with a one-line justification.
- **Residual risk:** reassess **after documented existing or proposed controls**, explicitly noting whether the control is only planned. If its effectiveness is unknown, mark residual `Unassessed` or `Provisional`.

## Prioritization guidance

- **Critical:** credible potentially catastrophic harm with meaningful exposure and inadequate controls evidenced. Requires immediate decision; do not use as a dramatic label for a merely imaginable scenario.
- **High:** credible material confidentiality, integrity, availability or control-boundary failure.
- **Medium:** important but bounded harm or meaningful uncertainty requiring planned mitigation/validation.
- **Low:** limited consequence and reachability with reasonably understood controls.
- **Unassessed:** insufficient information to justify a meaningful priority.

There is no automatic multiplication of ordinal labels, and a plausible threat is **not** a confirmed exploit. Explain reasoning instead of inventing numerical risk scores or probability claims. If evidence is thin but potential impact high, flag **high-impact uncertainty** with an explicit validation step.

## Control and decision lifecycle

| Field | Guidance |
| --- | --- |
| Existing control | Cite a file/config/approved document or mark `Unverified`. Do not infer controls from component names. |
| Proposed response | `Mitigate`, `Avoid`, `Transfer` or `Accept (proposed)`, with rationale and trade-offs. |
| Control status | `Observed`, `Proposed`, `Verification needed`, or `Verified effective` only with independent evidence. |
| Owner | Named person/team only if supplied; otherwise `Unassigned`. |
| Approval | Proposed response is **not** approval. Only an authorized decision owner can accept residual risk. |
| Next check | State a concrete, defensive test/review and the evidence needed to close the uncertainty. |
| Review trigger | New integration, privileged action, tenant boundary, data category, infrastructure topology, policy change or incident. |

## Example of defensible wording

- **Supported:** "The provided API diagram shows a user-to-service trust crossing (TB-01); per-resource authorization has not been evidenced, so TH-001 is an **unverified risk**. Review the actual enforcement path and test denied cross-resource access."
- **Unsupported:** "The API is vulnerable because the diagram does not show a permission check."

Risk-acceptance decisions, implementation of controls, test execution and compliance sign-off are **outside** this read-only skill.
