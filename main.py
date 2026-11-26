#!/usr/bin/env python3
"""Vending Machine Pickup Line Contest entry.

Writes one pickup line, spoken by a vending machine to a passing human,
to $MAKEFUN_OUTPUT_DIR/entry.txt. Python 3.13 standard library only.
"""

import os
import pathlib

LINE = "I've got forty snacks behind this glass, but you're the one I keep getting stuck on."


def main() -> None:
    # The gate allows 1-200 characters; keep the line inside it.
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
