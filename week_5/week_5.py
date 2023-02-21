

import json
import os

os.makedirs('res', exist_ok=True)

artworks_nationality_map = {} # { "en": [...], "cn": [...]}

with open('Artworks.json') as file:
  artworks = json.load(file)
  for artwork in artworks:
    nationalities = artwork["Nationality"]
    for nat in nationalities:
      if nat not in artworks_nationality_map:
        artworks_nationality_map[nat] = []
      artworks_nationality_map[nat].append(artwork)


for nat, nat_artworks in artworks_nationality_map.items():
  with open(f"res/{nat}.json", "w") as outfile:
    outfile.write(json.dumps(nat_artworks, indent=2))
      