# 班主任.Skill 安装说明

## skills.sh / compatible Agents

```bash
npx skills add YZDame/headteacher-skill --list
npx skills add YZDame/headteacher-skill --skill class-data
```

The repository follows the open `SKILL.md` format. Use `--skill` to install only a functional area, or install the complete bundle.

## Codex Plugin

The repository includes `.codex-plugin/plugin.json` and a repo marketplace. From the repository root, add the local marketplace and install `headteacher-workbench` using your Codex plugin commands.

## Claude Code

Use `npx skills add` or place the selected skill directories under `.claude/skills/`.

## DeepSeek Harness

Copy selected skill directories to `.dsh/skills/` or `.agents/skills/`. The harness discovers one-level bundles such as `skills/class-data/SKILL.md`.

## Feishu

Configure Feishu credentials and provide either a compatible API/MCP connector or `lark-cli`. Run:

```bash
python3 tools/setup_doctor.py --format markdown
python3 tools/feishu_bootstrap.py describe-limitations
```

The adapter inspects an existing Base before migration and never overwrites it by default.

## Notion and Obsidian

Notion requires an external API/MCP connection. Obsidian requires a local vault and optionally the Obsidian CLI. This repository supplies mappings, templates, and contract fixtures; it does not package credentials or remote connectors.
