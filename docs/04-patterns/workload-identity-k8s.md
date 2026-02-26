# Pattern — Workload Identity sur Kubernetes/OpenShift

## Problème
Les workloads utilisent trop souvent :
- secrets statiques
- clés longues durées
- comptes partagés

## Objectif
- Identité forte par workload
- Tokens courts
- Rotation automatisée
- Traçabilité (qui/quoi a appelé quoi)

## Approche (agnostique)
- ServiceAccount par application (least privilege)
- Tokens projetés / courts (si possible)
- mTLS via service mesh (option)
- Secret managers (External Secrets / CSI driver) pour secrets rotés
- Admission policies (ex : bloquer images non approuvées, exiger probes, etc.)

## Artifacts
- `templates/kubernetes/serviceaccount-rbac.yaml`
- `templates/kubernetes/networkpolicy.example.yaml`
- `templates/kubernetes/external-secret.example.yaml`

