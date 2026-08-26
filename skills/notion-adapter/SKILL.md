---
name: notion-adapter
description: Map the shared class-management contract to Notion databases, data sources, pages, and relations. Use when planning or configuring Notion access.
license: MIT
---

# Notion Adapter

Use the canonical schema and map each entity to a Notion data source or page structure.

## Workflow

1. Verify that Notion tools are available before claiming live access.
2. Read `references/schema-manifest.json` and `references/adapter-contract.md`.
3. Preview database/property mappings and relation fields.
4. Run fixture mapping tests when live access is unavailable.

## Rules

- Distinguish database containers, data sources, and page records.
- Do not claim parity with Feishu until live connector tests pass.
