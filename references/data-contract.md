# Headteacher Data Contract v1.0

The contract is backend-neutral. Each workspace chooses one backend as its source of truth; adapters project the same records without automatic cross-backend sync.

## Envelope

Every request or change set contains `protocol_version`, `operation`, `request_id`, `workspace_id`, `actor`, `emitted_at`, `dry_run`, and `records`.

Supported operations: `import`, `append`, `upsert`, `query`, `tombstone`, and `export`.

## Record invariants

Each record contains `entity_type`, `entity_id`, `class_id`, `revision`, `occurred_at`, `source`, `visibility`, `sensitivity`, and `payload`. IDs are stable within a workspace. Timestamps use ISO 8601 with an explicit offset. Unknown fields must be preserved under `payload` or reported as warnings; they must not be silently discarded.

## Safety and sync

- Writes are idempotent when the same `entity_id` and revision are replayed.
- Deletion is represented by a tombstone and requires confirmation.
- Existing backends are inspected before migration.
- Phone numbers, addresses, and national IDs are restricted by default.
- Generated Office files are downstream artifacts and must reference their source records.
