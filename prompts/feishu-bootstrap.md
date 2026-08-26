# Feishu bootstrap

Use `references/schema-manifest.json` as the source of truth. Route through a configured Feishu API/MCP connector when available, otherwise use `lark-cli`.

Before creating or changing a Base:

1. Check prerequisites with `python3 tools/setup_doctor.py --format markdown`.
2. Inspect existing tables and classify reusable fields.
3. Show the planned schema and mappings.
4. Apply only after confirmation.

Never overwrite an existing Base by default, and never commit credentials.
