import requests
from pyquery import PyQuery as pq
from collections import namedtuple
from bs4 import BeautifulSoup
import re
import pickle
from time import sleep
import os
#und ein paar auch verloren
finished = False
url="https://kitsunekko.net/"
cwd = os.getcwd()

def get_file(link,dir,title):
    path = dir+"/"+title
    print(path)
    f = open(path, "wb")
    resp = requests.get(url+link,allow_redirects=True)
    f.write(resp.content)
    f.close()

def retrieve_files(link,dir):
    link = url+link
    if link.split(".")=="rar" or link.split(".")=="zip":
        get_file(link,dir)
        #i am not special
        #i am surrounded
        #and i am not special
        #sentiments are sent to me
        #i reply sometimes
    else:
        resp = requests.get(link)
        soup = BeautifulSoup(resp.content,features="html.parser",from_encoding='utf8')
        table1 = soup.find('table', id="flisttable")
        table2 = table1.find('tbody')
        table3 = table2.find_all('tr')
        for i in table3:
            a = i.find('a',href=True)["href"]
            title = i.find("strong").text
            end = a.split(".")[-1]
            if end == "ass":
                get_file(a,dir,title)
            elif end == "zip":
                try:
                    get_file(a,dir,title)
                    from pyunpack import Archive
                    Archive(dir+"/"+title).extractall(dir)
                except:
                    print("unzipping failed")
            else:
                print("NONONO")
###program starts here:
def main():
    global finished
    offers = []
    lastid=''
    iter=0

    #visit the new announces page by page from link
    while finished == False:
        resp = None
        pagelink = 'https://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese%2F'
        while not resp:
            try:
                resp = requests.get(pagelink)
            #requests error
            except Exception as e:
                print("sleepingpage ",pagelink)
                print(e)
                sleep(10)
            #pagecaptcha enabled, call adjust_proxy flisttable

        soup = BeautifulSoup(resp.content,features="html.parser",from_encoding='utf8')
        table1 = soup.find('table', id="flisttable")
        table2 = table1.find('tbody')
        table3 = table2.find_all('tr')
        for i in table3:
            a = i.find('a',href=True)
            title = i.find("strong").text
            dir = cwd+"/sources/jani/"+title
            try:
                os.mkdir(dir)
                retrieve_files(a["href"],dir)
            except FileExistsError:
                print("Filealready")
        finished = True
        iter+=1
        if iter==2:
            break
    #     ids = [tr.attrib['adid'] for tr in trs]
    #     try:
    #         lastpos = ids.index(lastid)
    #     except:
    #         lastpos = len(ids)
    #         trs = trs[:lastpos]
    #         ids = ids[:lastpos]
    #     data = []#
    #     for i in trs:
    #         tr = parse_tr(i)
    #         if tr in gathered_links:
    #             #create offer object from link
    #             troffer = Offer(tr)
    #             if troffer.disabled_entry:
    #                 city_finished = True
    #                 break
    #             else:
    #                 if troffer in gathered_offers:
    #                     gathered_offers.index(troffer).updated.append(datetime.datetime.now())
    #                 else:
    #                     gathered_offers[gathered_links.index(tr)] = troffer
    #         else:
    #             if city_finished:
    #                 break
    #             if tr is not None:
    #                 data.append(tr)
    #     for i in data:
    #         o = Offer(i)
    #         offers.append(o.__dict__)
    #     if city_finished:
    #         break
    #     iter = iter+1
    # print("donedone ",iter)
    # try:
    #     old_offers = list(set(gathered_offers)-set(offers))
    # except:
    #     print("disregarding old offers")
    #     old_offers = []
    # print("offerlist ",offers)
    # print("gathered offers ",gathered_offers)
    # gathered_offers = offers+old_offers
    # #save offer list to file
    # with open('wglist.pickle', 'wb') as f:
    #     pickle.dump(gathered_offers, f, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    main()
