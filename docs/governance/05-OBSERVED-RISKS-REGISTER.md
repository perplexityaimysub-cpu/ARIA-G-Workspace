# 05 OBSERVED RISKS REGISTER

This register records observations and risks identified during prior tasks (specifically Mission 1). It is maintained purely as an evidence log. 

**DO NOT** interpret these entries as active defects in any existing workflow. **DO NOT** propose or autonomously implement workflow changes based on this document.

## Product-content observations awaiting a future workflow-change phase

The following observations relate to the quality and consistency of product content generated in prior phases. They are documented here to inform future, deliberate workflow redesigns.

### 1. Unsupported Superiority Claims
*   **Observation:** Marketing copy and SEO descriptions frequently included unsupported superiority language (e.g., "complete", "professional", or "best choice") without corresponding factual backing in the Evidence Pack.
*   **Risk:** Dilutes Iranian Trust signals (R5) and violates strict fact-based copywriting rules (R1) by introducing hallucinations.

### 2. Health, Safety, and Performance Claims Without Source Linkage
*   **Observation:** Unsupported health/safety or certification claims, as well as performance claims such as fast drying or impact resistance, were present in the final output. While terms like "acid-free" may exist in structured product data, their primary evidence source was not traceable in the reviewed files.
*   **Risk:** Significant liability and trust risk; breaks the fundamental rule of the R11 research protocol.

### 3. Weight/Content Discrepancies
*   **Observation:** Discrepancies were noted between the "Net Weight" or "Gross Weight" fields, and the actual shipping weight required for Shopfa postage calculations. Additionally, piece counts (e.g., "pack of 12" vs "1 dozen") were inconsistently formatted.
*   **Risk:** Direct impact on e-commerce logistics, shipping cost calculations, and customer expectations.

### 4. Parent-Versus-Variant Ambiguity
*   **Observation:** Complex products (like pens with multiple tip sizes or notebooks with multiple cover designs) lacked a clear architectural distinction between the "Parent" product definition and its specific "Variants".
*   **Risk:** Leads to duplicated SKU generation efforts (R4) and messy taxonomy structures in Shopfa.
