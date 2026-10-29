import csv
import time
import requests

from bs4 import BeautifulSoup
from rich.console import console
from rich.table import Table


HEADERS = {"User-Agent": "is310-course-scraper/1.0 (student project; katieh9@illinois.edu)"}
response = requests.get("YOUR_URL_HERE", headers=HEADERS, timeout=10)

print(response.status_code)
print(response.text[:300])



