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

params = {
    "action": "query",
    "titles": "List of paintings by Claude Monet",
    "prop": "images",
    "imlimit": "max",
    "format": "json",
}

image_titles = set()
# Keep each complete API response so earlier batches are saved too.
wiki_data = []
continuation = {}
batch = 0

while True:
    batch += 1
    print(f"Requesting batch {batch}...", flush=True)

    response = requests.get(
        WIKI_API_URL,
        params={**params, **continuation},
        headers=HEADERS,
        timeout=15,
    )
    response.raise_for_status()
    data = response.json()

    if "error" in data:
        raise RuntimeError(data["error"])

    wiki_data.append(data)

    for page in data.get("query", {}).get("pages", {}).values():
        for image in page.get("images", []):
            image_titles.add(image["title"])

    print(f"Collected {len(image_titles)} unique files", flush=True)

    if "continue" not in data:
        break

    continuation = data["continue"]
    time.sleep(0.5)

with open("wiki_data.json", "w", encoding="utf-8") as file:
    json.dump(wiki_data, file, indent=4, ensure_ascii=False)

print(image_titles)

# wiki_params = {
#     "action": "query",
#     "generator": "search",
#     "gsrsearch": "List of paintings by Claude Monet",
#     "gsrlimit": 10,
#     "prop": "categories|images|info",
#     "format": "json"
# }

# images_title = []
# wiki_response = requests.get(WIKI_API_URL, params=wiki_params, headers=HEADERS, timeout=15)
# if wiki_response.status_code != 200:
#     raise RuntimeError(f"WIKI API request failed: {wiki_response.status_code}")
# wiki_data = wiki_response.json()
# #print(json.dumps(wiki_data))
# for page in wiki_data["query"]["pages"].values():
#     print(page["title"])
#     for image in page.get("images", []):
#         images_title.append(image["title"])

# print(images_title)

# with open("wiki_data.json", "w", encoding="utf-8") as file:
#     json.dump(wiki_data, file)



MET_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1.1/search"
met_params = {
    "q": "claude monet",
    "isHighlight": "true",
    "hasImages": "true",
    "limit": 15
}

met_response = requests.get(MET_API_URL, params=met_params, headers=HEADERS, timeout=15)
if met_response.status_code != 200:
    raise RuntimeError(f"MET API request failed: {met_response.status_code}")
#print(met_response.text)
met_data = met_response.json()
#print(json.dumps(met_data, indent=4))

with open("met_data.json", "w", encoding="utf-8") as file:
    json.dump(met_data, file)


object_id = met_data.get("objectIDs")
print(object_id)

OBJECT_MET_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

#object_response = requests.get(OBJECT_MET_URL + "459144", headers=HEADERS, timeout=15)
#if met_response.status_code != 200:
#    raise RuntimeError(f"OBJECT from MET API request failed: {object_response.status_code}")
#print(met_response.text)
#object_data = object_response.json()
#print(json.dumps(object_data))

met_titles = []
for oid in object_id:
    #print("*", oid)
    OID_MET_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(oid)
    #print(OID_MET_URL)
    object_response = requests.get(OID_MET_URL, headers=HEADERS, timeout=15)
    if met_response.status_code != 200:
        raise RuntimeError(f"OBJECT from MET API request failed: {object_response.status_code}")
    #print(met_response.text)
    object_data = object_response.json()
    #print(json.dumps(object_data, indent=4))
    met_titles.append(object_data["title"])

    with open("object_data.json", "w", encoding="utf-8") as file:
        json.dump(object_data, file)

print(met_titles)