# Quickstart

This guide helps new contributors get started with the NovaEco Core Kernel quickly.

---

## Prerequisites
- Docker Desktop
- VS Code with Remote Containers extension
- Git installed

---

## Steps
1. Clone the repository:
```bash
   git clone https://github.com/novaeco-tech/novaeco.git
```

2.  Open the folder in VS Code.
3.  Click **"Reopen in Container"** when the popup appears (or use `F1` \> `Dev Containers: Reopen in Container`).
4.  Wait for the build to complete. Once running, the following services are available:
      - **Gateway API:** http://localhost:8000/health
      - **Identity (Keycloak):** http://localhost:8080 (User: `admin` / Pass: `admin`)
      - **Auth Verifier:** http://localhost:9000/health
      - **Documentation:** http://localhost:3000

---

## First API Call

Verify the system is healthy by querying the Gateway:

```bash
curl -i https://api.novaeco.tech/health
# Or locally:
curl -i http://localhost:8000/health
```

---

## Next Steps
- Explore [Architecture Overview](../architecture/overview.md).
- Review [Functional Requirements](../requirements/functional.md).
- Try [API Examples](../api/examples.md).
