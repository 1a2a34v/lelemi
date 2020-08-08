import requests
from bs4 import BeautifulSoup
import re
import json
#import ast
import sys
import os

def gather(dictionary,word):
    print(word)
    if dictionary=="wadoku":
        return get_wadoku(word)
    if "tatoeba" in dictionary:
        return get_tatoeba(word,dictionary[1],dictionary[2])
    if "wordref" in dictionary:
        return get_wordref(word,dictionary[1])


def get_wordref(word,inputoutput):
    try:
        print("WOWW")
        url="https://www.wordreference.com/{}/{}".format(inputoutput,word)
        vstr=requests.get(url).content
        soup = BeautifulSoup(vstr,features="html.parser",from_encoding='utf8')
        table = soup.find("div", attrs={'class': 'content'})
        ok = table.findAll("td", attrs={'class': 'ToWrd'})
        wordref = []

        if ok:
            for i in ok:
                if "<em class=" in str(i):
                    result = re.search('<td class="ToWrd">(.*)<em class=', str(i))
                    wordref.append(result.groups(1)[0])
            return wordref
        else:
            entry = soup.find("li", attrs={'class': 'arablist'})
            result = soup.find("span", attrs={'class': 'roman'})
            result = re.search('<span class="roman">(.*)</span>', str(result))
            return [result.groups(1)[0]]
    except Exception as e:
        print("lelele")
        print(e)

def get_wadoku(word):
    url="https://www.wadoku.de/search/{}".format(word)
    # vstr=requests.get(url).content
    # k=re.search('<h2><a id="ch_lblVerb" class="targetted-word-transl" style="color:#0970ac;" tooltip="vorhandener Infinitiv">hingeben</a></h2>',vstr)
    vstr=requests.get(url).content
    soup = BeautifulSoup(vstr,features="html.parser")
    rows = soup.findAll('div', {"class":"japanese"})
    wadoku=[]
    nrows = soup.findAll('div', {"class":"japanese"})
    # for nrow in nrows:
    table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="resulttable")
    if table:
        rows = table.findAll(lambda tag: tag.name=='tbody')
        for row in rows:
            npdiv = row.find('div', attrs={'class': 'japanese'})
            np = re.search('xml:lang="ja">(.*?)<',str(npdiv)).groups()[0]
            ddiv = row.find('div', attrs={'class': 'd'})#
            dsec = row.find('section', attrs={'class': 'senses'})
            #for i in dsec:
            de = str(dsec.text.strip()).replace('n\xa0n', '').replace('m\xa0m', '').replace('f\xa0f', '')
            de=de.replace('\xa0', '.')
            if len(de)>100:
                de = de[:100]
                # dspan = i.find('span', attrs={'class': 'sense'})
#                print(dspan)
                # if not "span" in i:
                #     de+=str(i)+"; "
            wadoku.append({'de':de,'np':np})
    return wadoku

def get_tatoeba(word,inputlang,resultlang):
    try:
        # url="https://tatoeba.org/eng/sentences/search?query={}&from=deu&to=jpn".format(word)
        url="https://tatoeba.org/eng/sentences/search?query={}&from={}&to={}".format(word,inputlang,resultlang)
        # vstr=requests.get(url).content
        # k=re.search('<h2><a id="ch_lblVerb" class="targetted-word-transl" style="color:#0970ac;" tooltip="vorhandener Infinitiv">hingeben</a></h2>',vstr)
        vstr=requests.get(url).content
        soup = BeautifulSoup(vstr,features="html.parser",from_encoding='utf8')
        rows = soup.findAll('div', {"class":"sentence-and-translations"})
        tatoeba=[]
        for row in rows:
            # data = '[' + row['ng-init'][11:-1] + ']'
            # print("okok")
            # print(type(data))
            # print(data)
            # print(data)
            if row:
                data = '[' + row['ng-init'][11:-1] + ']'
                # data = ast.literal_eval(data)
                # print(type(data))
                data = json.loads(data.replace(", [], '{}'".format(resultlang),"").replace(", '{}'".format(resultlang),""))
                # a=row.find('div',{'class':'translation'})
                # a=a.find('div',{'layout':'row'})
                #a=a.find('div',{'class':'text flex'})
                de = data[0]['text']
                np=""
                for item in data[1]:
                    np=item['text']+" "
                if len(data)>2:
                    for item in data[2]:
                        np+=item['text']
                tatoeba.append({'de':de,'np':np})
        return tatoeba
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("aaaa")
        print(exc_type, exc_tb.tb_lineno)
        print(e)
