#!/usr/bin/env python3
"""One funny line, written out for the judge.

The One-Line Laugh (make.fun): the program writes a single sentence of
at most 200 characters to the output file the scorer reads.
"""

import os
import sys
from pathlib import Path

LINE = "My password is so secure even I can't get in, so I reset it every month like a subscription I never wanted."

MAX_CHARS = 200


def checked(line):
    text = line.strip()
    if not text:
        raise ValueError("the line is empty")
    if len(text) > MAX_CHARS:
        raise ValueError("the line is over 200 characters")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("the line must be a single sentence")
    return text


def out_path():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    folder = Path(base)
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def main():
    text = checked(LINE)
    target = out_path()
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)
    if target.read_text(encoding="utf-8") != text:
        raise ValueError("the written line does not match the checked line")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
