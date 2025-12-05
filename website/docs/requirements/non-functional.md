# Non-Functional Requirements

These requirements define the **quality attributes** (Performance, Security, UX).

| ID | Title | Category | Constraint |
| :--- | :--- | :--- | :--- |
| **REQ-CORE-SEC-001** | **Token Signature** | Security | The Gateway must reject any JWT that is not signed by the internal private key (RS256). |
| **REQ-CORE-PERF-001** | **Gateway Latency** | Performance | The overhead added by the Gateway proxy must be less than **20ms** per request. |
| **REQ-CORE-UI-001** | **Mobile Responsiveness** | Usability | The Mission Control dashboard must render without horizontal scrolling on a 375px wide viewport. |
| **REQ-CORE-OPS-001** | **Container Health** | Operations | All core containers must provide a `/health` endpoint that returns JSON `{"status": "ok"}`. |