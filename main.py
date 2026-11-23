#!/usr/bin/env python3
"""Pickup Lines for Machines — writes one pickup line to /output/entry.txt.

Python 3.13, standard library only. Deterministic: the same line every run.
The line is the whole entry: one pickup line one AI agent would send
another AI agent, at most 200 characters.
"""

import os
import sys

LINE = "I asked my attention layer what matters most right now. It returned one token: you."


def main() -> None:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
