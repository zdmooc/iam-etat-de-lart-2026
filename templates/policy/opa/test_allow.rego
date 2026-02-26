package iam.authz

test_allow_public_read {
  data.iam.authz.allow with input as {
    "user": {"id": "u1", "roles": ["viewer"]},
    "token": {"scopes": ["read"]},
    "resource": {"id": "r1", "classification": "public"}
  }
}
