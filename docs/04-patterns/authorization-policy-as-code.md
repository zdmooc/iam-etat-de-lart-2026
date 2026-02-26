# Pattern — Autorisation fine & Policy-as-Code

## Quand dépasser le RBAC ?
- règles dépendantes d’attributs (entité, région, classification)
- relations (manager → employés, équipe → ressources) : ReBAC
- besoins d’audit & cohérence multi-apps

## Modèles
- RBAC : rôles
- ABAC : attributs
- ReBAC : graph/relations

## Externalisation (PDP/PEP)
- PDP : moteur de décision (ex. OPA)
- PEP : point d’application (gateway, sidecar, app)

## Artifact (OPA)
- Exemple Rego : `templates/policy/opa/allow-example.rego`
- Tests : `templates/policy/opa/README.md`

