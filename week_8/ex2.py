import requests
import cloudscraper
from bs4 import BeautifulSoup
import json

url = "https://www.moma.org/artists/?exhibition_id=5224&page=1"

all_artist_names = []
all_artist_data = {}
#  {'Lawrence Abu Hamdan': {'bio': '', 'works': '4\xa0works\xa0online'},

options = {'page': 1}

scraper = cloudscraper.create_scraper()
page = scraper.get(url, params=options)

soup = BeautifulSoup(page.text, 'html.parser')


artist_container = soup.find('div', {'class': 'layout/grid:1 layout/grid:gap:row:baseline:3'})


all_artist = artist_container.find_all('div', {'class': 'layout/flex:column layout/width:100%'})


for art in all_artist:
    h3 = art.find('h3',{'class':'typography'})
    span_h3 = h3.find('span', {'class': 'layout/block'})
    artist_name = span_h3.text.strip()
    all_artist_names.append(artist_name)

    p1 = art.find('p',{'class':'$typography/scale:down $typography/weight:regular typography typography/truncate:4'})
    artist_bio = ''
    if p1 is not None:
        span_p1 = p1.find('span',{'class':'layout/block balance-text'})
        artist_bio = span_p1.text.strip()
    p2 = art.find('p',{'class':'$color/alpha:54% $typography/scale:down $typography/weight:regular typography'})
    artist_works = p2.text.strip()
    all_artist_names.append(artist_name)
    all_artist_data[artist_name]={
        "bio": artist_bio
    }

    if "work" in artist_works:
        all_artist_data[artist_name]["works"] = artist_works

# print the results visually prettier
# print(json.dumps(all_artist_data, indent=2)) 
print(all_artist_data)