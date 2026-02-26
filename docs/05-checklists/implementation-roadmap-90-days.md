# Roadmap 90 jours (implémentation pragmatique)

## Jours 0–15 — Baseline & quick wins
- Inventaire : apps, protocoles, flux, comptes à privilèges
- Standardiser : OIDC-first, flows recommandés, PKCE
- Définir politiques MFA (priorité comptes à privilèges)
- Mettre en place journaux d’audit (IdP → SIEM)

## Jours 15–45 — Lifecycle & privilèges
- Industrialiser JML (Joiner/Mover/Leaver)
- Mettre SCIM sur les SaaS principaux
- Démarrer PAM : coffres + rotation + bastion
- Introduire JIT sur premiers périmètres

## Jours 45–75 — Autorisation & APIs
- Harmoniser scopes/audiences
- Standardiser validation tokens côté gateway/services
- Démarrer policy-as-code (OPA) sur un cas pilote
- Réduire secrets statiques (rotation, vault)

## Jours 75–90 — Continuous access & durcissement
- Définir signaux de risque + playbooks de réponse
- Piloter coupure sessions / re-auth
- Recertification pilote (campagne)
- KPIs : taux MFA, tokens courts, comptes orphelins, admins permanents

