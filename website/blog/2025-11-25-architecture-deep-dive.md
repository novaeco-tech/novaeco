---
slug: architecture-deep-dive
title: NovaEco Architecture — System of Systems
authors:
  - name: Claudiu Câmpeanu
    title: Founder, Circular Engineering Nova GmbH
    url: https://circular.engineering
    image_url: https://circular.engineering/wp-content/uploads/2025/09/team_member_claudiu-150x150.jpg
tags: [architecture, novaeco, enablers, sectors]
---

# NovaEco Architecture — System of Systems 🏗️

NovaEco is designed as a **system‑of‑systems**: interconnected **Horizontal Enablers**, **Vertical Sectors**, **Workers**, and **Products** that together enable sustainable collaboration, compliance, and innovation.

---

## Core Services (Kernel)

The foundational plumbing managed in the central `novaeco` repository:

- **Gateway** → [api.novaeco.tech](https://api.novaeco.tech) (Multiplexed REST/gRPC)
- **Identity** → [id.novaeco.tech](https://id.novaeco.tech) (Keycloak SSO)
- **Auth** → [auth.novaeco.tech](https://auth.novaeco.tech) (Internal Verifier)
- **Docs** → [novaeco.tech](https://novaeco.tech) (Knowledge Base)

---

## Horizontal Enablers

Cross‑cutting foundational services consumed by all sectors:

- **NovaAdmin** (Mission Control & Dashboard)
- **NovaBalance** (Environmental auditing)
- **NovaEquity** (Social auditing)
- **NovaFin** (Ledger, payments, staking)
- **NovaInfra** (IoT registry, fleet command)
- **NovaLogistics** (Optimization, circular transport)
- **NovaMaterial** (Digital product passports)
- **NovaMind** (Shared AI models)
- **NovaPolicy** (Policy-as-code, compliance)
- **NovaSkills** (Labor verification)
- **NovaTrade** (Marketplace, matching)

---

## Vertical Sectors

Industry‑specific applications:

- **NovaAgro** (Regenerative agriculture)
- **NovaAir** (Air quality, carbon capture)
- **NovaBuild** (Construction, material banks)
- **NovaChem** (Chemical leasing)
- **NovaEnergy** (Renewable grid, V2G)
- **NovaMake** (Distributed manufacturing)
- **NovaNature** (Biodiversity, reforestation)
- **NovaPack** (Reusable packaging)
- **NovaRecycle** (Recycling, urban mining)
- **NovaRetail** (Product-as-a-service)
- **NovaTronix** (E-waste, repair)
- **NovaTextile** (Circular fashion)
- **NovaWater** (Industrial water cycles)

---

## Workers

Independent background services for high-throughput tasks, such as:

- **Quality** (NovaAir sensor ingest)
- **Bioacoustics** (Species identification)
- **LCACalc** (Real-time impact calculation)
- **SlicerCheck** (3D printability verification)
- **TradeSettlement** (Ledger batching)

---

## Products

Flagship applications that consume multiple enablers/sectors:

- **DurasAGV** (Autonomous agricultural robot)
- **NovaLab** (Innovation engine for circular projects)
- **RetailLoop** (E-commerce plugin for resale)
- **UrbanMiner** (City council waste dashboard)

---

## Principles

- **Open Source** — community‑driven repos  
- **Transparency** — ADRs, use cases, glossary  
- **Scalability** — federated monorepo + containers  
- **Auditability** — Balance & Equity enablers  
- **Circularity** — every sector reinforces sustainable loops

---

For diagrams and flows, see the [Architecture Overview](/docs/architecture/overview).