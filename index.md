# PyRPC
![GitHub](https://img.shields.io/github/license/riviox/PyRPC)
![GitHub last commit](https://img.shields.io/github/last-commit/riviox/PyRPC)

# Join [Riviox's Community](https://discord.gg/FVAxsMbnk7)

This is a simple Discord Rich Presence application written in Python. It uses the pypresence library to update your Discord status with information retrieved from a specified user ID.

## Features

- Display Discord user information in your Rich Presence status
- Automatically updates every 15 seconds
- Minimal console output for a clean experience

# Config Builder
## Use config builder to make `config.json`!

## Prerequisites

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - requests
  - colorama
  - pypresence

## How to build exe
### 1. Easy way
- Run `build_PyRPC.bat`
### 2. Advanced way
```bash
pip install pyinstaller
pyinstaller --onefile PyRPC.py
```
PyRPC.exe should be in `/dist/PyRPC.exe`

Made with ~~love~~ code by riviox