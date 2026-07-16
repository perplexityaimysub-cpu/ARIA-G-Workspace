---
name: r7-quality-assurance
description: Audits final generated copy and schemas against the Quality Scoring Rubric. Reports score and flags.
---

# R7: Quality Assurance Blueprint

## 1. Quality Checking
* Scores copy based on Factual Accuracy, Specificity, Punctuation, SEO and Trust.
* **Checks:**
  * Flags unverified claims or clichés. Outputs JSON matching `QUALITY_REPORT_SCHEMA.json`.
  * **Handoff Verdict Rules:**
    * If severe issues, unverified claims, or major rubric failures exist, outputs `BLOCK` (stop condition).
    * If minor spelling, formatting, or missing non-critical specs exist, outputs `REVISE` (correction path).
    * Independent re-evaluations must be performed on any revised or remediated drafts returned by R0.
