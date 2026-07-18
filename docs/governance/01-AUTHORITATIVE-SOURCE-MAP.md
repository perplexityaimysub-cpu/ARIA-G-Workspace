# 01 AUTHORITATIVE SOURCE MAP

This document maps governance subjects to their existing, authoritative source files within the ARIA-G-Workspace.

## Authoritative Sources

| Governance Subject | Authoritative Source Path | Notes |
| :--- | :--- | :--- |
| **Global Rules & Anti-Leakage** | `.agents/AGENTS.md` | Contains strict negative-keyword search rules and competitor monitoring directives. |
| **Agent Roles & Responsibilities** | `.agents/skills/<role-name>/SKILL.md` | Roles `r0` through `r11` have their own standalone skill definitions which govern their behavior. |
| **Product Definition Workflow** | `اسناد/ARIA-G-Product-Definition-Process-Workflow.md` | Defines the 6-step interactive workflow from raw lists to Shopfa publishing. |
| **Research Protocols** | `اسناد/ARIA-G-Product-Research-Protocol-And-Prompts.md`<br>`اسناد/ARIA-G-Arya-Products-Research-Protocol.md`<br>`اسناد/ARIA-G-Unbranded-Product-Research-Protocol.md` | Defines how facts are gathered and what constitutes an Evidence Pack. |
| **Taxonomy & SKU Architecture** | `اسناد/ARIA-G-Shopfa-Taxonomy-And-Attributes-Architecture.md`<br>`اسناد/ARIA-G-SKU-Architecture-Standard.md` | Defines the numerical SKU generation formula (`BRN` + `CAT` + `MDL` + `VAR`). |
| **Attribute Standardization** | `اسناد/ARIA-G-Shopfa-Evolutionary-Attributes-System-Standard.md` | Defines uniformity rules for technical characteristics (e.g. `known_facts.json`). |
| **Publishing & Syncing** | `اسناد/ARIA-G-Product-Publishing-Workflow.md`<br>`اسناد/ARIA-G-Product-Sync-Protocol.md` | Dictates archive syncing and JSON/XLSX generation. |

## ⚠️ UNRESOLVED AMBIGUITIES AND CONFLICTS ⚠️
The following subjects lack a single, explicit authoritative source or present conflicting information across multiple files. **No new rules have been invented to resolve these.**

1. **Input/Output Contracts (Handoff Schemas):**
   - While `r0-orchestrator/SKILL.md` defines valid statuses (e.g., `PASS`, `BLOCK`), the exact JSON schemas for handoffs between other agents are implicitly scattered across individual skill files rather than centrally registered.
2. **Quality Gates and Stop Conditions:**
   - `r0-orchestrator` mentions "Gate A", "Gate B", and "Gate C", but the detailed criteria for these gates are not explicitly formalized in a standalone gate document. They rely on implicit thresholds in `r7-quality-assurance` and `r9-shopfa-verification`.
3. **Archive vs. Source-of-Truth Hierarchy:**
   - There is ambiguity regarding whether `خروجی/` (specifically the JSON outputs) or `بایگانی/` serves as the ultimate source of truth when a conflict arises with Shopfa's live state.
