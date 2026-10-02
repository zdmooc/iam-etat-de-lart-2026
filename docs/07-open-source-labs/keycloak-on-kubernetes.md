# Lab — Keycloak sur Kubernetes/OpenShift

## Rôle de ce document

Ce fichier décrit uniquement le **point de raccordement** entre l'architecture IAM vendor-neutral et une implémentation Keycloak.

Le dépôt spécialiste canonique est :

`zdmooc/keycloak-enterprise-roadmap-v7`

Il contient les versions, Operator/CR, security hardening, scénarios, runbooks et preuves runtime. Ne pas dupliquer ici une procédure Keycloak détaillée susceptible de diverger.

## Objectif

Valider sur un environnement de test :
- discovery OIDC ;
- Authorization Code + PKCE ;
- client/service identity ;
- groupes/rôles/scopes ;
- protection d'une application ou API ;
- observabilité et comportement au redémarrage selon le périmètre du test.

## Pré-requis

- Kubernetes ou OpenShift ;
- ingress/route et DNS adaptés au lab ;
- base supportée par le scénario ;
- livraison de secrets au runtime ;
- TLS pour toute validation proche production.

## Parcours recommandé

1. sélectionner le scénario dans le dépôt Keycloak spécialiste ;
2. noter version Keycloak/RHBK, Operator et cluster ;
3. créer realm/client/scopes sans secret versionné ;
4. exécuter discovery et flow OIDC ;
5. tester un cas nominal et au moins un échec 401/403 ;
6. conserver une preuve sanitizée ;
7. documenter ce qui est prouvé et ce qui reste référence.

## Frontière de preuve

Un guide ou manifest dans ce dépôt IAM reste `REFERENCE_DESIGN`. Une preuve Keycloak doit pointer vers l'exécution observée dans le dépôt spécialiste ; elle ne transforme pas automatiquement toute l'architecture IAM en runtime prouvé.
