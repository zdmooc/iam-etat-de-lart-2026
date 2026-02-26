package iam.authz

default allow := false

# Exemple: autoriser si le rôle "admin" est présent
allow {
  some r
  r := input.user.roles[_]
  r == "admin"
}

# Exemple: autoriser lecture si scope "read" et ressource publique
allow {
  input.token.scopes[_] == "read"
  input.resource.classification == "public"
}
