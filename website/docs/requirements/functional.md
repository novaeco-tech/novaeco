# Functional Requirements

These requirements define the **behavior** of the NovaEco Core services (App, Auth, Gateway).

| ID | Title | Description | Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| **REQ-CORE-FUNC-001** | **Universal Identity** | The Auth service must provide Single Sign-On (SSO) for all ecosystem apps. | 1. User logs in at `auth.novaeco.tech`.<br/>2. User is redirected to `app.novaeco.tech` with a valid JWT.<br/>3. Token contains `user_id` and `roles`. |
| **REQ-CORE-FUNC-002** | **Gateway Routing** | The Gateway must strictly route requests to internal microservices based on path prefixes. | 1. Request to `/api/agro/*` goes to `novaagro`.<br/>2. Request to `/api/trade/*` goes to `novatrade`.<br/>3. Invalid paths return HTTP 404. |
| **REQ-CORE-FUNC-003** | **Launchpad Discovery** | The Mission Control App must dynamically list active sectors. | 1. Dashboard renders a grid of cards.<br/>2. Clicking "NovaAgro" opens `agriculture.novaeco.tech`. |
| **REQ-CORE-FUNC-004** | **Health Aggregation** | The System Status indicator must reflect the collective health of core services. | 1. If Auth is down, Status is "Degraded" (Red).<br/>2. If all services respond 200 OK, Status is "Online" (Green). |

---

## Related Pages
- [Non-Functional Requirements](./non-functional.md)
- [Sustainability Requirements](./sustainability.md)
- [Architecture Overview](../architecture/overview.md)
- [Use Cases: Level 1 Onboarding](../usecases/level-1-onboarding.md)

[⬅️ Back to Intro](../intro.md)

[⬅️ Previous: Architecture Overview](../architecture/overview.md)
[Next: Use Cases (Level 1 Onboarding) ➡️](../usecases/level-1-onboarding.md)