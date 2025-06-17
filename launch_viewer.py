#!/usr/bin/env python3
"""Open the IBADAH whitepaper viewer.

This script opens ``viewer/index.html`` in the default web browser.
Use it on Windows to quickly launch the interactive whitepaper.
"""
from __future__ import annotations
import webbrowser
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    viewer = root / "viewer" / "index.html"
    webbrowser.open(viewer.as_uri())


if __name__ == "__main__":
    main()

