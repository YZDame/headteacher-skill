#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any, Dict, Optional


WORKSPACE_MANIFEST = Path(".headteacher-skill/workspace_manifest.json")


def parse_embedded_json(text: str) -> Optional[Dict[str, Any]]:
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None


def run_command(cmd: list[str]) -> Dict[str, Any]:
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def check_python_module(module_name: str) -> bool:
    try:
        importlib.import_module(module_name)
        return True
    except Exception:
        return False


def check_feishu_backend() -> Dict[str, Any]:
    path = shutil.which("lark-cli")
    if not path:
        return {
            "backend": "feishu_base",
            "installed": False,
            "configured": False,
            "status": "missing_cli",
            "recommendation": "Install lark-cli first.",
        }

    config = run_command(["lark-cli", "config", "show"])
    parsed = parse_embedded_json(config["stdout"])
    configured = bool(parsed and parsed.get("appId"))
    users = parsed.get("users") if parsed else None
    status = "ready" if configured else "needs_config"

    return {
        "backend": "feishu_base",
        "installed": True,
        "configured": configured,
        "status": status,
        "binary": path,
        "config_path": str(Path.home() / ".lark-cli" / "config.json"),
        "brand": parsed.get("brand") if parsed else None,
        "users": users,
        "recommendation": "Run `lark-cli config init --new`." if not configured else "Feishu backend is available.",
    }


def check_obsidian_backend() -> Dict[str, Any]:
    path = shutil.which("obsidian")
    return {
        "backend": "obsidian",
        "installed": bool(path),
        "status": "placeholder_ready" if path else "missing_cli",
        "binary": path,
        "recommendation": "Install the Obsidian CLI and the official Obsidian-related skill, then verify local access."
        if not path
        else "Obsidian CLI is installed; also verify the official Obsidian-related skill in the agent environment.",
    }


def check_notion_backend() -> Dict[str, Any]:
    return {
        "backend": "notion",
        "installed": None,
        "status": "manual_verification_required",
        "recommendation": "Verify that Notion MCP is connected and available in the current agent environment.",
    }


def check_artifact_stack() -> Dict[str, Any]:
    return {
        "python_docx": check_python_module("docx"),
        "openpyxl": check_python_module("openpyxl"),
        "python_pptx": check_python_module("pptx"),
    }


def build_report(focus_backend: Optional[str]) -> Dict[str, Any]:
    backends = {
        "feishu_base": check_feishu_backend(),
        "notion": check_notion_backend(),
        "obsidian": check_obsidian_backend(),
        "local_only": {
            "backend": "local_only",
            "status": "always_available",
            "recommendation": "Use the local schema plan and defer backend setup.",
        },
    }
    if focus_backend:
        selected = {focus_backend: backends[focus_backend]}
    else:
        selected = backends

    recommended_backend = "feishu_base" if backends["feishu_base"]["installed"] else "local_only"
    return {
        "workspace_manifest_exists": WORKSPACE_MANIFEST.exists(),
        "workspace_manifest_path": str(WORKSPACE_MANIFEST),
        "recommended_backend": recommended_backend,
        "artifact_stack": check_artifact_stack(),
        "backends": selected,
    }


def render_markdown(report: Dict[str, Any]) -> str:
    lines = ["# Setup Doctor", ""]
    lines.append(f"- Workspace manifest present: `{report['workspace_manifest_exists']}`")
    lines.append(f"- Workspace manifest path: `{report['workspace_manifest_path']}`")
    lines.append(f"- Recommended backend: `{report['recommended_backend']}`")
    lines.append("")
    lines.append("## Artifact stack")
    lines.append("")
    for name, available in report["artifact_stack"].items():
        lines.append(f"- {name}: `{available}`")
    lines.append("")
    lines.append("## Backends")
    lines.append("")
    for backend_name, data in report["backends"].items():
        lines.append(f"### {backend_name}")
        for key in ["status", "installed", "configured", "binary", "users", "recommendation"]:
            if key in data and data[key] is not None:
                lines.append(f"- {key}: `{data[key]}`")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check local prerequisites for the headteacher workbench.")
    parser.add_argument(
        "--backend",
        choices=["feishu_base", "notion", "obsidian", "local_only"],
        help="Focus on a single backend.",
    )
    parser.add_argument("--format", default="json", choices=["json", "markdown"], help="Output format.")
    args = parser.parse_args()

    report = build_report(args.backend)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
