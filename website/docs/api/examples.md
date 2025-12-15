# API Examples

These examples demonstrate how to interact with the NovaEco ecosystem using standard tools (`curl`) and our official SDKs.

---

## 1. Authentication (Keycloak)

To interact with any API, you first need a valid Access Token (JWT).

**For Testing (Password Grant):**
Use this to quickly get a token for development. In production apps, use the Browser Flow (Authorization Code).

```bash
curl -X POST https://id.novaeco.tech/realms/novaeco/protocol/openid-connect/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=novaeco-core" \
  -d "grant_type=password" \
  -d "username=testuser" \
  -d "password=password"
````

**Response:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1...",
  "expires_in": 300,
  "token_type": "Bearer"
}
```

-----

## 2\. REST API (Gateway)

**Base URL:** `https://api.novaeco.tech`

### Fetch Projects

Retrieve a list of active circular economy projects.

```bash
curl -X GET https://api.novaeco.tech/projects \
  -H "Authorization: Bearer <your_access_token>"
```

### Submit Digital Product Passport (DPP)

Register a new material event.

```bash
curl -X POST https://api.novaeco.tech/dpp \
  -H "Authorization: Bearer <your_access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "batch-123",
    "material": "recycled-steel",
    "mass_kg": 500,
    "origin": "NovaRecycle-Plant-1"
  }'
```

-----

## 3\. Python SDK (gRPC)

For high-performance agents or internal workers, use the official Python client.

**Installation:**

```bash
pip install novaeco-auth-client
```

**Usage:**

```python
from novaeco_auth_client import AuthClient

# Connect to the public multiplexed endpoint (Port 443)
client = AuthClient(address="auth.novaeco.tech:443")

# Validate a token
try:
    result = client.validate_token("eyJhbGciOiJSUzI1...")
    
    if result.is_valid:
        print(f"✅ User {result.user_id} is authorized.")
    else:
        print("❌ Invalid token.")
        
except Exception as e:
    print(f"Connection failed: {e}")
```