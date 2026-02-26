# Cas d’usage — Service-to-Service (microservices)

## Objectif
Identité de service, traçabilité, tokens courts.

## Pattern recommandé
- ServiceAccount par service
- tokens courts + rotation
- mTLS (service mesh) si besoin
- policy-as-code pour autorisation fine

## Anti-patterns
- partage de clés API
- tokens longs stockés en secret
- “god service account”

