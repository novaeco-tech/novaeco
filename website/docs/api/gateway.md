# Gateway API (`api.novaeco.tech`)

The **Gateway Service** is the unified ingress point for all external traffic entering the NovaEco ecosystem. It implements **Protocol Multiplexing** on Port 443, routing requests to the appropriate internal service based on protocol and path.

---

## 1. REST API (HTTP/1.1)

**Audience:** Web Dashboards, Mobile Apps, Third-Party Integrations.  
**Base URL:** `https://api.novaeco.tech`

### Core Endpoints
| Method | Path | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | **Health Check.** Returns 200 OK if the Gateway is operational. |
| `GET` | `/projects` | **List Projects.** Retrieves active circular economy projects across all sectors. |
| `POST` | `/projects` | **Create Project.** Registers a new project in the ecosystem registry. |
| `GET` | `/lca` | **LCA Data.** Fetches Life Cycle Assessment impact metrics. |
| `POST` | `/dpp` | **Product Passport.** Submits a new Digital Product Passport event. |

### Sector Routing
The Gateway also proxies traffic to specific vertical sectors using path prefixes:
- `/api/agro/*` $\to$ **NovaAgro**
- `/api/trade/*` $\to$ **NovaTrade**
- `/api/material/*` $\to$ **NovaMaterial**

> **Authentication:** All REST requests must include a Bearer Token in the header:
> `Authorization: Bearer <jwt_token>`

---

## 2. gRPC API (HTTP/2)

**Audience:** High-performance Agents, IoT Aggregators, Automated Workers.  
**Base URL:** `api.novaeco.tech:443`

The Gateway inspects the `Content-Type: application/grpc` header to route binary traffic directly to the internal gRPC mesh.

### Supported Services
| Service | Proto Package | Description |
| :--- | :--- | :--- |
| **Auth** | `novaeco.auth.v1` | Token verification and trust profile checks. |
| **Trade** | `novaeco.trade.v1` | High-frequency order matching and settlement. |
| **Infra** | `novaeco.infra.v1` | Real-time IoT telemetry ingestion. |

> **SDK:** External developers should use the generated client libraries (e.g., `novaeco-auth-client`) rather than calling these endpoints manually.

---

## Error Handling

The Gateway enforces standardized error responses for all protocols.

**REST (JSON):**
```json
{
  "error": "Unauthorized",
  "code": 401,
  "message": "Token signature invalid or expired.",
  "trace_id": "req-12345"
}
````

**gRPC:**
Returns standard gRPC Status Codes (e.g., `UNAUTHENTICATED`, `PERMISSION_DENIED`) with detailed error details in the metadata trailers.