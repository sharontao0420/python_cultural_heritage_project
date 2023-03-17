
import requests
import cloudscraper
from bs4 import BeautifulSoup

url = "https://www.moma.org/artists/?exhibition_id=5224&page=1"

all_artist_names = []

options = {'page': 1}

scraper = cloudscraper.create_scraper()
page = scraper.get(url, params=options)

soup = BeautifulSoup(page.text, 'html.parser')


artist_container = soup.find('div', {'class': 'layout/grid:1 layout/grid:gap:row:baseline:3'})


all_artist = artist_container.find_all('div', {'class': 'layout/flex:column layout/width:100%'})

for art in all_artist:
    h3 = art.find('h3',{'class':'typography'})
    span = h3.find('span', {'class': 'layout/block'})
    name = span.text
    all_artist_names.append(name)

# why do I need to use for loop instead of finding the object within the layers?
 
# h3 = all_artist.find('h3',{'class':'typography'})
# span_tag = h3.find('span', {'class': 'layout/block '})
# if span_tag:
#     name = span_tag.text
#     all_artist_names.append(name)
#     # print(name)  # Output: "Hello World"
# else:
#     print("Span tag not found")
    



print(all_artist_names)
# print(len(all_artist_names))