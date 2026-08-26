# Headteacher Workbench

`headteacher-skill` 是一个班级管理 Agent Skills 插件包。它把学生数据、成长记录、班务安排和文件生成拆成多个可独立调用的 Skills，并通过统一数据协议适配不同后端。

## 能力包

- `headteacher-workbench`：初始化与任务路由
- `class-data`：名单、考试、成绩和记录的导入、查询、追加、更新
- `student-growth`：德育表现、谈话、家校沟通和重点学生跟进
- `class-operations`：座位、值日、班委安排
- `class-artifacts`：Word、Excel、PPT 产物生成
- `feishu-adapter`、`notion-adapter`、`obsidian-adapter`：后端映射和配置

## 安装

```bash
npx skills add YZDame/headteacher-skill --list
npx skills add YZDame/headteacher-skill --skill class-data
```

Codex 可作为插件安装；Claude Code 和 DeepSeek Harness 可直接发现 `skills/<name>/SKILL.md`。DeepSeek Harness 也可以将这些目录复制到项目的 `.dsh/skills` 或 `.agents/skills`。

## 数据协议

统一协议位于 [`references/data-contract.md`](references/data-contract.md)，机器可校验的 Schema 位于 [`references/schema-manifest.json`](references/schema-manifest.json)。每个工作台选择一个后端作为数据源；协议负责统一实体、ID、时间、溯源、敏感级别和写入语义，v3 不做跨后端自动双向同步。

## 后端状态

| 后端 | 状态 |
|---|---|
| 飞书多维表格 | 首版优先接入，自动路由 API/MCP 或 `lark-cli`；真实写入需账号配置 |
| Notion | 数据源/页面映射和 fixture，需外部 API/MCP |
| Obsidian | Markdown/YAML/Bases 本地投影，需本地 vault |

仓库不携带账号、Token 或未经验证的 MCP 配置。请先阅读 [`INSTALL.md`](INSTALL.md) 和 [`references/capability-matrix.md`](references/capability-matrix.md)。

## 安全原则

敏感字段默认限制展示；批量写入、迁移和删除必须先预览并确认。Office 文件是下游产物，不是数据源。

## 许可证

MIT
