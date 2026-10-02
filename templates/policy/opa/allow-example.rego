package iam.authz

import rego.v1

default allow := false

# Autoriser si le rôle "admin" est présent.
allow if {
  "admin" in input.user.roles
}

# Autoriser la lecture si le scope "read" est présent et la ressource publique.
allow if {
  "read" in input.token.scopes
  input.resource.classification == "public"
}
