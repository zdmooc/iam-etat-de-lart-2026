# Checklist — Évaluation d’une plateforme IAM/SSO

## Standards
- [ ] OIDC + SAML2 (interop)
- [ ] PKCE, bonnes pratiques OAuth, gestion revocation/session
- [ ] SCIM (Users + Groups)

## Authentification
- [ ] MFA forte + facteurs résistants au phishing (passkeys/FIDO)
- [ ] Device posture / signaux de risque (si besoin)
- [ ] Policies adaptatives (risk-based)

## Sessions & tokens
- [ ] Tokens courts + rotation
- [ ] Gestion refresh tokens (rotation, binding)
- [ ] Revocation et propagation des coupures

## Lifecycle
- [ ] Processus Joiner/Mover/Leaver
- [ ] Journaux & export audit
- [ ] Recertification des accès

## Autorisation
- [ ] RBAC + possibilité ABAC/ReBAC
- [ ] Intégration policy-as-code (PDP/PEP) si nécessaire

## Sécurité & exploitation
- [ ] HA/PRA, sauvegardes, DR
- [ ] Observabilité (logs, métriques)
- [ ] Intégrations SIEM/SOAR
- [ ] Segmentation environnements (prod/non-prod)

