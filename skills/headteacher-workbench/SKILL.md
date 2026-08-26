---
name: headteacher-workbench
description: Set up and route a class-management workspace. Use when a teacher needs to choose a backend, initialize class data, or coordinate student, operations, and artifact skills.
license: MIT
---

# 班主任.Skill

Use this skill as the entry point for class-management work.

## Workflow

1. Read `references/data-contract.md` and `references/capability-matrix.md`.
2. Check the local environment with `python3 tools/setup_doctor.py --format markdown`.
3. Ask which single backend is the source of truth for this workspace.
4. Route data tasks to `class-data`, student follow-up to `student-growth`, class arrangements to `class-operations`, and files to `class-artifacts`.
5. Require a preview and confirmation before any write, migration, or destructive change.

## Rules

- Do not invent connector access or credentials.
- Treat generated Office files as downstream artifacts, never as the source of truth.
- Keep backend-specific details in the adapter skills and references.
