# ADR-005: gRPC/ProtoBuf Standard

Date: 2025-11-26
Status: Accepted

## Context
The NovaEco is a distributed system of systems involving diverse actors: internal microservices, external high-frequency trading agents, and IoT telemetry aggregators.

Relying solely on JSON for machine-to-machine communication introduces significant risks:
1.  **Loose Typing:** JSON lacks schema enforcement, leading to runtime errors when services drift.
2.  **Performance Overhead:** Text-based serialization adds latency, which is unacceptable for high-throughput loops (e.g., Grid Balancing or Trading).
3.  **Inefficient Development:** Developers must manually write client wrappers for every REST endpoint.

## Decision
We adopt **gRPC with Protocol Buffers (ProtoBuf)** as the standard protocol for **synchronous machine-to-machine communication**, regardless of whether the consumer is internal or external.

1.  **Internal Mesh:** Services (e.g., `NovaAgro` $\leftrightarrow$ `NovaFin`) communicate directly via gRPC.
2.  **Public Access:** External agents access these same gRPC interfaces via the **Multiplexed Gateway** (`api.novaeco.tech`) on Port 443 (see ADR-003).
3.  **Schema-First:** The `.proto` files are the source of truth. We publish generated SDKs (e.g., `novaeco-auth-client`) to ensure external developers have a strongly-typed, pre-validated interface.

## Consequences
### Positive
- **Strict Contracts:** ProtoBuf enforces schema compatibility, preventing integration bugs before deployment.
- **Unified Surface:** External agents get the same high-performance interface as internal services.
- **Code Generation:** We automatically generate and publish client SDKs for Python, Node, and Go, reducing integration effort for partners.

### Negative
- **Versioning Rigor:** Since our `.proto` definitions are now public APIs, we must adhere to strict semantic versioning (e.g., never renaming fields, only deprecating) to avoid breaking external clients.
- **Tooling:** Debugging requires specialized tools (like `grpcurl`) rather than standard browsers or `curl`.