# 04 DECISION AND EVIDENCE TRACE SPECIFICATION

## ⚠️ NON-ENFORCING STATUS ⚠️
This specification defines a **documentation-only trace format** for understanding and tracking agent decisions. 
**It is strictly optional and non-enforcing at this time.** Do not alter existing prompts, workflows, or handoffs to require this structure. It exists solely to provide a theoretical framework for future traceability improvements.

---

## Trace Structure

When a future phase mandates explicit traceability, the following JSON/Markdown structure should be used to record the state of a task as it passes between agents.

```json
{
  "trace_id": "Unique identifier for this specific handoff event",
  "task_id": "The parent Task Card ID from R0",
  "active_roles": ["R11", "R1"],
  
  "source_paths_used": [
    ".agents/AGENTS.md",
    "اسناد/ARIA-G-Product-Research-Protocol-And-Prompts.md"
  ],
  
  "evidence": {
    "verified_facts": [
      {"fact_id": "F-001", "claim": "Product weight is 150g", "source": "Torob verified listing"}
    ],
    "assumptions": [
      {"assumption_id": "A-001", "claim": "Packaging is assumed cardboard based on image analysis", "risk_level": "LOW"}
    ],
    "unknowns": [
      "Exact SKU from manufacturer"
    ]
  },
  
  "decision_gate": {
    "gate_name": "Gate A (Evidence Sufficiency)",
    "result": "PASS_WITH_CONSTRAINTS",
    "evaluating_role": "R0",
    "reasoning": "Sufficient facts gathered, but packaging type remains an assumption. Proceeding to R1."
  },
  
  "next_owner": "R1"
}
```

## Trace Fields Defined
- **task_id / trace_id:** Ensures correlation across multiple agent turns.
- **active_roles:** Who is currently possessing and processing the token.
- **source_paths_used:** Explicit links to the files in `01-AUTHORITATIVE-SOURCE-MAP.md` that governed the current decision.
- **verified_facts:** Data points that have passed the validation rules (e.g., negative-keyword filtering).
- **assumptions:** Unverified data points being carried forward. Must be explicitly flagged.
- **unknowns:** Data points required by the schema but completely missing.
- **decision_gate:** The result of the Orchestrator or QA review (`PASS`, `BLOCK`, `REVISE`, etc.).
- **next_owner:** The next role in the workflow sequence.
