# Cas d’usage — Workforce SSO

## Contexte
Portail interne + plusieurs applications (legacy + cloud).

## Pattern recommandé
- IdP central (OIDC/SAML)
- MFA forte (phishing-resistant sur admins)
- Groupes et attributs gouvernés (HR + référentiel)
- SCIM vers apps (SaaS) + audits

## Points d’attention
- cohabitation SAML (legacy) / OIDC (nouveau)
- mapping rôles/groupes cohérent
- gestion sessions (timeout, re-auth sur risque)

