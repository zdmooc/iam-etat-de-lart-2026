# Lab — OPA (Open Policy Agent) pour l’autorisation

## Objectif
Externaliser les règles d’accès en policy-as-code.

## Principe
- l’application ou la gateway appelle OPA (PDP)
- OPA renvoie allow/deny + éventuellement des obligations

Voir : `templates/policy/opa/`.

