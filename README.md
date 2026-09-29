## 🚀 Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/IIliyaII/Simple-personal-web-page.git
cd Simple-personal-web-page
```

### 2. Install dependencies

This project uses **uv** for Python package and environment management.

```bash
uv sync
```

### 3. Run the application

```bash
uv run python main.py
```

Then open:

```text
http://127.0.0.1:5000
```

## 📦 Dependency Management

The project uses:

* `pyproject.toml` — project metadata and dependency configuration
* `uv.lock` — locked dependency versions for reproducible environments
* `uv` — Python package and project management

The lock file is committed to the repository so that the project can be recreated with the same dependency versions.

## 📁 Project Structure

```text
Simple-personal-web-page/
│
├── static/
│   └── ...
│
├── templates/
│   └── home.html
│
├── icon.png
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```
