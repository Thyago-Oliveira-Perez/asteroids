# Asteroids (Pygame)

Small Asteroids-style game built with Python + Pygame.

## Requirements

- Python $\ge$ 3.12 (see `.python-version`)
- Recommended: [`uv`](https://github.com/astral-sh/uv) for dependency management (this repo includes `uv.lock`)

## Setup (recommended: `uv`)

From the project root:

```bash
# install uv (if needed)
python3 -m pip install --user uv

# create/update the local virtual environment and install deps
uv sync
```

## Run

You can run without manually activating the venv:

```bash
uv run main.py
```

## Controls

- `W`: thrust forward
- `S`: thrust backward
- `A`: rotate left
- `D`: rotate right
- `Space`: shoot

If you prefer to activate the environment (optional):

```bash
source .venv/bin/activate
python main.py
```

## Troubleshooting

- If `source .venv/bin/activate` fails, run `uv sync` first to create `.venv/`.
