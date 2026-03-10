#!/usr/bin/env python3
import json
import re
import base64
import hashlib
from pathlib import Path

BASE = Path(".")
MANIFEST = json.loads((BASE / "ARTIFACT_MANIFEST.json").read_text(encoding="utf-8"))
PEM_TEXT = (BASE / "artifacts_pem.txt").read_text(encoding="utf-8")
OUT = BASE / "decoded_artifacts"
OUT.mkdir(exist_ok=True)

def extract_block(label: str) -> bytes:
    pattern = rf"-----BEGIN {re.escape(label)}-----\s*(.*?)\s*-----END {re.escape(label)}-----"
    m = re.search(pattern, PEM_TEXT, re.DOTALL)
    if not m:
        raise RuntimeError(f"No se encontró bloque PEM para label={label}")
    b64 = re.sub(r"\s+", "", m.group(1))
    return base64.b64decode(b64)

for item in MANIFEST["artifacts"]:
    name = item["name"]
    label = item["pem_label"]
    expected_sha256 = item["sha256"]
    expected_size = item["size_bytes"]

    data = extract_block(label)

    got_sha256 = hashlib.sha256(data).hexdigest()
    got_size = len(data)

    if got_sha256 != expected_sha256:
        raise RuntimeError(f"SHA256 inválido para {name}: {got_sha256} != {expected_sha256}")
    if got_size != expected_size:
        raise RuntimeError(f"SIZE inválido para {name}: {got_size} != {expected_size}")

    out_path = OUT / name
    out_path.write_bytes(data)
    print(f"[OK] {out_path} ({got_size} bytes)")

print("[OK] Extracción finalizada en decoded_artifacts/")
