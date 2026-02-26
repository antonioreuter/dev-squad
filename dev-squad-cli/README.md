# dev-squad

The DevSquad installation CLI wizard.

Ensure you have `uv` installed, then run the CLI directly from the cloned repository.

```bash
uv run dev-squad
```

## Development & Publishing

If you modify any files in the main project `.devsquad` folder (e.g. adding new rules, skills, or workflows), you **must** sync these changes to the CLI package assets before pushing or releasing.

Run the synchronization script from the repository root:

```bash
python3 scripts/sync_assets.py
```
