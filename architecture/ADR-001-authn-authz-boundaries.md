# ADR-001 — Separate authentication, coarse API policy and business authorization

## Status
Accepted as reference-architecture principle.

## Context

Enterprise IAM designs often become ambiguous when the IdP, API gateway and application all appear to "authorize" the same request.

## Decision

- IdP authenticates subjects/clients and issues identity/security tokens.
- API gateway may validate tokens and apply coarse-grained access policies such as audience/scope/rate limits.
- Application/domain service remains responsible for object-, function- and business-level authorization.
- A PDP may externalize fine-grained policy decisions where consistency, auditability or cross-application reuse justifies it.

## Consequences

- explicit trust boundaries;
- reduced risk of pushing business rules into the gateway;
- better alignment with OWASP API authorization concerns;
- authorization context and failure behavior must be documented.

## Validation

Validate the split in each solution architecture and integration test; this ADR does not prove any specific product implementation.
