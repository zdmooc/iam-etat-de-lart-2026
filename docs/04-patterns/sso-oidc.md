# Pattern — SSO OIDC + MFA/passwordless

## Quand l’utiliser
- Nouvelles applications web, mobile, SPA
- Besoin de fédérer plusieurs domaines (B2B)

## Décisions clés
- Flow : Authorization Code (+ PKCE pour SPA/mobile)
- MFA : facteur résistant au phishing (passkey/FIDO) sur parcours sensibles
- Sessions : durée, rotation, refresh token, revocation

## Bonnes pratiques
- PKCE partout quand applicable
- Limiter les scopes/claims, éviter “trop d’attributs”
- Séparer authN (IdP) et authZ (policies applicatives)

## Anti-patterns
- Implicit flow (legacy)
- Tokens longs non rotés
- Claims “gros” avec données sensibles inutiles

## Artifacts
- `templates/oauth/oidc-client.example.json`
- `diagrams/flows-login-oidc.mmd`

