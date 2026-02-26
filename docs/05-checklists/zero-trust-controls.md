# Checklist — Contrôles Zero Trust centrés identité

- [ ] Auth forte, phishing-resistant sur comptes sensibles
- [ ] Moindre privilège (RBAC strict, séparation des rôles)
- [ ] JIT/JEA pour admin (PAM)
- [ ] Segmentation (réseau + identity-aware access)
- [ ] Logs d’audit unifiés (IdP, gateway, apps, PAM)
- [ ] Détection (ITDR) + réponse (coupure sessions)
- [ ] Secrets rotés, pas de clés longues durées
- [ ] Workload identity (K8s) + mTLS (option)
- [ ] Revue régulière des accès (recertification)
- [ ] Tests : simulations d’attaque (phishing, token replay, etc.)

