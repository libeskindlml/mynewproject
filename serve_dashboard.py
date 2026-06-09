#!/usr/bin/env python3
"""Serve the sample dashboard on http://localhost:8080"""

import http.server
import os
import webbrowser
from pathlib import Path

PORT = 8080
DASHBOARD_DIR = Path(__file__).parent / "dashboard"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DASHBOARD_DIR), **kwargs)


def main():
    os.chdir(DASHBOARD_DIR)
    url = f"http://localhost:{PORT}"
    print(f"Serving dashboard at {url}")
    print("Press Ctrl+C to stop.")
    webbrowser.open(url)
    http.server.HTTPServer(("", PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
