# API Examples

## Example: User Login
```bash
curl -X POST https://auth.nova-ecosystem.org/login \
  -d '{"username":"claudiu","password":"secret"}'
```

## Example: Fetch Sustainability Dashboard
```bash
curl -H "Authorization: Bearer <token>" \
  https://api.nova-ecosystem.org/dashboard
```

## Example: Submit DPP
```bash
curl -X POST https://api.nova-ecosystem.org/dpp \
  -H "Authorization: Bearer <token>" \
  -d '{"productId":"123","material":"steel"}'
```