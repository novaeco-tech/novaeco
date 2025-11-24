# ADR-002: Identity & Authentication

## Context
Single Sign-On (SSO) and OAuth2 are required for unified contributor and user identity.

## Decision
Implement a dedicated Auth service (`/auth`) using Python/Flask with OAuth2 flows.

## Consequences
- Centralized identity management.
- Simplified contributor onboarding.
- Compliance with GDPR and security standards.
