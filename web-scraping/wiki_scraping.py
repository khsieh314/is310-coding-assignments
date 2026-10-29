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

REQUEST_DELAY = 1.0
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

def scrape_pokemon (___, source_url):
    pokemon = []
    if ___, is None:
        return pokemon

    pokemon_section = ___.find(id="mw-content-text")
    if pokemon_section is None:
        return pokemon

    pokemon_items = pokemon_section.find_all("td")
    for pokemon in pokemon_items:
        link = pokemon.find("a", href=True)
        if link is None:
            continue

        pokemon.append({
            "Pokemon": link.get_text(" ", strip=True),
            "source_url": source_url,
            "Pokemon_url": f"{BASE_URL}{link['href']}",
        })

    return pokemon

def get_internal_links(content):
    if content is None:
        return []

    links = []
    for link in content.find_all("a", href=True):
        href = link["href"]
        if href.startswith("/wiki/") and "#" not in href:
            links.append(href)

    return links



console.print(scrape_pokemon(___, KANTO_REGION_URL))


