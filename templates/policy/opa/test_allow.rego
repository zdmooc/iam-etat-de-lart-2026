package iam.authz

import rego.v1

test_allow_public_read if {
  data.iam.authz.allow with input as {
    "user": {"id": "u1", "roles": ["viewer"]},
    "token": {"scopes": ["read"]},
    "resource": {"id": "r1", "classification": "public"},
  }
}

test_deny_private_without_admin if {
  not data.iam.authz.allow with input as {
    "user": {"id": "u2", "roles": ["viewer"]},
    "token": {"scopes": ["read"]},
    "resource": {"id": "r2", "classification": "private"},
  }
}
