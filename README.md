# IAM — État de l’art (2026)

Ce dépôt propose un **référentiel IAM** prêt à réutiliser (patterns, checklists, schémas, templates) pour des contextes **entreprise** et **cloud-native** (Kubernetes/OpenShift).

## Contenu
- `docs/` : synthèses, standards, architecture de référence, patterns, checklists, cas d’usage
- `diagrams/` : schémas (Mermaid)
- `templates/` : exemples (Kubernetes, OPA, SCIM, OAuth/OIDC)
- `references.md` : sources et lectures

## Comment l’utiliser
1. Lire `docs/00-executive-summary.md`
2. Parcourir `docs/03-reference-architecture.md` + `diagrams/`
3. Sélectionner les patterns dans `docs/04-patterns/`
4. Appliquer les checklists (`docs/05-checklists/`)
5. Adapter les templates (`templates/`)

## Périmètre
- Authentification (SSO, MFA, passwordless)
- Fédération (OIDC/SAML)
- Autorisation (RBAC/ABAC/ReBAC, policy-as-code)
- Provisioning (SCIM) & lifecycle
- PAM (privilèges)
- ITDR & “continuous access” (signaux)

## Licence
MIT — voir `LICENSE`.

_Date de génération : 2026-02-26_
