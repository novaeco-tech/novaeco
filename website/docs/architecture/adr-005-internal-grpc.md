# ADR-005: gRPC/ProtoBuf for Internal Communication

Date: 2025-11-26
Status: Accepted

## Context
The NovaEco is a distributed system of systems. Relying solely on JSON for internal service-to-service communication risks loose typing, parsing errors, and higher latency as the ecosystem grows.

## Decision
We will use **gRPC with Protocol Buffers (ProtoBuf)** for synchronous internal communication between Pillars (Enablers and Sectors).
External clients will still interface via a REST/JSON API Gateway (see ADR-003).

## Consequences
### Positive
- **Strict Contracts:** ProtoBuf enforces schema compatibility between services.
- **Performance:** Binary serialization is faster and lighter than JSON.
- **Code Generation:** Client libraries can be auto-generated for Python, Node, and Go.

### Negative
- **Debuggability:** Binary data is harder to inspect (curl) than JSON.
- **Tooling:** Requires `grpcurl` or specific tools for ad-hoc testing.