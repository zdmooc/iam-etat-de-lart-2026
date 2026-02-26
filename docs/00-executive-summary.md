# Synthèse (à lire en 10 minutes)

## Ce que l’IAM est devenu
L’IAM moderne est un **plan de contrôle** transverse qui sécurise **identités**, **sessions**, **droits** et **risques** sur :
- identités humaines (workforce, partenaires, clients/CIAM)
- identités non-humaines (APIs, microservices, workloads, agents)

## Les priorités 2026
1. **Phishing-resistant** : passkeys / FIDO2-WebAuthn, MFA forte, réduction des mots de passe.
2. **OAuth/OIDC durci** : PKCE, profils prescriptifs (FAPI) pour APIs sensibles, bonnes pratiques de tokens.
3. **Provisioning industrialisé** : SCIM + “joiner/mover/leaver” fiable (réduction des comptes orphelins).
4. **Autorisation fine** : au-delà du RBAC (ABAC/ReBAC), policy-as-code, externalisation des décisions.
5. **Privilèges maîtrisés** : PAM, JIT/JEA, suppression des privilèges permanents.
6. **Continuous Access** : signaux partagés (SSF/CAEP/RISC), coupure / réévaluation des sessions.
7. **Workload Identity** : identité de service, tokens courts, mTLS, séparation stricte des secrets.

## Architecture cible (vision)
- **IdP** (SSO + MFA/passwordless) = source d’authentification
- **Provisioning** (SCIM) vers applications/SaaS
- **Policy decision** (PDP) + enforcement (PEP) côté gateway/service
- **PAM** pour comptes à privilèges
- **ITDR + SIEM/SOAR** pour détection/réponse
- **Kubernetes/OpenShift** : workloads identity + RBAC + admission policies

Voir : `docs/03-reference-architecture.md` + `diagrams/`.

## Livrables actionnables
- Patterns : `docs/04-patterns/`
- Checklists : `docs/05-checklists/`
- Templates : `templates/`

