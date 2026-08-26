# Setup workflow

1. Run `python3 tools/setup_doctor.py --format markdown`.
2. Ask the user to choose one source-of-truth backend.
3. Verify credentials or local paths without printing secrets.
4. Inspect an existing backend before migration.
5. Bootstrap only after showing the schema and receiving confirmation.
6. Write a workspace manifest containing the selected backend and protocol version.
