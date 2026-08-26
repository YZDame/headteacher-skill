---
name: class-artifacts
description: Generate class-management Word, Excel, and PowerPoint artifacts from canonical records, including seat plans, duty schedules, notices, talk records, and parent-meeting materials.
license: MIT
---

# Class Artifacts

Generate files only after querying structured records and selecting a template.

## Workflow

1. Confirm the source entities, date range, audience, and output format.
2. Load the applicable template and artifact rules.
3. Render a draft or preview for review.
4. Write the final file only after confirmation.
5. Register the artifact with its source records and local path.

## Rules

- Never use an Office file as the primary database.
- Mark inferred or missing values clearly.
- Avoid exposing restricted student fields in shareable artifacts.
