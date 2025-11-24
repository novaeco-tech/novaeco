# API Testing

## Unit Tests
- Each service has its own test suite (`pytest` for Python, `npm test` for Node.js).

## Integration Tests
- Run with `pytest tests/integration`.
- Validate cross-service flows (Auth + Gateway).

## CI/CD
- GitHub Actions run tests automatically on pull requests.
- Containers ensure consistent environments.

## Best Practices
- Always test with mock data before production.
- Use Postman or curl for manual validation.
