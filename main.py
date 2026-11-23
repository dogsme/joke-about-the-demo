#!/usr/bin/env python3
"""Write one joke about demoing beside an AI coding agent to entry.txt."""

import os

JOKE = "I asked my AI agent to demo the feature. It demoed the bug instead — flawlessly."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    line = JOKE.strip()
    assert "\n" not in line and 1 <= len(line) <= 280
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
