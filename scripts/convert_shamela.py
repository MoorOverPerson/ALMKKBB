#!/usr/bin/env python3
"""Utility to convert Shamela .bok files to plain text or JSON.

This script expects a directory containing `.bok` files from Al-Maktaba
Al-Shamela. It will extract the text and store it in a more convenient
format for the application.

Usage:
    python3 convert_shamela.py /path/to/bok/files output_dir
"""

import sys
from pathlib import Path

try:
    import shml2txt  # hypothetical library for conversion
except ImportError:
    print("This script requires the 'shml2txt' library. Install it via pip.")
    sys.exit(1)


def convert_directory(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    for bok_file in src.glob("*.bok"):
        out_file = dst / (bok_file.stem + ".txt")
        text = shml2txt.convert(bok_file)
        out_file.write_text(text, encoding="utf-8")
        print(f"Converted {bok_file} -> {out_file}")


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: convert_shamela.py <src_dir> <dst_dir>")
        return 1
    src = Path(argv[1])
    dst = Path(argv[2])
    convert_directory(src, dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
