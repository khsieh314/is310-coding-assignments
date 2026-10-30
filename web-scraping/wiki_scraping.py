import csv
import time
import requests
import rich
from rich.console import Console
from rich.table import Table
from collections import Counter

HEADERS = {"User-Agent": "is310-course-scraper/1.0 (student project; katieh9@illinois.edu)"}
response = requests.get("https://bulbapedia.bulbagarden.net", headers=HEADERS, timeout=10)
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

#print(response.status_code)
#print(response.text[:300])

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

def get_pokemon_list(url):
    soup = fetch_soup(url)
    #print(soup.prettify())
    tables = soup.find_all("table")
    #print(tables)
    pokemon_table_list = []
    pokemon_type_list = []

    for table in tables:
        element = table.find_previous_sibling()
        if element and element.name in {"h4", "h3"}:
            element_text = element.get_text()
            table_items = []
            #print(element)
            #print(table)
            for row in table.find_all("tr"):
                cells = row.find_all("td")
                #print(cells)
                if len(cells) >= 5: 
                    pokemon_name = cells[2].get_text()
                    #pokemon_name_list.append(pokemon_name)
                    pokemon_type = cells[3].get_text()
                    pokemon_type_list.append(pokemon_type.strip())
                    pokemon_row = {"pokemon_name": pokemon_name, "pokemon_type": pokemon_type}
                    table_items.append(pokemon_row)
                    #print(pokemon_name)
                    #print(pokemon_type)
            if len(table_items) > 0:
                pokemon_table_data = {"header": element_text, "table_items": table_items}
                pokemon_table_list.append(pokemon_table_data)
    return pokemon_table_list, pokemon_type_list

kanto_pokemon, kanto_pokemon_types = get_pokemon_list(KANTO_REGION_URL)
unova_pokemon, unova_pokemon_types = get_pokemon_list(UNOVA_REGION_URL)

def print_pokemon_types(kanto_pokemon_types, unova_pokemon_types):
    kanto_type_count = Counter(kanto_pokemon_types)
    unova_type_count = Counter(unova_pokemon_types)
    type_totals = kanto_type_count + unova_type_count

    with open("pokemon_counts.csv", "w", newline= "") as newfile:
        writer = csv.writer(newfile)
        writer.writerow(["Type", "Kanto Region", "Unova Region"])

        table = Table(title="Pokemon Type Comparison")
        table.add_column("Type")
        table.add_column("Kanto Region")
        table.add_column("Unova Region")

        # 1. Look at everything in List A
        for p_type in kanto_type_count:
            count_a = kanto_type_count[p_type]
            count_b = unova_type_count.get(p_type, 0)  # Use 0 if it's not in List B
            table.add_row(p_type, str(count_a), str(count_b))
            writer.writerow([p_type, str(count_a), str(count_b)])

        # 2. Look at everything in List B (but SKIP things we already counted in List A)
        for p_type in unova_type_count:
            if p_type not in kanto_type_count:
                count_a = 0                     # Since it wasn't in List A
                count_b = unova_type_count[p_type]
                table.add_row(p_type, str(count_a), str(count_b))
                writer.writerow([p_type, str(count_a), str(count_b)])
  
        console.print(table)

print_pokemon_types(kanto_pokemon_types, unova_pokemon_types)

def print_pokemon_table(pokemon_list):
    for ptable in pokemon_list:
        table = Table(title = ptable["header"] , style="dark_green")
        table.add_column("Pokemon Name", justify="center")
        table.add_column("Pokemon Type", justify="center")
        for p in ptable["table_items"]:
            table.add_row((p["pokemon_name"]), (p["pokemon_type"]))
        console.print(table)



#print_pokemon_table(kanto_pokemon)
#print_pokemon_table(unova_pokemon)

#print(pokemon_name_list)
#print(pokemon_type_list)
#pokemon_name_dict = {"Name": pokemon_name_list}
#print(pokemon_name_dict)

#collected_data = dict(zip(pokemon_name_list, pokemon_type_list))
#print(collected_data)
#print(collected_data.items())
#cleaned_collection = collected_data.items()

#pokemon_table(collected_data)

#type_count = Counter(pokemon_type_list)
#print(type_count)

#what I want this to do is to scrape the pokemon from the table as well as the corresponding
#type I want to store both the name and the type together as well as count up the total of each type

# def scrape_name():
#     pokemon = []
#     table = soup.find('table', class_=__)

#     for row in table.tbody.find_all('tr'):
#         columns = row.find_all('td')
#         if columns:
#             name = columns[3].text.strip()
#             type = columns[4].text.strip()  
# """
#     pokemon.append({
#         "pokemon": name
#         "pokemon_url":
#         "type": type
#                     })  
# """

# def scrape_pokemon( __, source_url):
#     pokemon = []
#     if __ is None:
#         return pokemon

#     table = __.find("table", class_:__)
#     if table is None:
#         return pokemon

#     pokemon_name = table.find_all("tr")
#     for item in pokemon_name:
#         link = item.find("a", href=True)
#         if link is None:
#             continue

#         pokemon.append({
#             "pokemon_name": link.get_text(" ", strip=True),
# #            "character_type": character_type,
#             "source_url": source_url,
#             "pokemon_url": f"{BASE_URL}{link['href']}",
#         })

#     return pokemon



