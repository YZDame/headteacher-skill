# Backend Contract

Every adapter exposes the same conceptual operations:

- `check_prerequisites()`
- `authenticate()`
- `bootstrap_workspace(schema_manifest)`
- `read_entities(query_spec)`
- `write_entities(change_set)`
- `materialize_views(view_manifest)`
- `register_artifact(record)`
- `describe_limitations()`

Feishu is the first live-tested implementation. Notion and Obsidian provide mappings, configuration templates, and fixture tests until their external connectors are configured.
