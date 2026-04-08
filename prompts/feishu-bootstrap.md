# Feishu Bootstrap

Use this prompt when the selected backend is `feishu_base`.

## Prerequisites

Run:

```bash
python3 tools/setup_doctor.py --backend feishu_base --format markdown
```

If `lark-cli` is missing, guide installation first.

If `lark-cli` is not configured, guide:

```bash
lark-cli config init --new
```

## Bootstrap path

### New workspace

Use:

```bash
python3 tools/feishu_bootstrap.py bootstrap --workspace-name "<class-name>" --format markdown
```

### Existing Base provided by user

Inspect first:

```bash
python3 tools/migration_inspector.py feishu --base-token "<base-token>" --format markdown
```

Then decide:

- connect existing headteacher base
- or copy-and-refactor a subject-teacher base

## Rules

- do not overwrite an existing Base by default
- classify first, migrate second
- write the local workspace manifest after bootstrap succeeds
- keep the user informed of created tables, views, and local manifest path
