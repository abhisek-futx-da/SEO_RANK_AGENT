#!/usr/bin/env python3
"""
Main script for Google ranking scraper
Uses SerpAPI to get Google search results
Updates Excel file in-place preserving format
"""

import time
import random
from scraper.google_search import GoogleSearchScraper
from scraper.google_places import GooglePlacesScraper
from utils.excel import ExcelHandler


def main():
    # Configuration
    EXCEL_FILE = "./keywords.xlsx"  # Update this file in-place
    SHEET_NAME = "Keywords"
    HEADER_ROW = 1
    TARGET_DOMAIN = "omorganickitchen.com"
    LOCATION = "Noida, Uttar Pradesh, India"
    SERPAPI_API_KEY = "043a5aabdc2f17335b1e4d707302d3b13043a692629d701c0717a5eed2cee782"
    
    print("="*80)
    print("Google Ranking Scraper (SerpAPI)")
    print(f"Target Domain: {TARGET_DOMAIN}")
    print(f"Location: {LOCATION}")
    print(f"Excel File: {EXCEL_FILE}")
    print("="*80)
    print()
    
    # Initialize handlers
    excel_handler = ExcelHandler(EXCEL_FILE)
    search_scraper = GoogleSearchScraper(SERPAPI_API_KEY, TARGET_DOMAIN, LOCATION)
    places_scraper = GooglePlacesScraper(SERPAPI_API_KEY, TARGET_DOMAIN, LOCATION)
    
    # Read keywords
    try:
        df = excel_handler.read_keywords(SHEET_NAME, HEADER_ROW)
    except Exception as e:
        print(f"✗ Error reading Excel file: {e}")
        return 1
    
    # Validate columns
    if excel_handler.keyword_column not in df.columns:
        print(f"✗ Column '{excel_handler.keyword_column}' not found")
        print(f"Available columns: {list(df.columns)}")
        return 1
    
    # Filter valid keywords
    df_clean = df[df[excel_handler.keyword_column].notna()].copy()
    total_keywords = len(df_clean)
    
    print(f"✓ Found {total_keywords} keywords to process")
    print(f"→ Updating {EXCEL_FILE} in-place (format preserved)")
    print()
    
    try:
        # Process each keyword
        for idx, (row_index, row) in enumerate(df_clean.iterrows(), 1):
            keyword = str(row[excel_handler.keyword_column]).strip()
            
            if not keyword:
                continue
            
            print(f"[{idx}/{total_keywords}] Processing: {keyword}")
            print("-" * 80)
            
            # Search Google Places
            print("  Google Places:")
            places_rank = places_scraper.search(keyword)
            print(f"  → Result: {places_rank if places_rank else 'Not found'}")
            
            # Small delay between searches
            time.sleep(random.uniform(1, 2))
            
            # Search Google Organic
            print("  Google Links:")
            links_rank = search_scraper.search(keyword)
            print(f"  → Result: {links_rank if links_rank else 'Not found'}")
            
            # Update Excel file in-place (preserves format)
            print("  → Updating Excel file...")
            excel_handler.update_rankings(
                row_index=row_index,
                places_rank=places_rank,
                links_rank=links_rank,
                sheet_name=SHEET_NAME,
                header_row=HEADER_ROW
            )
            print(f"  ✓ Saved to {EXCEL_FILE}")
            
            print()
            
            # Rate limiting delay (SerpAPI has rate limits)
            if idx < total_keywords:
                delay = random.uniform(2, 3)
                print(f"  → Waiting {delay:.1f}s before next keyword...")
                time.sleep(delay)
                print()
    
    except KeyboardInterrupt:
        print("\n\n⚠ Process interrupted by user")
        print(f"✓ Progress saved to {EXCEL_FILE}")
        return 1
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    print("="*80)
    print("✓ All keywords processed!")
    print(f"✓ Results saved to: {EXCEL_FILE}")
    print("="*80)
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
