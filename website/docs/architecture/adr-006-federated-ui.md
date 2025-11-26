# ADR-006: Federated User Interfaces

Date: 2025-11-26
Status: Accepted

## Context
The ecosystem covers diverse domains (Health, Agriculture, Finance, Construction). A single "Monolithic" Frontend trying to serve all these personas would become bloated, hard to maintain, and confusing for users.

## Decision
We will adopt a **Federated UI** strategy. Each Pillar (e.g., `novaagro`, `novafin`) will develop and host its own lightweight frontend application tailored to its specific user persona.
These apps will be stitched together via a shared **Identity/SSO** session.

## Consequences
### Positive
- **Decoupling:** The `Agro` team can update their UI without breaking `Health`.
- **Performance:** Users only load the JavaScript/Assets relevant to their current context.
- **Simplicity:** Interfaces remain focused on specific domain tasks.

### Negative
- **Consistency Risk:** Requires a strong Design System to ensure apps look like they belong to the same family.
- **Navigation Friction:** Moving between apps requires handling cross-domain navigation and auth persistence.