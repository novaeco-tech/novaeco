# API Overview

The NovaEco exposes its ecosystem capabilities through a unified **Multiplexed Gateway** (`api.novaeco.tech`) and a split-stack Identity infrastructure.

## Principles
- **Unified Entry Point:** All external traffic—whether REST (Web/Mobile) or gRPC (Agents/IoT)—flows through `api.novaeco.tech` on Port 443.
- **Protocol Multiplexing:** The Gateway automatically routes traffic based on protocol (`HTTP/1.1` vs `HTTP/2`) and content type.
- **Secure Access:** All requests require a valid JWT issued by the public Identity Provider (`id.novaeco.tech`).
- **Strong Contracts:** Internal services communicate via strict gRPC ProtoBuf contracts, which are also exposed to external high-performance clients.

## Available Services

### 1. Core Infrastructure
| Service | Host | Protocol | Purpose |
| :--- | :--- | :--- | :--- |
| **Gateway** | `api.novaeco.tech` | REST & gRPC | Central ingress for data, orchestration, and routing to all sectors. |
| **Identity** | `id.novaeco.tech` | HTTPS (OIDC) | Public Identity Provider (Keycloak). Handles Login, Sign-up, and Token Issuance. |
| **Auth** | `auth.novaeco.tech` | gRPC | High-speed Token Verifier and Trust Anchor for microservices. |

### 2. Sector APIs
Specific verticals (e.g., NovaAgro, NovaTrade) are accessible via the Gateway using path-based routing:
- **REST:** `https://api.novaeco.tech/api/agro/...`
- **gRPC:** `novaeco.agro.v1.AgroService` (via `api.novaeco.tech:443`)

---

## Related Pages
- [Gateway API](./gateway.md) — Endpoints and Routing.
- [Auth & Identity API](./auth.md) — OIDC Flows and Token Verification.
- [API Examples](./examples.md) — cURL and Python snippets.
- [API Testing](./testing.md) — How to validate your integration.
- [Developers: Setup](../developers/setup.md) — Get your local environment running.
