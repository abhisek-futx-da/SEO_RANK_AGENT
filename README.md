# Google Ranking Scraper

A Python tool that uses SerpAPI to get Google search results and find keyword rankings for a target domain. Fills ranking data directly into an Excel sheet.

## Features

- ✅ **SerpAPI Integration** - Uses SerpAPI for reliable, fast Google search results
- ✅ **Google Places Ranking** - Finds position in Local Pack/Maps results
- ✅ **Google Organic Ranking** - Finds position in organic search results (up to top 50)
- ✅ **Excel Integration** - Reads keywords and writes results directly to Excel (preserves format)
- ✅ **Rate Limiting** - Built-in delays to respect API limits
- ✅ **Progress Saving** - Saves results after each keyword

## Installation

### 1. Setup Virtual Environment

```bash
# Create virtual environment (already done)
uv venv

# Activate virtual environment
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install Python packages
uv pip install -r requirements.txt
```

## Usage

### 1. Prepare Your Excel File

Your Excel file (`keywords.xlsx`) should have:
- **Sheet name:** "Keywords"
- **Column:** "Local Keyword Ideas" (contains keywords)
- **Column:** "Targeted Page" (optional, for reference)

The script will update:
- **"Google Places"** column (Local Pack rankings)
- **"Google Links"** column (Organic search rankings)

### 2. Run the Scraper

```bash
python main.py
```

### 3. Check Results

Results are saved directly to `keywords.xlsx` with rankings filled in.

## Configuration

Edit `main.py` to customize:

```python
EXCEL_FILE = "./keywords.xlsx"        # Input Excel file
SHEET_NAME = "Keywords"                # Sheet name
TARGET_DOMAIN = "omorganickitchen.com" # Domain to find
LOCATION = "Noida, Uttar Pradesh, India"  # Search location
SERPAPI_API_KEY = "your-api-key"      # Your SerpAPI key
```

## How It Works

### Google Places Ranking
1. Uses SerpAPI to search keyword with location
2. Gets `local_results` from API response
3. Checks each result for target domain
4. Returns position (1, 2, 3...) or None if not found

### Google Organic Ranking
1. Uses SerpAPI to search keyword with location
2. Gets `organic_results` from API response
3. Checks up to 5 pages (top 50 results)
4. Returns absolute position (1-50) or None if not found

## API Key

The script uses SerpAPI for Google search results. Your API key is configured in `main.py`.

**Note:** SerpAPI is a paid service. Check your API usage and limits at [serpapi.com](https://serpapi.com).

## Output

The Excel file is updated in-place. Each row gets:
- **Google Places** score (position number or empty if not found)
- **Google Links** score (position number or empty if not found)

## Requirements

- Python 3.7+
- SerpAPI account and API key
- All dependencies are installed in the virtual environment

## Notes

- Progress is saved after each keyword
- The script includes delays to respect API rate limits
- Results are written directly to your Excel file (format preserved)
- SerpAPI is faster and more reliable than browser scraping
- No browser installation required

## License

This tool is for legitimate SEO analysis purposes only. Use responsibly and in compliance with SerpAPI's Terms of Service.
