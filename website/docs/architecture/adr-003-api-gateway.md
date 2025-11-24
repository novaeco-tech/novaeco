# ADR-003: API Gateway

## Context
The ecosystem requires a single "front door" for all data and service requests.

## Decision
Use a Python/Flask API Gateway (`/api`) to route requests to services.

## Consequences
- Simplified client integration.
- Centralized logging and monitoring.
- Easier enforcement of rate limits and policies.
