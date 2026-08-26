# Adapter Contract

Adapters implement the same conceptual operations:

- `check_prerequisites()`
- `authenticate()`
- `bootstrap_workspace(schema_manifest)`
- `read_entities(query_spec)`
- `write_entities(change_set)`
- `materialize_views(view_manifest)`
- `register_artifact(record)`
- `describe_limitations()`

The Feishu adapter is the first live-tested implementation. Notion and Obsidian provide mapping, configuration templates, and fixture tests until their connectors are available.
