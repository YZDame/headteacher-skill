# 班主任.Skill 安装说明

## 安装到 Claude Code

```bash
mkdir -p .claude/skills
git clone https://github.com/YZDame/headteacher-skill .claude/skills/headteacher-workbench
```

全局安装：

```bash
git clone https://github.com/YZDame/headteacher-skill ~/.claude/skills/headteacher-workbench
```

## 安装到 OpenClaw

```bash
git clone https://github.com/YZDame/headteacher-skill ~/.openclaw/workspace/skills/headteacher-workbench
```

## Python 依赖

```bash
pip3 install -r requirements.txt
```

## 飞书后端前置条件

若你打算使用飞书多维表格作为工作台后端：

1. 安装 `lark-cli`
2. 在首次运行 Skill 时完成 `lark-cli config init --new`
3. 让 Skill 使用 `tools/setup_doctor.py` 和 `tools/feishu_bootstrap.py` 完成检查与初始化

Skill 的默认建议顺序是：

1. 先做环境检查
2. 再选后端
3. 最后初始化工作台

## 其他后端

### Notion

第一版只提供结构映射和最小初始化说明，不承诺完整自动写入链路。

### Obsidian

第一版只提供目录骨架、模板和数据规范说明，不承诺完整结构化数据库体验。
