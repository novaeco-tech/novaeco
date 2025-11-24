# Auth API

The Auth service (`/auth`) provides identity and access management.

## Endpoints
- `POST /signup` — Register a new user.
- `POST /login` — Authenticate and receive a token.
- `GET /profile` — Retrieve user profile.
- `POST /refresh` — Refresh access tokens.

## Notes
- Uses OAuth2 flows.
- Tokens must be included in the `Authorization` header.
