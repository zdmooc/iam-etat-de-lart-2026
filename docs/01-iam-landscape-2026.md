# Panorama IAM (2026)

## 1. IAM, CIAM, PAM, ITDR : clarification
- **IAM (workforce)** : identités internes (collaborateurs, prestataires), SSO, MFA, lifecycle.
- **CIAM** : identités clients, forte volumétrie, consentement, parcours d’inscription, fraude.
- **PAM** : comptes et actions à privilèges (admin, prod, break-glass).
- **ITDR** : détection et réponse aux menaces identitaires (corrélation signaux + actions).

## 2. Zero Trust comme “système d’exploitation”
Principes :
- vérifier explicitement (auth + device + contexte)
- moindre privilège (JIT/JEA, segmentation)
- supposer la compromission (monitoring + réponses)

## 3. Déplacement du centre de gravité
- Du **périmètre réseau** vers l’**identité**.
- Du “login” vers la **session** (réévaluation continue).
- Des rôles statiques vers des **policies** (contextuelles, fines).

## 4. Non-human identities (NHI)
Ce sont souvent les identités les plus nombreuses :
- services, workloads, pipelines CI/CD, bots, agents
- clés API, certificats, tokens, comptes de service
Enjeu : rotation, expiration courte, preuve cryptographique, traçabilité.

## 5. Motifs d’échec fréquents
- MFA non résistante au phishing (push fatigue, OTP interceptable)
- provisioning incomplet (comptes orphelins)
- autorisation dispersée dans le code (incohérences)
- secrets longs/vivants (API keys) non rotés
- admins permanents, pas de JIT
- absence de signaux/réponse sur sessions

