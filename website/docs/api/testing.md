# API Testing Guide

This guide details how to verify the **NovaEco Gateway** and **Identity Services** across different testing levels.

---

## 1. Unit Tests (Level 5)

**Scope:** Isolated logic within a single container (e.g., "Does this function correctly parse a JWT header?").

- **Python Services (Gateway/Auth):**
  Uses `pytest` with mocked external dependencies.

```bash
# Inside the API or Auth container
pytest tests/unit
```

- **Node.js Services (Docs):**
  Uses `jest`.

```bash
# Inside the Website container
npm test
```

---

## 2. Integration Tests (Level 4)

**Scope:** Wiring between the Gateway, Auth Service, and the Keycloak Identity Provider.

**Goal:** Verify that the Gateway correctly routes traffic and that the Auth service correctly validates tokens against Keycloak's keys.

**Running Integration Tests:**
These tests run against the **real** Docker containers defined in `.devcontainer/docker-compose.yml`.

```bash
# 1. Ensure the stack is running
docker compose up -d

# 2. Run the suite (from the API container)
pytest tests/integration
```

**Key Scenarios Covered:**

- **OIDC Flow:** Can a test user get a token from Keycloak?
- **Token Validation:** Does the Auth service accept a valid RS256 token?
- **Gateway Routing:** Does `api.novaeco.tech/health` return 200 OK?

---

## 3. Manual Testing (Ad-Hoc)

### Testing REST Endpoints (curl)

You can manually verify the REST interface using `curl` or Postman.

**Health Check:**

```bash
curl -i https://api.novaeco.tech/health
```

**Authenticated Request:**

```bash
# 1. Get Token from Keycloak (Password Grant for testing)
TOKEN=$(curl -s -d "client_id=novaeco-core" -d "username=testuser" -d "password=password" -d "grant_type=password" https://id.novaeco.tech/realms/novaeco/protocol/openid-connect/token | jq -r .access_token)

# 2. Call Protected Endpoint
curl -H "Authorization: Bearer $TOKEN" https://api.novaeco.tech/projects
```

### Testing gRPC Endpoints (grpcurl)

To test the binary gRPC interface exposed on Port 443, use `grpcurl`.

**List Services:**

```bash
grpcurl api.novaeco.tech:443 list
```

**Validate Token (Directly via Auth Service):**

```bash
grpcurl -d '{"token": "'$TOKEN'"}' api.novaeco.tech:443 novaeco.auth.v1.AuthService/ValidateToken
```

---

## 4. CI/CD Pipeline

- **Continuous Integration (`ci.yml`):** Runs Unit and Integration tests on every Pull Request.
- **Contract Testing:** We use **Pact** to ensure that the API Gateway and the Frontend (NovaAdmin) remain compatible without requiring a full end-to-end environment.

## Best Practices

- **Never use production tokens** for local testing. Use the `testuser` account seeded in Keycloak.
- **Use the SDK:** For Python scripts, prefer `novaeco-auth-client` over raw gRPC calls.
