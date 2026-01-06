"""
Google Organic Search Scraper using SerpAPI
Scrapes Google search results using SerpAPI and finds domain position
"""

from typing import Optional
from urllib.parse import urlparse
from serpapi import GoogleSearch


class GoogleSearchScraper:
    def __init__(self, api_key: str, target_domain: str = "omorganickitchen.com", location: str = "Noida, Uttar Pradesh, India"):
        self.api_key = api_key
        self.target_domain = target_domain.lower()
        self.location = location
        self.max_pages = 5
        self.results_per_page = 10
    
    def search(self, keyword: str) -> Optional[int]:
        """
        Search Google using SerpAPI and find domain position in organic results
        
        Args:
            keyword: Search keyword
            
        Returns:
            Position (1-100) or None if not found
        """
        try:
            print(f"    → Searching: {keyword}")
            
            # Search through pages (up to 5 pages = top 50 results)
            print(f"    → Searching through {self.max_pages} pages (top {self.max_pages * self.results_per_page} results)...")
            
            for page_num in range(self.max_pages):
                start = page_num * self.results_per_page
                
                params = {
                    "api_key": self.api_key,
                    "engine": "google",
                    "google_domain": "google.co.in",
                    "q": keyword,
                    "gl": "in",
                    "hl": "en",
                    "location": self.location,
                    "start": str(start)
                }
                
                print(f"    → Checking page {page_num + 1} of {self.max_pages} (start={start})...")
                
                search = GoogleSearch(params)
                results = search.get_dict()
                
                # Check for errors
                if "error" in results:
                    print(f"    ✗ API Error: {results.get('error')}")
                    return None
                
                # Get organic results
                organic_results = results.get("organic_results", [])
                
                if not organic_results:
                    if page_num == 0:
                        print(f"    → No organic results found")
                    break
                
                print(f"    → Found {len(organic_results)} organic results on page {page_num + 1}")
                
                # Check each result for target domain
                base_position = page_num * self.results_per_page
                for idx, result in enumerate(organic_results, start=1):
                    try:
                        link = result.get("link", "")
                        if not link:
                            continue
                        
                        domain = urlparse(link).netloc.lower()
                        domain = domain.replace("www.", "")
                        
                        if self.target_domain in domain or domain in self.target_domain:
                            position = base_position + idx
                            print(f"    ✓ Found domain at position {position}: {link[:60]}")
                            return position
                    except Exception as e:
                        continue
            
            return None
            
        except Exception as e:
            print(f"    ✗ Error searching: {e}")
            import traceback
            traceback.print_exc()
            return None
