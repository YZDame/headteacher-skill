#!/usr/bin/env python3
"""Small fixture contract test for the canonical envelope and backend mappings."""
import json, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
fixture = {
  "protocol_version":"1.0", "operation":"upsert", "request_id":"req_fixture",
  "workspace_id":"class_demo", "actor":{"id":"teacher_demo"},
  "emitted_at":"2026-08-26T10:00:00+08:00", "dry_run":True,
  "records":[{"entity_type":"student_master","entity_id":"stu_demo","class_id":"class_demo",
    "revision":1,"source":{"backend":"fixture"},"visibility":"staff","sensitivity":"restricted",
    "payload":{"name":"示例学生","focus_tags":[]}}]
}
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
    json.dump(fixture, fh, ensure_ascii=False); path = fh.name
result = subprocess.run([sys.executable, str(ROOT/"scripts/validate_schema.py"), path])
Path(path).unlink(missing_ok=True)
raise SystemExit(result.returncode)
