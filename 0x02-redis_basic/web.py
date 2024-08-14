#!/usr/bin/env python3
"""
Module for caching web page content using Redis.
"""
import redis
import requests
from typing import Callable
from functools import wraps

class WebCache:
    """Class to handle web page caching with Redis."""
    
    def __init__(self):
        self._redis = redis.Redis()
    
    def get_page(self, url: str) -> str:
        """Fetches the content of a URL and caches it with an expiration."""
        # Check if the content is already cached
        cached_content = self._redis.get(f"content:{url}")
        
        if cached_content:
            return cached_content.decode('utf-8')
        
        # If not cached, fetch the content
        response = requests.get(url)
        html_content = response.text
        
        # Store the content in Redis with an expiration of 10 seconds
        self._redis.setex(f"content:{url}", 10, html_content)
        
        # Increment the access count for the URL
        self._redis.incr(f"count:{url}")
        
        return html_content

# Decorator implementation
def cache_page(func: Callable) -> Callable:
    """Decorator to cache the result of a web page fetch."""
    
    @wraps(func)
    def wrapper(self, url: str) -> str:
        return self.get_page(url)
    
    return wrapper

# Applying the decorator
@WebCache.cache_page
def get_page(url: str) -> str:
    """Function to fetch a web page's content."""
    return WebCache().get_page(url)

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    print(get_page(url))

