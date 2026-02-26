# Pattern — Sécurisation d’APIs (OAuth/OIDC)

## Objectifs
- Authentifier des clients (apps, services)
- Autoriser finement (scopes, policies)
- Minimiser l’impact en cas de fuite (tokens courts)

## Points clés
- Utiliser Authorization Code + PKCE (apps)
- Pour service-to-service : client credentials + durcissement (mTLS, rotation, audience)
- Tokens courts, refresh tokens limités, rotation
- Validation : signature JWT + audiences + issuers + clock skew

## Renforcement (haute sécurité)
- Profils prescriptifs type FAPI
- mTLS ou DPoP selon contexte
- Binding de token à un contexte de preuve

## Artifacts
- `templates/oauth/token-validation.md`
- `diagrams/flows-api-oauth.mmd`

