# Architecture de référence IAM (entreprise + cloud-native)

## Objectif
Fournir un modèle cible **réutilisable** qui sépare clairement :
- **AuthN** (qui es-tu ?)
- **AuthZ** (as-tu le droit ?)
- **Lifecycle** (quand créer/supprimer/adapter ?)
- **Session & Risk** (est-ce encore sûr maintenant ?)
- **Privileged** (administration contrôlée)

## Composants (vue logique)
1. **Identity Sources** : HR, référentiels internes, annuaires
2. **IdP** : SSO, MFA/passwordless, federation (OIDC/SAML)
3. **Directory / Identity graph** : attributs, groupes, relations
4. **Provisioning** : SCIM vers apps/SaaS + audits
5. **Access Layer** : gateway, WAF, API gateway, service mesh
6. **Authorization** : PDP (policy decision), PEP (enforcement)
7. **PAM** : bastion, vault, rotation, JIT, sessions enregistrées
8. **ITDR / SIEM / SOAR** : signaux, détection, réponse, coupure sessions
9. **K8s/OpenShift** : workload identity, secrets mgmt, RBAC, admission policies

## Schémas
- Vue d’ensemble : `diagrams/iam-reference-architecture.mmd`
- Flots (login, API, provisioning) : `diagrams/flows-*.mmd`

## Principes d’implémentation
- OIDC-first, SAML en compat.
- Tokens courts + rotation, scopes minimalistes.
- Externaliser l’autorisation (policy-as-code) quand utile.
- PAM + JIT sur chemins sensibles.
- Continuous access via signaux (événements) + actions de réponse.

