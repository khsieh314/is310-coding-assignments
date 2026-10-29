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
KANTO_REGION_URL = f"{BASE_URL}/wiki/List_of_Pokémon_by_Kanto_Pokédex_number" 
UNOVA_REGION_URL = f"{BASE_URL}/wiki/List_of_Pokémon_by_Unova_Pokédex_number_in_Pokémon_Black_and_White" 

REQUEST_DELAY = 5.0
RESULTS_OUTPUT = "pokemon_region_numbers.csv"

console = Console()


def fetch_soup(url):
    if not url:
        console.print("[yellow]No URL was found for this page.[/yellow]")
        return None

    response = requests.get(url, headers=HEADERS, timeout=30)
    time.sleep(REQUEST_DELAY)

    if response.status_code != 200:
        console.print(f"[red]Could not download {url}: HTTP {response.status_code}[/red]")
        return None

    return BeautifulSoup(response.text, "html.parser")


#what I want this to do is to scrape the pokemon from the table as well as the corresponding
#type I want to store both the name and the type together as well as count up the totla of each type

def scrape_name():
    pokemon = []
    table = soup.find('table', class_=__)

    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            name = columns[3].text.strip()
            type = columns[4].text.strip()  
"""
    pokemon.append({
        "pokemon":
        "pokemon_url":
        "type":
                    })  
"""

def scrape_pokemon( __, source_url):
    pokemon = []
    if __ is None:
        return pokemon

    table = __.find("table", class_:__)
    if table is None:
        return pokemon

    pokemon_name = table.find_all("tr")
    for item in pokemon_name:
        link = item.find("a", href=True)
        if link is None:
            continue

        pokemon.append({
            "pokemon_name": link.get_text(" ", strip=True),
#            "character_type": character_type,
            "source_url": source_url,
            "pokemon_url": f"{BASE_URL}{link['href']}",
        })

    return pokemon
