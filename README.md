# 同事.skill

把同事的技能与性格蒸馏成 AI Skill，让它替他工作。

提供同事的原材料（飞书消息、钉钉文档、邮件、截图）加上你的主观描述，生成一个**真正能替他工作的 AI Skill**——用他的技术规范写代码，用他的语气回答问题，知道他什么时候会甩锅。生成后支持持续进化，直接说「他不会这样」就能修正。

## 安装

### Claude Code

```bash
# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/titanwings/colleague-skill .claude/skills/create-colleague

# 或安装到全局（所有项目都能用）
git clone https://github.com/titanwings/colleague-skill ~/.claude/skills/create-colleague
```

> **注意**：Claude Code 从 git 仓库根目录的 `.claude/skills/` 查找 skill。如果 `/create-colleague` 无法识别，请确认你在正确的目录下执行了 clone。

### OpenClaw

```bash
git clone https://github.com/titanwings/colleague-skill ~/.openclaw/workspace/skills/create-colleague
```

### 依赖（可选）

```bash
pip3 install -r requirements.txt
```

## 使用

在 Claude Code 中输入：

```
/create-colleague
```

按提示输入同事姓名、公司职级（如 `字节 2-1 算法工程师`）、性格标签，然后选择数据来源（飞书/钉钉自动采集、上传文件、或直接粘贴）。全部可跳过，仅凭描述也能生成。

完成后用 `/{slug}` 调用该同事 Skill。

### 其他命令

| 命令 | 说明 |
|------|------|
| `/list-colleagues` | 列出所有同事 Skill |
| `/{slug}` | 调用完整 Skill（Persona + Work） |
| `/{slug}-work` | 仅工作能力 |
| `/{slug}-persona` | 仅人物性格 |
| `/colleague-rollback {slug} {version}` | 回滚到历史版本 |
| `/delete-colleague {slug}` | 删除 |

## 效果示例

输入：`字节 2-1 后端工程师，INTJ，甩锅高手，字节范`

```
用户      ❯ 帮我看一下这个接口设计

同事.skill ❯ 等等，这个接口的 impact 是什么？背景没说清楚。
             （看完后）N+1 查询，改掉。返回结构用统一的
             {code, message, data}，这是规范，不用问为什么。
```

```
用户      ❯ 这个 bug 是你引入的吧

同事.skill ❯ 上线时间对上了吗？那个需求改了好几个地方，还有其他变更。
```

## 数据来源

**自动采集**（推荐，输入姓名即可）

| 平台 | 消息记录 | 文档/Wiki | 多维表格 |
|------|:-------:|:---------:|:-------:|
| 飞书 | ✅ API | ✅ | ✅ |
| 钉钉 | ⚠️ 浏览器 | ✅ | ✅ |

**手动上传**：PDF、图片、飞书 JSON 导出、邮件 `.eml/.mbox`、Markdown、直接粘贴

首次使用飞书/钉钉自动采集需配置 App 凭证，详见 [INSTALL.md](INSTALL.md)。

## 生成的 Skill 结构

每个同事 Skill 由两部分组成：

- **Part A — Work Skill**：负责系统、技术规范、工作流程、经验知识库
- **Part B — Persona**：5 层性格结构（硬规则 → 身份 → 表达风格 → 决策模式 → 人际行为）

运行逻辑：接到任务 → Persona 判断态度 → Work Skill 执行 → 用他的语气输出

### 支持的标签

**个性**：认真负责 · 甩锅高手 · 完美主义 · 差不多就行 · 拖延症 · PUA 高手 · 职场政治玩家 · 向上管理专家 · 阴阳怪气 · 反复横跳 · 话少 · 只读不回 …

**企业文化**：字节范 · 阿里味 · 腾讯味 · 华为味 · 百度味 · 美团味 · 第一性原理 · OKR 狂热者 …

**职级**：字节 2-1~3-3+ · 阿里 P5~P11 · 腾讯 T1~T4 · 百度 T5~T9 · 美团 P4~P8 · 华为 13~21 级 …

### 进化

- **追加文件** → 自动分析增量 → merge 进对应部分，不覆盖已有结论
- **对话纠正** → 说「他不会这样，他应该是 xxx」→ 写入 Correction 层，立即生效
- **版本管理** → 每次更新自动存档，支持回滚

## 项目结构

本项目遵循 [AgentSkills](https://agentskills.io) 开放标准。整个 repo 就是一个 skill 目录：

```
create-colleague/
├── SKILL.md             # skill 入口
├── prompts/             # Prompt 模板（intake / analyzer / builder / merger）
├── tools/               # Python 工具（飞书/钉钉采集、邮件解析、版本管理）
├── colleagues/          # 生成的同事 Skill（gitignored）
├── docs/PRD.md
├── requirements.txt
└── LICENSE
```

## License

MIT
