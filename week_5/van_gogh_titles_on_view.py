import requests
import json

url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
res = requests.get(url, params={ "isOnView": "true", "hasImages": "true", "q": "van gogh" })
res_json = res.json()
objectIDs = res_json["objectIDs"]

titles = []
for objectID in objectIDs:
    detail_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectID}"
    res = requests.get(detail_url)
    res_json = res.json()
    titles.append(res_json["title"])
    
print(json.dumps(titles, indent=2))
