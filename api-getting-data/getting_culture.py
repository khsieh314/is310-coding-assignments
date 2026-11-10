import time
import json
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
    "srsearch": "Claude Monet",
    "format": "json"
}

wiki_response = requests.get(WIKI_API_URL, params=wiki_params, headers=HEADERS, timeout=15)
if wiki_response.status_code != 200:
    raise RuntimeError(f"WIKI API request failed: {wiki_response.status_code}")
wiki_data = wiki_response.json()
print(json.dumps(wiki_data))



MET_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1.1/search"
met_params = {
    "q": "Claude Monet",
    "title": "true",
    "meduim": "paintings",
    "hasImages": "true"
}

met_response = requests.get(MET_API_URL, params=met_params, headers=HEADERS, timeout=15)
if met_response.status_code != 200:
    raise RuntimeError(f"MET API request failed: {met_response.status_code}")
met_data = met_response.json()
print(json.dumps(met_data))

