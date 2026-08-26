# Headteacher Workbench

`headteacher-skill` is a portable Agent Skills plugin bundle for class management. It separates data operations, student growth, class operations, artifact generation, and backend adapters.

Install with `npx skills add YZDame/headteacher-skill --list`, or install the Codex Plugin bundle. The canonical data contract is documented in `references/data-contract.md`; Feishu is the first prioritized backend, while Notion and Obsidian adapters ship with mappings and fixtures. Live writes require user-provided credentials.

Sensitive fields are restricted by default. Writes, migrations, and tombstones require preview and confirmation. Credentials and connectors remain external to this repository.
