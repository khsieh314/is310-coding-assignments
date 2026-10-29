import csv
import time
import requests
import rich
from rich.console import Console
from rich.table import Table

HEADERS = {"User-Agent": "is310-course-scraper/1.0 (student project; katieh9@illinois.edu)"}
response = requests.get("https://bulbapedia.bulbagarden.net", headers=HEADERS, timeout=10)
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')


print(response.status_code)
print(response.text[:300])

BASE_URL = "https://bulbapedia.bulbagarden.net"
KANTO_REGION_URL = f"{BASE_URL}/wiki/Kanto" 
UNOVA_REGION_URL = f"{BASE_URL}/wiki/Unova" 

REQUEST_DELAY = 1.0
RESULTS_OUTPUT = "pokemon_region_numbers.csv"

