# Grill Me — selective question bank

This is a source of **possible prompts**, not a questionnaire. Use only decision-relevant questions on the current frontier. Each should have a rationale, a recommended answer, and a credible trade-off. Don't ask for facts already supplied or verifiable through authorized read-only tools.

## Goal and evidence (root decisions)
- What problem or objective matters, for whom, and what would count as success?
- What makes action worthwhile compared with doing nothing?
- Which assumption, if false, invalidates the proposal?
- What observation or inexpensive experiment would change your mind?

## Scope and priorities (after goals)
- What is essential for the next milestone, and what is explicitly out?
- What is the cheapest reversible option that still tests the key hypothesis?
- Are two stated goals in conflict (speed vs. reliability, cost vs. control, etc.)?
- Who has authority to make the decision, and who needs to be consulted?

## Alternatives and commitment (after constraints)
- What other practical route exists, and what do we lose by choosing it?
- Which trade-off is most costly to reverse? Can we defer that choice?
- Is an existing product, process change, or smaller prototype enough?
- When would we stop, pivot, or revisit this decision?

## Software-project branches (only when applicable)
- **Users -> workflow -> MVP:** Who uses the system first? What is the smallest end-to-end valuable journey?
- **Data classification -> trust boundaries -> integration:** Who owns/accesses data? Are third-party transfers permitted? What authorization and retention constraints apply?
- **Critical failure -> recovery objective -> operations:** What must survive downtime? Who runs backups, updates, monitoring, and incident response?
- **Workload -> quality requirements -> technology:** What measurable limits justify a framework, data store, or distributed design?
- **Success criterion -> experiment -> delivery:** What evidence shows the MVP worked, and what would invalidate the investment?
- **Team, budget, delivery:** Which resource, approval, dependency, or ongoing maintenance cost is the real blocker?

## Interview discipline

Prioritize decisions over trivia. Recommend without steering toward automatic agreement. A user's "unknown" is a legitimate answer; mark the item **Assumed**, **Open**, or **Deferred** and identify the verification needed. Do not ask questions about a dependent branch before its prerequisite is settled.
