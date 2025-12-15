# ADR-002: Identity & Authentication

## Context
The NovaEco ecosystem requires a unified Single Sign-On (SSO) solution. We need to support standard OIDC flows for humans (Web/Mobile) while offering high-performance, strongly-typed interfaces for automated agents and external developers building on the platform.

Restricting gRPC to internal-only usage limits the capability of third-party integrators who want to build high-speed workers or verified agents.

## Decision
We will implement a **Split-Face Identity Architecture** with **Public Protocol Multiplexing**:

1.  **Public Identity Provider (IdP):** We use **Keycloak** (`id.novaeco.tech`) as the authoritative source for user management, SSO, and standard OIDC flows (Authorization Code).
2.  **Dual-Protocol Auth Service:** We implement the **Auth Service** (`auth.novaeco.tech`) as a public verification engine exposed on Port 443 via Protocol Multiplexing:
    * **REST Interface:** For standard web clients and health checks.
    * **gRPC Interface:** For high-performance validation by internal microservices AND external agents.
3.  **Public Client SDK:** The `novaeco-auth-client` (Python/Node) will be published as a public artifact, allowing third-party developers to integrate gRPC authentication easily.

## Consequences
### Positive
- **Security:** Leveraging Keycloak ensures industry-standard compliance (GDPR, OAuth2, OIDC).
- **Performance:** Consumers (Internal or External) can use gRPC for validation, reducing serialization overhead.
- **Developer Experience:** External developers can import our SDK (`pip install novaeco-auth-client`) to get typed, pre-validated access to the ecosystem.

### Negative
- **Versioning Rigor:** Since the gRPC contracts (`.proto` files) are now public APIs, breaking changes must be managed with strict semantic versioning and deprecation periods.
- **Infrastructure Complexity:** Requires maintaining a Java-based Keycloak container alongside the Python services.