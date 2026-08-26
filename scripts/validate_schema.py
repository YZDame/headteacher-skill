#!/usr/bin/env python3
"""Validate a headteacher data-contract JSON document without external dependencies."""
import json, sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "references/schema-manifest.json").read_text())
ENTITIES = set(SCHEMA["$defs"]["record"]["properties"]["entity_type"]["enum"])
OPS = set(SCHEMA["properties"]["operation"]["enum"])

def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    return 1

def validate(doc):
    required = ["protocol_version", "operation", "request_id", "workspace_id", "emitted_at", "dry_run", "records"]
    missing = [k for k in required if k not in doc]
    if missing: return fail("missing envelope fields: " + ", ".join(missing))
    if doc["protocol_version"] != "1.0": return fail("protocol_version must be 1.0")
    if doc["operation"] not in OPS: return fail("unsupported operation")
    if not isinstance(doc["records"], list): return fail("records must be an array")
    try: datetime.fromisoformat(doc["emitted_at"].replace("Z", "+00:00"))
    except ValueError: return fail("emitted_at must be ISO 8601 date-time")
    fields = {"entity_type","entity_id","class_id","revision","source","visibility","sensitivity","payload"}
    for i, record in enumerate(doc["records"]):
        if not isinstance(record, dict): return fail(f"records[{i}] must be an object")
        if fields - record.keys(): return fail(f"records[{i}] missing: {', '.join(sorted(fields-record.keys()))}")
        if record["entity_type"] not in ENTITIES: return fail(f"records[{i}] has unknown entity_type")
        if not isinstance(record["revision"], int) or record["revision"] < 1: return fail(f"records[{i}].revision must be a positive integer")
        if record["visibility"] not in {"staff","restricted","shareable"}: return fail(f"records[{i}].visibility invalid")
        if record["sensitivity"] not in {"public","internal","restricted","highly_restricted"}: return fail(f"records[{i}].sensitivity invalid")
        if not isinstance(record["payload"], dict): return fail(f"records[{i}].payload must be an object")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2: raise SystemExit("usage: validate_schema.py contract.json")
    try: document = json.loads(Path(sys.argv[1]).read_text())
    except Exception as exc: raise SystemExit(f"invalid JSON: {exc}")
    raise SystemExit(validate(document))
