# Pattern — ITDR & Continuous Access (SSF/CAEP/RISC)

## Constat
Le risque change *pendant* une session : device compromis, compte suspect, fuite, etc.

## Objectif
Partager des signaux et déclencher des actions :
- réauthentification
- élévation MFA
- coupure session / révocation tokens

## Mise en œuvre (vue simple)
- Producteurs : IdP, EDR, SIEM, SaaS
- Bus d’événements / API signaux
- Consommateurs : IdP (session), apps/gateways (enforcement), SOAR (automations)

## Artifacts
- Schéma : `diagrams/iam-continuous-access.mmd`

