# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This is the **Microsoft 365 Agent Toolkit Assistant** — an AI-powered developer assistant with three runnable components:

| Component | Entry Point | Port | How to Run |
|---|---|---|---|
| Python CLI Assistant | `assistant.py` | N/A (CLI) | `python3 assistant.py` (interactive; pipe commands for non-interactive) |
| FastAPI Marketplace API | `api/main.py` | 8000 | `python3 api/main.py` |
| React Web UI (Vite) | `web-ui/` | 3000 | `cd web-ui && npm run dev` |

The Web UI proxies `/api` requests to the FastAPI backend on port 8000 (see `web-ui/vite.config.js`). Start the API before the Web UI if you need the Template Gallery to function.

### Gotchas

- **`requirements.txt` has `python>=3.8`**: This is not a valid pip package. When installing, filter it out: `pip install $(grep -v '^python>=' requirements.txt | grep -v '^adaptivecards>=' | grep -v '^#' | grep -v '^$') adaptivecards`
- **`adaptivecards>=1.0.0`** doesn't exist on PyPI. The latest version is `0.4.1`. Install as `adaptivecards` (no version pin).
- **`uvicorn` installs to `~/.local/bin`** which may not be on PATH. Ensure `export PATH="$HOME/.local/bin:$PATH"` is set or use `python3 -m uvicorn`.
- **No ESLint config** exists in `web-ui/`. The `npm run lint` script will fail. Lint is not configured for this repo.
- **No test files** exist (neither Python pytest nor JS vitest). `pytest` collects zero tests; `vitest` finds no test files.
- **CLI `assistant.py` is interactive** (uses `input()`). For non-interactive usage, pipe commands: `echo -e "list templates\nexit" | python3 assistant.py`
- **The API uses in-memory mock data** — no database or external services are required.

### Standard Commands

See `README.md` for full commands. Key dev commands:
- **Install deps**: `pip install -r requirements.txt` (root) + `pip install -r api/requirements.txt` (API) + `cd web-ui && npm install`
- **Build Web UI**: `cd web-ui && npm run build`
- **API docs**: `http://localhost:8000/docs` (Swagger UI)
