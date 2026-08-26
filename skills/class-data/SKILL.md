---
name: class-data
description: Import, normalize, query, append, and update class-management records using the shared data contract. Use for rosters, exams, scores, growth events, communications, and workspace migrations.
license: MIT
---

# Class Data

Operate on canonical records, not backend-specific field guesses.

## Workflow

1. Load `references/data-contract.md` and validate input with `scripts/validate_schema.py`.
2. Identify the entity type and stable ID; create an ID only when the record has none.
3. Normalize dates, enums, nulls, provenance, visibility, and sensitivity.
4. For writes, show a change preview and require confirmation unless the user explicitly supplied dry-run mode.
5. Call the selected adapter and record the native record ID in `source`.

## Rules

- Use idempotent `upsert` for repeatable imports.
- Represent deletion as a tombstone; do not hard-delete student data by default.
- Never expose phone numbers, addresses, or national IDs unless necessary for the requested task.
