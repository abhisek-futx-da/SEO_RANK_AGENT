# Setup Instructions

## Virtual Environment Setup

This project uses `uv` for fast Python package management and a virtual environment.

### Initial Setup (Already Done)

```bash
# Create virtual environment
uv venv

# Install all packages
uv pip install -r requirements.txt
```

### Daily Usage

**Activate the virtual environment:**
```bash
source .venv/bin/activate
```

**Deactivate when done:**
```bash
deactivate
```

### Running Scripts

**Option 1: Activate venv first (recommended)**
```bash
source .venv/bin/activate
python keyword_ranker.py
python seo_analyzer.py
python run_seo_analysis.py
```

**Option 2: Use uv run (no activation needed)**
```bash
uv run python keyword_ranker.py
uv run python seo_analyzer.py
uv run python run_seo_analysis.py
```

### Adding New Packages

```bash
# Activate venv first
source .venv/bin/activate

# Install new package
uv pip install package-name

# Or add to requirements.txt and install all
uv pip install -r requirements.txt
```

### Installed Packages

- pandas>=2.0.0 - Data manipulation
- openpyxl>=3.1.0 - Excel file handling
- selenium>=4.15.0 - Web automation
- webdriver-manager>=4.0.0 - ChromeDriver management
- requests>=2.31.0 - HTTP requests
- beautifulsoup4>=4.12.0 - HTML parsing
- lxml>=4.9.0 - XML/HTML parser
- xlrd>=2.0.1 - Excel file reading (legacy .xls)

All packages are installed in `.venv/` directory.

