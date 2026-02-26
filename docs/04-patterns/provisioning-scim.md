# Pattern — Provisioning & Identity Lifecycle (SCIM)

## Problème
Sans provisioning robuste : comptes orphelins, groupes incohérents, audits difficiles.

## Solution
- Source d’autorité : HR / référentiel interne
- Mécanisme : SCIM (Users + Groups)
- Processus : Joiner/Mover/Leaver (JML) + exceptions

## Règles essentielles
- Désactivation immédiate à la sortie (leaver)
- Revue périodique des accès (recertification)
- Journalisation des événements SCIM (création/MAJ/suppression)

## Artifacts
- `templates/scim/user.example.json`
- `templates/scim/group.example.json`
- Checklist : `docs/05-checklists/platform-evaluation.md`

