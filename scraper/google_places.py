"""
Google Places (Local Pack) Scraper using SerpAPI
Scrapes Google Maps/Local results and finds domain position
"""

from typing import Optional
from urllib.parse import urlparse
from serpapi import GoogleSearch


class GooglePlacesScraper:
    def __init__(self, api_key: str, target_domain: str = "omorganickitchen.com", location: str = "Noida, Uttar Pradesh, India"):
        self.api_key = api_key
        self.target_domain = target_domain.lower()
        self.location = location
    
    def search(self, keyword: str) -> Optional[int]:
        """
        Search Google Maps using SerpAPI and find domain position in Local results
        
        Args:
            keyword: Search keyword
            
        Returns:
            Position (1, 2, 3...) or None if not found
        """
        try:
            print(f"    → Searching Places: {keyword}")
            
            params = {
                "api_key": self.api_key,
                "engine": "google_maps",
                "type": "search",
                "google_domain": "google.co.in",
                "q": keyword,
                "hl": "en",
                "gl": "in",
                "location": self.location,
                "z": "20"
            }
            
            search = GoogleSearch(params)
            results = search.get_dict()
            
            # Check for errors
            if "error" in results:
                print(f"    ✗ API Error: {results.get('error')}")
                return None
            
            # Get local results from Google Maps
            local_results = results.get("local_results", [])
            
            if not local_results:
                print(f"    → No Local results found")
                return None
            
            print(f"    → Found {len(local_results)} Places results")
            
            # Check each result for target domain
            for idx, result in enumerate(local_results, start=1):
                try:
                    # Check website URL
                    website = result.get("website", "")
                    if website:
                        domain = urlparse(website).netloc.lower()
                        domain = domain.replace("www.", "")
                        
                        if self.target_domain in domain or domain in self.target_domain:
                            print(f"    ✓ Found domain in Places at position {idx}: {website[:60]}")
                            return idx
                    
                    # Check title for domain mentions
                    title = result.get("title", "").lower()
                    if 'omorganic' in title or 'om organic' in title or 'omorganickitchen' in title:
                        print(f"    ✓ Found domain in Places title at position {idx}")
                        return idx
                    
                    # Also check link field if available
                    link = result.get("link", "")
                    if link:
                        domain = urlparse(link).netloc.lower()
                        domain = domain.replace("www.", "")
                        if self.target_domain in domain or domain in self.target_domain:
                            print(f"    ✓ Found domain in Places link at position {idx}")
                            return idx
                    
                except Exception as e:
                    continue
            
            print(f"    → Domain not found in Local results")
            return None
            
        except Exception as e:
            print(f"    ✗ Error searching Places: {e}")
            import traceback
            traceback.print_exc()
            return None
