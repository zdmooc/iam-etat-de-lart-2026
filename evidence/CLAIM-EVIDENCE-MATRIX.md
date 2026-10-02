# Claim / Evidence Matrix

| Capability | Evidence level | Source |
|---|---|---|
| IAM/CIAM/PAM/ITDR landscape | REFERENCE_DESIGN | `docs/01-iam-landscape-2026.md` |
| OIDC/SAML/OAuth/SCIM standards model | REFERENCE_DESIGN | `docs/02-standards-protocols.md` |
| Enterprise IAM HLD | REFERENCE_DESIGN | `architecture/HLD.md` |
| IAM integration LLD | IMPLEMENTATION_CONTRACT | `architecture/LLD.md` |
| AuthN/AuthZ boundary ADR | REFERENCE_DECISION | `architecture/ADR-001-authn-authz-boundaries.md` |
| UML component / OIDC sequence | STATIC_ASSET | `diagrams/*.puml` |
| OPA policy examples | STATIC_VALIDATED when CI passes | `templates/policy/opa/` |
| SCIM examples | STATIC_ASSET | `templates/scim/` |
| Kubernetes identity/RBAC examples | STATIC_ASSET | `templates/kubernetes/` |
| Keycloak runtime | EXTERNAL_SPECIALIST_EVIDENCE | `zdmooc/keycloak-enterprise-roadmap-v7` |
| Enterprise IAM runtime | NOT_PROVEN | — |
| Production readiness | NOT_CLAIMED | — |

## Rule

This repository is a vendor-neutral reference architecture. It must not inherit runtime claims from a product-specific repository. Links to Keycloak evidence show implementation depth in the portfolio, not proof that this entire IAM reference architecture has been deployed.
