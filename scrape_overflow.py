import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests # Getting Webpage content
from bs4 import BeautifulSoup as bs # Scraping webpages
import regex as re

def a(url):
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    body = soup.find('body')
    i = 0
    while True:
        o = soup.findAll('div', {"class":"question-summary search-result"})

        if len(o)>0:
            #for q in o:
            q=o[1]
            print(q)
            q=str(q)
            w=q.find("question-summary-")
            id = ""
            while q[w] != '"':
                id+=q[w]
                w+=1
            print(id.split("-")[-1])

        else:
            break
        break
    o = soup.findAll('div', {"class":"question-summary search-result"})
    print(len(o))

def pq(url):
    pass
URL2 = 'https://stackoverflow.com/search?page={}&tab=Votes&q=caffe'
df1 = a(URL2.format(1))
