import requests
import json

url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
res = requests.get(url, params={ "isOnView": True, "hasImages": True, "q": "van gogh" })
res_json = res.json()
# print(res_json)

# res_json = json.loads(res.text)
formatted_res = json.dumps(res_json, indent=2)
print(formatted_res)
