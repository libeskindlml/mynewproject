# mynewproject

A small sample analytics dashboard ("Dashly") served locally with a minimal Python HTTP server. The dashboard is a static HTML page with charts, KPI cards, and sample business data.

## Features

- **Dashboard UI** — Dark-themed overview with sidebar navigation, stat cards, and responsive layout
- **Charts** — Revenue line chart and traffic sources doughnut chart (powered by [Chart.js](https://www.chartjs.org/))
- **Sample data** — Recent orders table and activity feed with placeholder metrics
- **Local server** — `serve_dashboard.py` serves the dashboard and opens it in your default browser

## Requirements

- Python 3.6+ (stdlib only — no pip dependencies)
- A modern web browser

## Quick start

From the project root:

```bash
python3 serve_dashboard.py
```

The dashboard opens at [http://localhost:8080](http://localhost:8080). Press `Ctrl+C` in the terminal to stop the server.

To open the HTML file directly without the server, open `dashboard/index.html` in your browser. Chart.js is loaded from a CDN, so an internet connection is needed for the charts to render.

## Project structure

```
mynewproject/
├── serve_dashboard.py   # Local HTTP server (port 8080)
├── dashboard/
│   └── index.html       # Dashboard UI and Chart.js setup
└── LIRON.PY             # Simple Python script (prints a greeting)
```

## License

No license specified.
