# Migration to v3

v3 removes the legacy root Skill entry point and obsolete runtime-specific routing. Install the desired Skill from `skills/`, or install the Codex Plugin bundle.

Existing Feishu Bases must be inspected before migration. Score columns should be normalized into `score_detail`; activity logs should become `growth_event` records. Keep native record IDs in each record's `source` object.
