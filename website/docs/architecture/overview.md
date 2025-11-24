# Architecture Overview

The Nova Ecosystem Core is a monorepo containing the four central services that power the platform.

- **Gateway (/api)** — Central REST API Gateway (Python/Flask).
- **Dashboard (/app)** — Mission Control dashboard (Python/Flask).
- **Identity (/auth)** — SSO & Identity provider (Python/Flask).
- **Docs (/website)** — Public documentation site (Node.js/Docusaurus).

## Design Principles
- Scalability
- Transparency
- Interoperability

---

## Related Pages
- [ADR-001: Core Services](./adr-001-core-services.md)
- [ADR-002: Identity & Authentication](./adr-002-auth.md)
- [ADR-003: API Gateway](./adr-003-api-gateway.md)
- [ADR-004: Documentation Site](./adr-004-docs-site.md)
- [Requirements Overview](../requirements/functional.md)

---

[⬅️ Back to Intro](../intro.md)

[Next: Functional Requirements ➡️](../requirements/functional.md)
