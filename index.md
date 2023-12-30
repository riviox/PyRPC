<style>
    body {
      background-color: #121212;
      color: #c7c7c7;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.6;
    }

    h1, h2, h3, h4, h5, h6 {
      color: #bd93f9;
    }

    a {
      color: #8be9fd;
    }

    a:hover {
      color: #bd93f9;
    }

    hr {
      border: 0;
      border-bottom: 1px solid #444;
    }

    pre, code {
      background-color: #282a36;
      color: #f8f8f2;
      border: 1px solid #444;
      border-radius: 4px;
    }

    pre {
      padding: 8px;
      overflow: auto;
    }

    blockquote {
      background-color: #444;
      border-left: 4px solid #bd93f9;
      padding: 0.5em;
      margin: 0;
    }
  </style>
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