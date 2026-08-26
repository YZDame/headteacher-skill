---
name: feishu-adapter
description: Connect the shared class-management data contract to Feishu Base. Use when configuring, inspecting, bootstrapping, reading, or writing Feishu tables.
license: MIT
---

# Feishu Adapter

Route through the first available configured connector: compatible API/MCP, then `lark-cli`.

## Workflow

1. Run `python3 tools/setup_doctor.py --format markdown`.
2. Inspect an existing Base before proposing migration.
3. Map canonical entities to one table per entity using `references/schema-manifest.json`.
4. Preview schema or record changes before applying them.
5. Preserve Feishu table/record IDs in the canonical `source` object.

## Rules

- Do not overwrite an existing Base by default.
- Keep schema changes additive unless migration is explicitly confirmed.
- Never store credentials in this repository.
