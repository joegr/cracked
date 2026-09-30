"""Execute every chapter notebook top to bottom; exit non-zero if any cell fails.

Usage:  uv run python tools/run_all.py [chapter-substring ...]
"""
import pathlib
import sys

import nbformat
from nbclient import NotebookClient

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main(filters: list[str]) -> int:
    failures = 0
    for path in sorted(ROOT.glob("[0-9][0-9]_*/*.ipynb")):
        if filters and not any(f in path.stem for f in filters):
            continue
        nb = nbformat.read(path, as_version=4)
        try:
            NotebookClient(nb, timeout=180, kernel_name="python3",
                           resources={"metadata": {"path": str(path.parent)}}).execute()
            print(f"PASS  {path.relative_to(ROOT)}")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"FAIL  {path.relative_to(ROOT)}\n{str(exc)[-800:]}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
