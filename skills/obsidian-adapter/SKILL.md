---
name: obsidian-adapter
description: Project class-management records into an Obsidian vault using Markdown, YAML frontmatter, and Bases views. Use for local-first class records and queries.
license: MIT
---

# Obsidian Adapter

Treat the vault as a local projection of canonical records.

## Workflow

1. Confirm the vault path and allowed folders.
2. Map stable objects to Markdown notes and event entities to dated notes or JSONL.
3. Keep canonical fields in YAML frontmatter and human prose in the note body.
4. Generate or refresh Bases views from the same field vocabulary.

## Rules

- Do not describe Obsidian as a remote database equivalent to Feishu.
- Keep private vault paths and student data out of committed examples.
- Preview bulk file changes before applying them.
