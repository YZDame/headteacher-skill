# 班主任.Skill

[English](README.en.md) · [论文](https://github.com/YZDame/headteacher-skill/blob/main/paper/headteacher_skill_paper.pdf)

`headteacher-skill` 是一个面向班级治理的可移植 Agent Skills 插件包。它把班主任工作拆成 5 个业务 Skills 和 3 个后端适配 Skills，并用一套统一的数据协议连接飞书多维表格、Notion 与 Obsidian。每个 Skill 都可以单独发现和安装，也可以作为完整插件一起安装。

## 快速安装

### 提示词安装（推荐）

把下面这段提示词发送给正在使用的 Agent。它适用于 Codex、Claude Code、DSH、豆包工作台、WorkBuddy、千问办公等能够读取 GitHub 仓库或导入 `SKILL.md` 的环境：

```text
请安装 https://github.com/YZDame/headteacher-skill 中的班级管理 Skills。先阅读 README.md、INSTALL.md 和 references/data-contract.md，列出 skills/ 下每个 Skill 的用途，让我选择安装全部 Skills 还是其中几个。若当前环境支持插件，请执行 npx plugins add YZDame/headteacher-skill；若支持 Skills CLI，请执行 npx skills add YZDame/headteacher-skill；若只能导入本地目录，请导入所选 Skill 的完整文件夹，不要只复制 SKILL.md。安装后检查各个 SKILL.md 是否能被发现，说明当前 Agent、后端连接器、凭据和本地工具还缺什么；不要假设已经连上飞书、Notion 或 Obsidian，也不要把任何凭据写入仓库。
```

安装完成后，让 Agent 报告：已安装的 Skill、未满足的依赖、选定的数据源后端，以及任何需要人工确认的写入操作。

### 命令行安装

支持 Plugins CLI 的环境可以安装完整插件：

```bash
npx plugins add YZDame/headteacher-skill
```

支持 Skills CLI 的环境可以先查看清单，再安装完整包或单个 Skill：

```bash
npx skills add YZDame/headteacher-skill --list
npx skills add YZDame/headteacher-skill
npx skills add YZDame/headteacher-skill --skill class-data
```

把 `class-data` 换成下表中的其他名称即可。Codex 也可以读取仓库中的 `.codex-plugin/plugin.json` 和 `.agents/plugins/marketplace.json`，按其插件界面完成安装。

### 手动导入

下载仓库并从 `skills/` 中选择完整的 Skill 文件夹。不同 Agent 的目录约定可能不同，常见位置包括项目级 `.agents/skills/`、`.dsh/skills/` 和 `.claude/skills/`；豆包工作台、WorkBuddy、千问办公等产品可以通过各自的技能导入界面添加。完整文件夹可能包含脚本和参考资料，不要只复制 `SKILL.md`。

## Skill 清单

### 业务 Skills

| Skill | 用途 |
| --- | --- |
| `headteacher-workbench` | 初始化工作台、选择数据源并把请求路由到正确的 Skill |
| `class-data` | 按统一协议导入、规范化、查询、追加和更新班级记录 |
| `student-growth` | 记录和整理成长事件、表现、干预、家校沟通与学生时间线 |
| `class-operations` | 根据明确约束生成座位、值日、班委等班务安排 |
| `class-artifacts` | 从规范记录生成 Word、Excel、PPT 等班级工作产物 |

### 后端适配 Skills

| Skill | 用途 |
| --- | --- |
| `feishu-adapter` | 将统一协议映射到飞书多维表格，检查环境、预览变更并执行受确认的读写 |
| `notion-adapter` | 将实体映射到 Notion data source、页面、属性和关系 |
| `obsidian-adapter` | 将记录投影到 Obsidian Markdown、YAML frontmatter 和 Bases 视图 |

## 统一数据协议

规范见 [`references/data-contract.md`](references/data-contract.md)，机器可校验的 Schema 见 [`references/schema-manifest.json`](references/schema-manifest.json)。每个工作台选择一个后端作为事实来源，适配器只负责映射，不做未经请求的跨后端双向同步。

- 请求或变更集包含 `protocol_version`、`operation`、`request_id`、`workspace_id`、`actor`、`emitted_at`、`dry_run` 和 `records`。
- 每条记录包含稳定的 `entity_type`、`entity_id`、`class_id`、`revision`、`occurred_at`、`source`、`visibility`、`sensitivity` 和 `payload`。
- 支持 `import`、`append`、`upsert`、`query`、`tombstone` 和 `export`；重复写入应保持幂等，删除用需要确认的 tombstone 表示。
- 生成的 Office 文件属于下游产物，必须登记其来源记录，不能反过来充当主数据库。

## 后端状态

| 后端 | 当前状态 | 使用前提 |
| --- | --- | --- |
| 飞书多维表格 | 首个优先适配器；仓库包含连接路由、Schema 映射和迁移检查 | 飞书凭据，以及可用的 API/MCP 或 `lark-cli`；真实写入仍需预览和确认 |
| Notion | 适配器骨架、字段映射和 fixture | 已连接的 Notion API/MCP；当前不宣称与飞书能力等价 |
| Obsidian | 本地投影适配器和 fixture | 本地 vault，可选 Obsidian CLI；它是本地知识库投影，不是远程数据库 |

仓库不携带账号、Token、学生数据或未经验证的远程连接器。运行前可执行：

```bash
python3 tools/setup_doctor.py --format markdown
python3 tools/feishu_bootstrap.py describe-limitations
```

## 安全边界

敏感字段默认限制展示。导入、追加、迁移、批量写入和 tombstone 都应先给出预览，再获得确认；学生电话、地址和证件号码不能在不必要的场景中暴露。系统不会根据单次观察推断诊断或给学生贴标签。

## 仓库结构

```text
headteacher-skill/
├── .codex-plugin/plugin.json
├── .agents/plugins/marketplace.json
├── skills/                  # 8 个可独立发现的 Skills
├── references/              # 数据协议、Schema、适配器和安全边界
├── scripts/                 # Schema 与契约校验
├── tools/                   # 环境检查、迁移和后端辅助工具
├── paper/                   # 项目说明论文与编译后的 PDF
├── INSTALL.md
├── README.md
├── README.en.md
└── LICENSE
```

## 许可证

本仓库原创内容使用 MIT License。使用外部 Agent、连接器或平台时，仍应遵守其各自的服务条款、许可证和数据保护要求。
