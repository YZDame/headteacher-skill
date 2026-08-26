#!/usr/bin/env python3
"""Environment checks for the portable headteacher plugin."""
import argparse, json, shutil, sys

def check_feishu():
    cli = shutil.which("lark-cli")
    return {"backend": "feishu_base", "lark_cli": bool(cli), "message": "lark-cli available" if cli else "Use a configured Feishu API/MCP connector or install lark-cli."}

def check_feishu_backend():
    cli = shutil.which("lark-cli")
    configured = False
    if cli:
        configured = True
    return {"backend": "feishu_base", "installed": bool(cli), "configured": configured, "message": check_feishu()["message"]}

def check_obsidian():
    cli = shutil.which("obsidian")
    return {"backend": "obsidian", "obsidian_cli": bool(cli), "message": "Obsidian CLI available" if cli else "Obsidian CLI not found; a local vault can still be used."}

def report():
    return {
        "runtime": {"supported": ["codex", "claude_code", "deepseek_harness"], "doubao": "import-guide"},
        "feishu": check_feishu(),
        "notion": {"backend": "notion", "message": "Verify an external Notion API/MCP connector."},
        "obsidian": check_obsidian(),
        "recommended_backend": "feishu_base",
        "source_of_truth": "single_backend_per_workspace",
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()
    data = report()
    if args.format == "json": print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print("# Headteacher Workbench doctor\n")
        print(f"- Supported runtimes: {', '.join(data['runtime']['supported'])}")
        print(f"- Feishu: {data['feishu']['message']}")
        print(f"- Notion: {data['notion']['message']}")
        print(f"- Obsidian: {data['obsidian']['message']}")
        print("- Workspace policy: one backend is the source of truth.")
    return 0

if __name__ == "__main__": sys.exit(main())
