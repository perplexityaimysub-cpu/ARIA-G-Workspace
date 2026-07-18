# 00 READ ME FIRST - ARIA-G Governance Layer

## Scope and Purpose
This `docs/governance/` directory serves as the **strict, non-destructive assistant-coherence hardening layer** for the ARIA-G-Workspace project. 

Its primary purpose is to improve agent coherence, rule fidelity, traceability, and handoff discipline by creating a centralized map of the existing authoritative sources, workflows, roles, and rules.

## ⚠️ CRITICAL NON-DESTRUCTIVE DIRECTIVE ⚠️
**EXISTING WORKFLOWS, RULES, AND ROLES REMAIN UNCHANGED.**

This governance layer is strictly for mapping, observation, and documentation. **It does not implement, redefine, or enforce any new operational behaviors, routing logic, or workflow steps at this time.** 

- No existing file in `.agents/`, `اسناد/`, `بایگانی/`, or `خروجی/` has been modified to create this layer.
- No existing prompt or agent skill definition has been altered.
- All product-content generation workflows remain exactly as they were prior to the creation of this governance layer.

## How Future Agents Must Use These Documents
1. **Reference ONLY:** Agents should consult these documents to understand the landscape of authoritative sources, existing rules, and observed gaps.
2. **No Autonomous Enforcement of New Rules:** Unless explicitly directed by a future, approved owner mandate that alters the existing `SKILL.md` or `.agents/AGENTS.md` files, agents must not enforce the structural trace mappings or experimental workflow gaps observed here.
3. **Traceability:** Agents may reference the documentation-only trace formats defined in this directory to improve their internal memory and reasoning, but must not inject these traces into final output artifacts (like Shopfa metadata or product descriptions) unless the main workflow explicitly requests it.
4. **Authoritative Source Precedence:** `01-AUTHORITATIVE-SOURCE-MAP.md` is a navigation map only. In any conflict, the original referenced source file always has priority. These governance documents never become the ultimate operational authority.

## Directory Contents
- `01-AUTHORITATIVE-SOURCE-MAP.md`: Maps governance subjects to their true source files.
- `02-RULE-AND-WORKFLOW-REGISTER.md`: Inventory of all active rules and workflows.
- `03-ROLE-RESPONSIBILITY-AND-HANDOFF-MAP.md`: Map of existing agent roles and handoffs.
- `04-DECISION-AND-EVIDENCE-TRACE-SPEC.md`: A documentation-only trace format (not yet enforced).
- `05-OBSERVED-RISKS-REGISTER.md`: Log of observed risks and gaps awaiting future resolution.
- `06-NO-CHANGE-VALIDATION.md`: Cryptographic validation that no existing files were altered during the creation of this layer.
