# Testing Guide

## Unit Tests
- Python: `pytest`
- Node.js: `npm test`

## Integration Tests
- Run `pytest tests/integration`
- Validate cross‑service flows (Auth + Gateway).

## CI/CD
- GitHub Actions run tests automatically.
- Containers ensure consistent environments.

## Best Practices
- Test early and often.
- Use mock data for sensitive flows.
