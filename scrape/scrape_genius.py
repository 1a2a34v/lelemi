import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests # Getting Webpage content
from bs4 import BeautifulSoup as bs # Scraping webpages
import regex as re
import unicodedata as ud
#fix cutoff dinosaur 
def album(url):
    words = ""
    artist = url.split("/")[-2]
    albumname = url.split("/")[-1]
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    body = soup.find('body')
    i = 0
    o = soup.findAll('div', {"class":"chart_row-content"})
    songs = []
    for i in o:
        a = i.find("a",href=True)
        songs.append(a["href"])
    for i in songs:
        words+=song(i)
        words+="\n"
    with open("{}_{}.txt".format(artist,albumname),"w") as f:
        f.write(words)

def song(url):
    words = ""
    soup = bs(requests.get(url).content, 'html.parser')
    text = soup.select_one('div[class^="Lyrics__Container"], .lyrics').get_text(strip=True, separator='\n')
    song = ""
    text=re.split('\n| ', text)
    for i in text:
        isa=False
        print(i)
        for l in i:
            if 'HANGUL' in ud.name(l):
                isa = True
        if isa:
            words+=i+" "
    return words
albums = ["Play","Summer-episode","Winter","Spring","Sailing"]
for i in albums:
    album("https://genius.com/albums/Akmu/{}".format(i))
# song("https://genius.com/Akmu-give-love-lyrics")
