# Sustainability Requirements

These requirements ensure the platform itself minimizes its ecological footprint through efficient design and protocol choices.

| ID | Title | Description | Metric |
| :--- | :--- | :--- | :--- |
| **REQ-CORE-SUS-001** | **Dark Mode Default** | To reduce energy consumption on OLED screens, the default UI theme for all Core apps (Docs, Admin) must be Dark. | Default CSS variable `--bg` is `#0f2027` (or similar dark hex). |
| **REQ-CORE-SUS-002** | **Protocol Efficiency** | High-volume machine-to-machine traffic must use **Binary Serialization** (gRPC/ProtoBuf) to reduce CPU cycles and bandwidth usage compared to text-based JSON. | Internal service validation uses gRPC by default. |
| **REQ-CORE-SUS-003** | **Payload Compression** | Public REST APIs must support compression to minimize data transfer energy for mobile/web clients. | API responses must have `Content-Encoding: gzip` enabled. |

---

## Related Pages
- [Non-Functional Requirements](./non-functional.md)
- [Sustainability Requirements](./sustainability.md)
- [Architecture Overview](../architecture/overview.md)
- [Use Cases: Level 1 Onboarding](../usecases/level-1-onboarding.md)