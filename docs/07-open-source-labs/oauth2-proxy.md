# Lab — OAuth2-Proxy (devant une app)

## Objectif
Ajouter un SSO OIDC devant une application legacy (sans OIDC natif).

## Principe
- oauth2-proxy gère OIDC avec l’IdP
- il injecte des headers (user/groups) vers l’app
- l’app délègue l’authN au proxy

Voir : `templates/kubernetes/oauth2-proxy.example.yaml`.

