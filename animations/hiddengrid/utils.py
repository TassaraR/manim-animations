import tomllib
from pathlib import Path
from typing import Any


def load_config(curr_path: str, filename: str) -> dict[str, Any]:

    currdir = Path(curr_path).parent
    filename = Path(filename)
    abspath = currdir / filename
    with open(abspath, "rb") as f:
        cfg = tomllib.load(f)
    return cfg
