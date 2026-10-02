# IAM — État de l’art (2026)

Ce dépôt propose un **référentiel IAM d’architecture** prêt à réutiliser pour des contextes **entreprise** et **cloud-native** (Kubernetes/OpenShift).

Il porte les patterns vendor-neutral. La profondeur produit Keycloak et ses preuves runtime sont maintenues séparément dans `zdmooc/keycloak-enterprise-roadmap-v7`.

## Livrables d'architecture

- [HLD IAM](architecture/HLD.md)
- [LLD IAM](architecture/LLD.md)
- [ADR — frontières AuthN/AuthZ](architecture/ADR-001-authn-authz-boundaries.md)
- [UML Component](diagrams/iam-component.puml)
- [UML OIDC Sequence](diagrams/oidc-login-sequence.puml)
- [Claim / Evidence Matrix](evidence/CLAIM-EVIDENCE-MATRIX.md)
- [IAM Platform Comparison Template](docs/05-checklists/platform-comparison-template.md)

## Contenu

- `docs/` : synthèses, standards, architecture de référence, patterns, checklists, cas d’usage ;
- `architecture/` : HLD, LLD et décisions structurantes ;
- `diagrams/` : Mermaid + PlantUML ;
- `templates/` : exemples Kubernetes, OPA/Rego v1, SCIM et OAuth/OIDC ;
- `evidence/` : séparation entre conception et preuve ;
- `.github/workflows/` : validation statique et tests Rego ;
- `references.md` : sources officielles.

## Comment l’utiliser

1. Lire `docs/00-executive-summary.md`.
2. Lire `architecture/HLD.md` puis `architecture/LLD.md`.
3. Parcourir `docs/03-reference-architecture.md` et les diagrammes.
4. Sélectionner les patterns dans `docs/04-patterns/`.
5. Appliquer les checklists de `docs/05-checklists/`.
6. Adapter les templates.
7. Vérifier le niveau de preuve dans `evidence/CLAIM-EVIDENCE-MATRIX.md`.

## Périmètre

- authentification : SSO, MFA, passwordless/passkeys ;
- fédération : OIDC/SAML ;
- autorisation : RBAC/ABAC/ReBAC, PDP/PEP, policy-as-code ;
- provisioning : SCIM, Joiner/Mover/Leaver ;
- PAM : JIT/JEA, vault, break-glass ;
- ITDR / continuous access : SSF/CAEP/RISC ;
- CIAM / B2B ;
- non-human identities et workload identity ;
- Kubernetes/OpenShift ;
- audit, SIEM/SOAR et Zero Trust centré identité.

## Niveau de preuve

Ce dépôt démontre une **capacité de conception IAM**. Il ne revendique pas un déploiement IAM d'entreprise en production. Les preuves d’exécution Keycloak restent dans le dépôt spécialiste.

## Licence

MIT — voir `LICENSE`.

_Mise à jour architecture : 2026-10-02._
