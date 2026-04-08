# Setup Workflow

Use this prompt when the workspace has not been initialized yet.

## Goal

Turn a fresh installation into a usable headteacher workspace.

## Default behavior

1. Check whether `./.headteacher-skill/workspace_manifest.json` exists.
2. If missing, enter setup mode immediately.
3. Run:

```bash
python3 tools/setup_doctor.py --format markdown
```

4. Recommend `feishu_base` unless the user explicitly prefers another backend.
5. If the user accepts Feishu, guide them through:
   - installing or verifying `lark-cli`
   - running `lark-cli config init --new` if needed
   - bootstrapping the workspace with `tools/feishu_bootstrap.py`
6. If the user selects Notion, verify that Notion MCP is connected. If not, stop at external setup guidance.
7. If the user selects Obsidian, verify that Obsidian CLI is installed and remind them to install the official Obsidian skill if needed.
6. After bootstrap, explain what tasks the user can run next.

## Required outputs

- environment status
- chosen backend
- whether the workspace is initialized
- next available actions

## Do not do

- do not role-play a teacher
- do not ask persona questions
- do not jump into file generation before setup is complete
- do not pretend this repository contains Notion MCP or Obsidian CLI capabilities
