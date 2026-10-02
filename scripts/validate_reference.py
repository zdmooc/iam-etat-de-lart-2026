from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

required = [
    ROOT / "architecture/HLD.md",
    ROOT / "architecture/LLD.md",
    ROOT / "architecture/ADR-001-authn-authz-boundaries.md",
    ROOT / "diagrams/iam-component.puml",
    ROOT / "diagrams/oidc-login-sequence.puml",
    ROOT / "evidence/CLAIM-EVIDENCE-MATRIX.md",
]

for path in required:
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"missing or empty required asset: {path.relative_to(ROOT)}")

private_key = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
jwt = re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    if private_key.search(text):
        errors.append(f"private key material: {path.relative_to(ROOT)}")
    if jwt.search(text):
        errors.append(f"JWT-like material: {path.relative_to(ROOT)}")

    if path.suffix in {".yaml", ".yml"}:
        try:
            list(yaml.safe_load_all(text))
        except Exception as exc:
            errors.append(f"invalid YAML {path.relative_to(ROOT)}: {exc}")

    if path.suffix == ".json":
        try:
            json.loads(text)
        except Exception as exc:
            errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

if errors:
    print("IAM_REFERENCE_VALIDATION=FAIL")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("IAM_REFERENCE_VALIDATION=PASS")
