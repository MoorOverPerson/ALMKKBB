# IBADAH Project Repository

This repository hosts the whitepaper for the "IBADAH" cryptocurrency project and
serves as a starting point for future development.

The project aims to link worship activities with blockchain technology.

## Directory Structure

- `الورقة البيضاء` – Arabic whitepaper describing the concept.
- `shamela/` – Placeholder for Al-Maktaba Al-Shamela library files and
  instructions for integration.
- `scripts/` – Utility scripts for handling data.

## Adding the Shamela Library

The actual book files are not included in this repository. See
[`shamela/README.md`](shamela/README.md) for steps on how to obtain and
prepare the library for use in your application.

## Interactive Viewer

An HTML-based viewer is available in [`viewer/`](viewer) for reading the Arabic
whitepaper with a simple search feature. Open `viewer/index.html` in your web
browser to try it out.

### Windows launcher

For convenience, a small Python script `launch_viewer.py` opens the viewer
directly in your default browser. Run it with Python 3:

```bash
python launch_viewer.py
```

To create a standalone executable on Windows, install
[PyInstaller](https://pyinstaller.org/) and execute:

```bash
pyinstaller --onefile launch_viewer.py
```

This will generate `dist/launch_viewer.exe` which you can double-click to start
the viewer without needing Python installed.
