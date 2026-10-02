# HLD — Enterprise IAM Reference Architecture

**Classification:** REFERENCE_DESIGN  
**Runtime status:** NOT_RUNTIME_PROVEN

## 1. Purpose

Define an enterprise IAM architecture covering workforce, partners, CIAM and non-human identities while separating authentication, authorization, identity lifecycle, privileged access and risk response.

## 2. Architecture drivers

- standards-based SSO and federation;
- phishing-resistant authentication for sensitive populations;
- lifecycle automation and rapid deprovisioning;
- least privilege and fine-grained authorization;
- reduction of long-lived secrets;
- auditability and continuous access/risk response;
- Kubernetes/OpenShift workload identity;
- clear separation between IdP, API gateway, application authorization and PDP/PEP.

## 3. Logical architecture

```text
HR / Authoritative Sources
          |
   Directory / Identity Graph
          |
   +------+----------------------+
   |                             |
IdP / Federation             Provisioning
OIDC / SAML / MFA              SCIM/JML
   |                             |
   +----> Apps / API Gateway <---+
              |
           PEP/API
              |
             PDP
        RBAC/ABAC/ReBAC
              |
        Business Services

PAM/JIT ----> privileged paths
ITDR/SIEM --> risk signals/session response
Workload Identity --> Kubernetes/OpenShift services
```

## 4. Trust boundaries

- authoritative identity source to identity plane;
- identity plane to applications;
- external/partner federation boundary;
- gateway to backend service;
- PDP decision boundary;
- privileged administration boundary;
- workload/service identity boundary.

## 5. Core principles

1. Authentication and business authorization are separate concerns.
2. OIDC first for modern applications; SAML retained for justified legacy/federation.
3. Short-lived tokens and least-privilege scopes/audiences.
4. JML lifecycle is governed from authoritative sources.
5. Privileged access is time-bound and audited.
6. Fine-grained authorization is externalized only when it improves consistency and governance.
7. Non-human identities avoid shared long-lived secrets.
8. Risk can change during a session; response must not end at login time.

## 6. NFR

- availability targets depend on population and business service;
- recovery objectives must cover both identity service and authoritative dependencies;
- audit logs must be exportable to SIEM;
- capacity planning must consider authentication peaks and token traffic;
- configuration changes must be governed and reversible.

## 7. Portfolio relationship

This repository owns the vendor-neutral IAM reference architecture. Deep Keycloak implementation and runtime evidence are owned by `zdmooc/keycloak-enterprise-roadmap-v7`.

## 8. Detailed design

See `architecture/LLD.md`.
