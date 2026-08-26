# Headteacher Skill

[中文说明](README.md) · [Paper](https://github.com/YZDame/headteacher-skill/blob/main/paper/headteacher_skill_paper.pdf)

`headteacher-skill` is a portable Agent Skills plugin bundle for class management. It separates five functional Skills from three backend adapters and connects them with one backend-neutral data contract. Each Skill can be discovered and installed independently, or the complete bundle can be installed as a plugin.

## Quick installation

### Prompt installation (recommended)

Send this prompt to the Agent you are using. It works for Codex, Claude Code, DSH, Doubao Workbench, WorkBuddy, Qianwen Office, and other clients that can read a GitHub repository or import `SKILL.md`:

```text
Please install the class-management Skills from https://github.com/YZDame/headteacher-skill. First read README.md, INSTALL.md, and references/data-contract.md. List every Skill under skills/ with its purpose and let me choose between the complete bundle and selected Skills. If this environment supports Plugins CLI, run npx plugins add YZDame/headteacher-skill; if it supports Skills CLI, run npx skills add YZDame/headteacher-skill; if it only supports local directories, import the complete folder for each selected Skill rather than copying only SKILL.md. After installation, verify that the SKILL.md files are discoverable, report missing Agent capabilities, backend connectors, credentials, and local tools, and do not assume that Feishu, Notion, or Obsidian is connected. Never write credentials into the repository.
```

Ask the Agent to report the installed Skills, missing prerequisites, selected source-of-truth backend, and any write operation that still requires human confirmation.

### CLI installation

For environments with Plugins CLI:

```bash
npx plugins add YZDame/headteacher-skill
```

For environments with Skills CLI:

```bash
npx skills add YZDame/headteacher-skill --list
npx skills add YZDame/headteacher-skill
npx skills add YZDame/headteacher-skill --skill class-data
```

Replace `class-data` with any other Skill name in the tables below. Codex can also use `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` to install the bundle through its plugin interface.

### Manual import

Download the repository and import complete folders from `skills/`. Depending on the client, common project-level locations include `.agents/skills/`, `.dsh/skills/`, and `.claude/skills/`. Doubao Workbench, WorkBuddy, and Qianwen Office can use their own Skill import UI. A complete Skill folder may include scripts and references; do not copy only `SKILL.md`.

## Skill inventory

### Functional Skills

| Skill | Purpose |
| --- | --- |
| `headteacher-workbench` | Initialize a workspace, select a backend, and route requests |
| `class-data` | Import, normalize, query, append, and update canonical class records |
| `student-growth` | Record growth events, conduct, interventions, parent contacts, and timelines |
| `class-operations` | Generate seats, duty schedules, committees, and other arrangements from constraints |
| `class-artifacts` | Generate Word, Excel, and PowerPoint artifacts from canonical records |

### Backend adapter Skills

| Skill | Purpose |
| --- | --- |
| `feishu-adapter` | Map the contract to Feishu Base, inspect prerequisites, preview changes, and perform confirmed reads/writes |
| `notion-adapter` | Map entities to Notion data sources, pages, properties, and relations |
| `obsidian-adapter` | Project records into Obsidian Markdown, YAML frontmatter, and Bases views |

## Shared data contract

The canonical specification is [`references/data-contract.md`](references/data-contract.md), with a machine-readable Schema at [`references/schema-manifest.json`](references/schema-manifest.json). Each workspace chooses one backend as its source of truth. Adapters map records to that backend; they do not perform unrequested bidirectional synchronization.

- Requests and change sets contain `protocol_version`, `operation`, `request_id`, `workspace_id`, `actor`, `emitted_at`, `dry_run`, and `records`.
- Records carry stable `entity_type`, `entity_id`, `class_id`, `revision`, `occurred_at`, `source`, `visibility`, `sensitivity`, and `payload` fields.
- Supported operations are `import`, `append`, `upsert`, `query`, `tombstone`, and `export`. Replayed writes should be idempotent; deletion is represented by a confirmed tombstone.
- Office files are downstream artifacts and must reference their source records. They are not the primary database.

## Backend status

| Backend | Current status | Prerequisites |
| --- | --- | --- |
| Feishu Base | First prioritized adapter with connector routing, Schema mapping, and migration inspection | Feishu credentials plus API/MCP or `lark-cli`; live writes still require preview and confirmation |
| Notion | Adapter skeleton, field mappings, and fixtures | A connected Notion API/MCP; parity with Feishu is not claimed |
| Obsidian | Local projection adapter and fixtures | A local vault and optionally the Obsidian CLI; it is a local projection, not a remote database |

The repository contains no credentials, tokens, student data, or unverified remote connectors. Check the local environment with:

```bash
python3 tools/setup_doctor.py --format markdown
python3 tools/feishu_bootstrap.py describe-limitations
```

## Safety boundaries

Sensitive fields are restricted by default. Imports, appends, migrations, bulk writes, and tombstones require a preview and confirmation. Phone numbers, addresses, and national IDs should not be exposed unless the task requires them. A single observation must not be turned into a diagnosis or a student label.

## Repository layout

```text
headteacher-skill/
├── .codex-plugin/plugin.json
├── .agents/plugins/marketplace.json
├── skills/                  # 8 independently discoverable Skills
├── references/              # Contract, Schema, adapter, and safety docs
├── scripts/                 # Contract and Schema validation
├── tools/                   # Doctor, migration, and backend helpers
├── paper/                   # Project paper and compiled PDF
├── INSTALL.md
├── README.md
├── README.en.md
└── LICENSE
```

## License

Original content in this repository is released under the MIT License. External Agents, connectors, and platforms remain subject to their own terms, licenses, and data-protection requirements.
