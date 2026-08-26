# Schema Manifest

The machine-readable contract is [`schema-manifest.json`](schema-manifest.json). This document explains the model at a glance.

Stable objects include `class_profile` and `student_master`. Event or assignment entities include `exam_batch`, `score_detail`, `growth_event`, `parent_contact`, `seat_assignment`, `duty_assignment`, and `committee_assignment`. Generated files are tracked as `artifact_record`.

Use one backend as the source of truth for a workspace. Feishu is the first live-tested adapter; Notion and Obsidian use the same schema through their adapter mappings and fixture tests.
