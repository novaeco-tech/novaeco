# Auth & Identity API

The NovaEco Identity stack is split into two distinct services to optimize for both standard user flows and high-performance machine validation.

---

## 1. Public Identity Provider (`id.novaeco.tech`)

**Engine:** [Keycloak](https://www.keycloak.org/)  
**Role:** Source of Truth for Users, SSO, and Token Issuance.

This is the standard **OpenID Connect (OIDC)** provider. Web and Mobile applications should interact with this service to log users in.

### Configuration
- **Issuer:** `https://id.novaeco.tech/realms/novaeco`
- **Discovery Endpoint:** `https://id.novaeco.tech/realms/novaeco/.well-known/openid-configuration`

### Standard OIDC Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/protocol/openid-connect/auth` | **Login / Signup.** Redirect browser here to start the Authorization Code flow. |
| `POST` | `/protocol/openid-connect/token` | **Exchange.** Trade an Authorization Code for an Access Token (JWT). |
| `POST` | `/protocol/openid-connect/token` | **Refresh.** Get a new Access Token using a Refresh Token. |
| `GET` | `/protocol/openid-connect/userinfo` | **Profile.** Retrieve standard claims (email, name) for the current user. |
| `POST` | `/protocol/openid-connect/logout` | **Logout.** Terminate the server-side session. |

> ** Developer Note:** You should rarely call these endpoints manually. Use a standard OIDC library (e.g., `Authlib`, `NextAuth`, `OIDC-Client`) configured with the Discovery Endpoint.

---

## 2. Auth Verification Service (`auth.novaeco.tech`)

**Engine:** Python/gRPC  
**Role:** Token Validation Bridge & Trust Anchor.

This service acts as a high-speed verification layer. It caches Keycloak's public keys (JWKS) and provides a lightweight interface for internal microservices (and external agents) to validate tokens without the overhead of full HTTP calls.

### REST API (Health)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Returns `{"status": "ok", "mode": "verifier"}`. Used by load balancers. |

### gRPC API (Validation)
Exposed on **Port 443** (via Multiplexing) for high-performance clients.

**Service Definition:**
```protobuf
service AuthService {
  // fast, local validation using cached JWKS
  rpc ValidateToken (ValidateRequest) returns (ValidateResponse);
}

message ValidateRequest {
  string token = 1; // The JWT access token
}

message ValidateResponse {
  bool is_valid = 1;
  string user_id = 2; // Extracted from 'sub' claim
  string role = 3;    // Extracted from 'realm_access'
}
````

### SDK Usage

To validate tokens in your own Python service, use the official client:

```bash
pip install novaeco-auth-client
```

```python
from novaeco_auth_client import AuthClient

client = AuthClient("auth.novaeco.tech:443")
result = client.validate_token(user_jwt)

if result.is_valid:
    print(f"User {result.user_id} is authorized.")
```