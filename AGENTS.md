# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This is a **Microsoft 365 Agent Toolkit Assistant** — a three-tier developer toolkit:
1. **Python CLI** (`python3 assistant.py`): Interactive assistant with 14 operating modes for creating M365 agents, bots, cards, workflows, etc.
2. **React Web UI** (`web-ui/`): Visual Workflow Designer, Agent Builder, Template Gallery on port 3000
3. **FastAPI Marketplace API** (`api/`): REST backend for templates on port 8000

### Running Services

- **CLI assistant**: `python3 assistant.py` (interactive) or `python3 assistant.py --mode <mode>` (see `--help`)
- **API server**: `cd api && python3 main.py` (runs on port 8000; Swagger docs at `/docs`)
- **Web UI dev server**: `cd web-ui && npm run dev` (runs on port 3000; proxies `/api` to port 8000)

Start the API server **before** the Web UI so the proxy to port 8000 works correctly.

### Dependencies

- Python deps are split across two files: root `requirements.txt` and `api/requirements.txt`.
- The root `requirements.txt` has a bogus `python>=3.8` line and `adaptivecards>=1.0.0` (only 0.4.x exists on PyPI). The update script handles both.
- Web UI uses npm (`web-ui/package.json`); no lockfile is committed.

### Lint / Test / Build

- **ESLint**: No `.eslintrc` config exists. `npm run lint` will fail until one is created.
- **pytest**: No test files exist. The `TestFramework` class in `src/cli_tools/test_framework.py` is not a pytest test (it has `__init__`).
- **vitest**: No test spec files exist in `web-ui/`.
- **Web UI build**: `cd web-ui && npm run build` (outputs to `web-ui/dist/`).

### Gotchas

- `python` is not on PATH; always use `python3`.
- pip installs go to `~/.local` (user site-packages). Ensure `~/.local/bin` is on PATH for `uvicorn` etc.
- The CLI's interactive mode uses `input()` prompts; pipe commands via stdin for non-interactive use (e.g., `echo "exit" | python3 assistant.py`).
