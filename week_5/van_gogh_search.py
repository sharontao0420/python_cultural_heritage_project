import requests
import json

url = "https://collectionapi.metmuseum.org/public/collection/v1/search"#?q=van gogh&isOnView=true&hasImages=true"
res = requests.get(url, params={ "q": "van gogh", "isOnView": "true", "hasImages": "true" })
res_json = res.json()
# print(res_json)

# res_json = json.loads(res.text)
formatted_res = json.dumps(res_json, indent=2)
print(formatted_res)
