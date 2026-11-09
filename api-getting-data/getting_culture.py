import time

import apikey
import requests
from bs4 import BeautifulSoup
from rich.console import Console

console = Console()

HEADERS = {
    "User-Agent": "is310-course/1.0 (https://khsieh314.github.io; katieh9@illinois.edu)"
}

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

wiki_params = {
    "action": "query",
    "list": "search",
    "srsearch": "Claude%20Monet",
    "format": "json"
}

response = requests.get(WIKI_API_URL, params=wiki_params, headers=HEADERS, timeout=15)
if response.status_code != 200:
    raise RuntimeError(f"WIKI API request failed: {response.status_code}")
data = response.json()



MET_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1.1/search"

met_params = {
    "action": "query",
    "list": "search",
    "srsearch": "Claude%20Monet",
    "format": "json"
}

response = requests.get(MET_API_URL, params=met_params, headers=HEADERS, timeout=15)
if response.status_code != 200:
    raise RuntimeError(f"MET API request failed: {response.status_code}")
data = response.json()

