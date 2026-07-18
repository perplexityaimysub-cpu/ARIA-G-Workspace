# 03 ROLE RESPONSIBILITY AND HANDOFF MAP

This document maps the existing roles within the ARIA-G-Workspace and explicitly categorizes their authority level (Producer, Reviewer, Approver, Blocker, Source Owner).

## Role Map

| Role ID | Role Name | Type | Verification Status | Key Responsibility |
| :--- | :--- | :--- | :--- | :--- |
| **R0** | Orchestrator | Approver / Blocker | VERIFIED | Central supervisor and release authority. Classifies tasks, creates Task Cards, issues final release decisions. (as per SKILL.md) |
| **R1** | Content Production | Producer | UNVERIFIED | Copywriter drafting Persian page descriptions and specification tables based strictly on Evidence Pack. |
| **R2** | SEO SERP Intelligence | Producer / Reviewer | UNVERIFIED | Analyzes search intent, target keywords, and competitor SERP structures. Generates semantic SEO guidelines. |
| **R3** | Internal Linking | Producer | UNVERIFIED | Evaluates and places internal links using the merchant's category tree. |
| **R4** | Schema Entity Graph | Producer | UNVERIFIED | Generates valid JSON-LD structured data schema blocks based on verified specifications. |
| **R5** | Iranian Trust | Reviewer / Blocker | UNVERIFIED | Enforces Iranian trust signals including ENAMAD compliance and consumer protection warning layouts. |
| **R6** | UX CRO | Producer / Reviewer | UNVERIFIED | Optimizes layout readability, call-to-actions, specificity gates, and executes the Horoscope Test. |
| **R7** | Quality Assurance | Reviewer / Blocker | UNVERIFIED | Audits final generated copy and schemas against the Quality Scoring Rubric. Reports score and flags. |
| **R8** | Strategy Conflict Resolution | Reviewer | UNVERIFIED | Analyzes clashing constraints between SEO, UX, and Trust roles. Enforces Conflict Resolution Protocol. |
| **R9** | Shopfa Verification | Reviewer / Blocker | UNVERIFIED | Verifies Shopfa platform settings, dashboard constraints, and verified vs verification-required boundaries. |
| **R10** | Shopfa Integration | Source Owner | UNVERIFIED | Integration module for structured local-only data ingestion and CMS sync. |
| **R11** | Research Intelligence | Source Owner / Producer | UNVERIFIED | Collects public product specs, compiles Evidence Pack. Generates Deep Research briefs. |

## Handoff Gaps and Missing Fields

While R0 defines valid handoff statuses (`PASS`, `PASS_WITH_CONSTRAINTS`, `REVISE`, `BLOCK`, `RESEARCH_AGAIN`, `HUMAN_DECISION_NEEDED`, `NOT_APPLICABLE`), the exact data structure exchanged between the other agents remains underspecified in the current implementation.

### Observed Gaps:
1. **Schema Deficits:** There is no centralized JSON schema file defining the exact structure of an "Evidence Pack" passed from R11 to R1.
2. **Review Feedback Loop:** When R7 blocks a task and sends it back for revision, the explicit format of the "correction payload" sent back to R1 is not strictly typed.
3. **Traceability in Handoffs:** Handoffs do not currently enforce a strict attachment of the rule IDs or source document paths that led to a specific decision.

> [!NOTE]
> These gaps are documented here for observation only. **Do not create or enforce new workflow steps to fix them during this task.**
