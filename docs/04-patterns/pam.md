# Pattern — PAM (Privileged Access Management)

## Objectifs
- Supprimer le privilège permanent (“standing privilege”)
- Tracer, limiter, et contrôler l’élévation
- Réduire le blast radius

## Composants typiques
- Vault / coffre (secrets, rotation)
- Bastion / session manager (enregistrement)
- JIT/JEA (accès à durée limitée)
- Break-glass (procédure d’urgence auditée)

## Recommandations
- Admins “normaux” sans droits permanents
- Élévation JIT avec approbation (workflow)
- Rotation automatique des secrets
- Segmentation forte (prod vs non-prod)

## Artifacts
- `docs/05-checklists/zero-trust-controls.md`

