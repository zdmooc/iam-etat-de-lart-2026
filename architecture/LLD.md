# LLD — Enterprise IAM Integration Contract

**Classification:** IMPLEMENTATION_CONTRACT  
**Runtime status:** NOT_RUNTIME_PROVEN

## 1. Scope

Translate the IAM HLD into concrete integration contracts for applications, APIs and Kubernetes/OpenShift workloads.

## 2. OIDC application contract

For a modern web/mobile application:
- Authorization Code flow;
- PKCE where applicable;
- exact redirect URIs;
- explicit issuer;
- explicit client type;
- minimal scopes;
- audience designed for the target API;
- token/session lifetimes documented;
- logout/revocation behavior documented.

## 3. API validation contract

A resource server/gateway validates at minimum:
- signature against trusted JWKS;
- `iss`;
- `aud`;
- `exp` / `nbf`;
- accepted algorithm;
- required scope/claims.

A valid token does not replace object/function/business authorization.

## 4. Authorization contract

```text
PEP = gateway / service / application
PDP = policy decision service when externalized
PIP = trusted attributes/context
PAP = governed policy administration
```

Decision input must be bounded and auditable. Fail-open/fail-closed behavior is a conscious architecture decision.

## 5. SCIM/JML contract

Minimum lifecycle events:
- joiner: create identity/account and baseline access;
- mover: update attributes/groups/entitlements;
- leaver: disable access promptly and revoke privileged access;
- recertification: periodically review high-risk access.

SCIM payloads and identity ownership must be governed separately from authentication.

## 6. Workforce / CIAM separation

Do not assume one realm/tenant/directory design fits all populations. Separate at least:
- ownership;
- policies;
- registration/recovery;
- consent/privacy;
- fraud/risk controls;
- support model;
- lifecycle.

## 7. Privileged access

- named administration accounts;
- MFA resistant to phishing where possible;
- JIT/JEA;
- approval/audit;
- break-glass procedure;
- secret rotation;
- session monitoring where policy requires it.

## 8. Workload identity

For Kubernetes/OpenShift:
- one ServiceAccount per workload responsibility;
- projected/short-lived credentials when supported;
- no shared service account;
- runtime secret delivery for unavoidable secrets;
- RBAC least privilege;
- network policy and audit linkage.

## 9. Observability and audit

Correlate:
- authentication event;
- client/application;
- subject/service identity;
- authorization decision;
- privileged elevation;
- provisioning change;
- risk signal/session action.

Do not log bearer tokens or sensitive authentication material.

## 10. Failure modes

| Failure | Design question |
|---|---|
| IdP unavailable | what continues with already-issued locally validated tokens? |
| directory unavailable | can authentication continue and for how long? |
| PDP unavailable | fail closed or bounded cached decision? |
| SCIM target unavailable | queue/retry/reconciliation behavior? |
| SIEM unavailable | local buffering and audit durability? |
| secret manager unavailable | startup/runtime behavior and recovery? |

## 11. Evidence boundary

This LLD is a design contract. Runtime proof is recorded in specialist implementation repositories, not inferred from this document.
