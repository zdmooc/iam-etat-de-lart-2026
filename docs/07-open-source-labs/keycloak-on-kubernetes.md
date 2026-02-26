# Lab — Keycloak sur Kubernetes (guide)

## Objectif
Mettre en place un IdP de test pour :
- OIDC (Auth Code + PKCE)
- groupes/roles
- MFA (selon configuration)

## Pré-requis
- cluster K8s/OpenShift
- ingress (ou route)
- base de données (option selon chart)
- TLS (recommandé)

## Étapes (high level)
1. Déployer Keycloak via Helm (chart communautaire/éditeur)
2. Configurer un realm, un client, des redirect URIs
3. Créer utilisateurs/groupes/roles
4. Tester OIDC (ex : oauth2-proxy ou app demo)
5. Exporter realm (sans secrets) pour IaC

Templates indicatifs : `templates/kubernetes/` et `templates/oauth/`.

