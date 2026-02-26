# Validation de token (check minimal)

## JWT validation
- Vérifier signature (JWKS)
- Vérifier `iss` (issuer)
- Vérifier `aud` (audience) / `azp` si nécessaire
- Vérifier `exp` + tolérance d’horloge
- Vérifier `scope` / claims minimales
- Refuser algorithmes faibles / non attendus
- Journaliser `jti` / `sub` selon besoin d’audit

## Notes
- Préférer claims minimales et éviter PII.
- Distinguer authN (id_token) et authZ (access_token).
