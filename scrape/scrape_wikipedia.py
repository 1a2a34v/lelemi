import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests # Getting Webpage content
from bs4 import BeautifulSoup as bs # Scraping webpages
import regex as re
import os
import pickle

url = 'https://de.wikipedia.org/wiki/Faschismus'
keywords = ["Faschismus","Extremismus","Ideologie","Nationalismus","Rassismus"]
pile = ""
current_iteration = 0
current_url_index = ()
discarded = []
max_discarded = 1000
suited_links = []
desired_suited = 50
#so we gather all links connected to the initial link in a list
#the initial link is scraped until criteria are met or enough links containing relevant keywords are found
#once the initial link is scraped, all links contained are searched for relevant keywords and a new list of initial links is created
#because we are trying to stay as connected as possible to the initial link, we require a recursive function that treats
#initial links differently from regular links which are only searched for links again if the suited link number requirement
#is not met after the currently loaded list is finished scraping
#this means that blubblub blabla blibblib hihi huhu hahaha
#we need to save the state of the pile after completion and segment it into a dictionary containing information such as
#pile origin(url), number of different words(?), and index in our suited links list

#also, given that blubblub
#given that with the provided set of keywords we may never reach our desired suited link number
#so we create a discarded links pile and abort if a threshold of upper_max is reached

#i am so lonely and sad and the idea that people are capable of being as "happy" as the youtubers we are seeing
#is distancing itself so fast it is creating a vacuum between us
#maybe it can help me be sucked upwards in that direction?

#so much potential means so much wasted potential, inevitably always
#francafrancafrancafrancaFUCKFUCKFUCK
#i am so scared
#of being seen the way i see stef
#short tempered and unpredictable
#scary to be around
#the way alica sees me
#stef if i try to help you we will both drown
#the only way for us to have a chance at mutually succeeding
#is by finding our ways seperately
#please dont hold a grudge against me
#though i am sure you will
#though i know the grudge you hold towards yourself is the biggest one
#your own inabilities and shortcomings, all the fault of your parents for making you and everything else this way
#you are nothing but a victim and the world is supposed to feel bad for you but also admire you for your smartness

#the other humans blanky has barely ever felt as warm as it does now
#i forget all that was plaguing me
#keeping me from _
#this feeling of complete envelopment
#i missed it so much
#and it will disappear again
#i will be alone with death dispair pain and suffering soon enough
#in a world that is so obviously hell
#i will be alone with those that create hell
#those that lodged themselves deeply into my brain by showing me their despicable selves through their actions
#i just want to play
#i never ever ever wanted to be the 3deep achieving through paind and suffering type of person
#yet now that i am here
#there is not much else left for me
#francafrancafranca
#every single day i completely obliterate any trace of humanity inside of me
#i do so because i know the steps so well
#i know how you can use your eyes in a way
#that will make you see others for only their absolute worst qualities
#everything i built myself on, anything that could possibly be, all turns to mush
#how are you?
#i cannot possibly count the number of times i felt like asking you
#yet i never do
#because i am so scared to take a chance
#is what i like to tell myself sometimes
#but the truth is
#the stupid disgusting truth is that i know i am a burden
#only i know how heavily hardcore i am capable of pulling downwards
#and anyone i associate myself with in this way
#will be pulled downwards
#how are you
#what have you been up to
#how have you been spending your time
#all questions stef asked me
#and i said
#go find someone else:/
#sorrysorry
#despicable humans telling me

#sometimes feelings of missing other humans become so overwhelming
#breathing is barely possible
#distraction becomes the only alternative
#yet intrusive thoughts make their way through the noise regardless
#"i am so sad and depressed"
#i wouldnt want simone to be like that
#yet i spend most of my time down in this pit
#with all the other despicable pos people
#because we deserve each other
#franca doesnt deserve me
#please be happy
#please dont be like me
#i mean these words more than anything i have written before
#please live the fairytalelife i for some reason believe you deserve
#that i am sure i would be an obstacle in
#i miss you so much
#but time moves on
#i stay here
#you move forward
#time creates new pain
#i "deal with it"
#until i stop finding ways to and panic
#until i find myself crawling on the ground again
#ist ein einziger kreis

#lying will be
#an inevitable part of something if something were to become something in reality
#i would want to be lied to in a sense
#so its only fair if i do the same for the other sides sake
#finding the proper balance is the challenge

#i like you and i hate me
#yet turning chessboards is my numberone hobby
#and you really believe this to be maintainable?
def gather_content(soup):
    global pile
    body = soup.find('body')
    text = soup.find_all(text=True)
    output = ''
    blacklist = [
    	'[document]',
    	'noscript',
    	'header',
    	'html',
    	'meta',
    	'head',
    	'input',
    	'script',
    	# there may be more elements you don't want, such as "style", etc.
    ]
    for t in text:
    	if t.parent.name not in blacklist:
    		output += '{} '.format(t)
    if "↑" in output:
        output = output.split("↑")[0]
    if "Siehe auch" in output:
        output = output.split("Siehe auch")[0]
    # if any(word in pile for word in keywords):
    for w in keywords:
        if re.search(w, output, re.IGNORECASE):
            # pile[url.split("/")[-1]]= {
            #     "url":url,
            #     "index":
            # }
            pile+=" "+str(output)
            print("hohohohohohoho")
            return True
    return False

def retrieve_links(soup):
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    dlinks = []
    badkeys = ["//","#","svg","Hilfe","index","Über","Impressum","Diskussion","Portal","Hauptseite","Spezial","Wikipedia"]
    for i in links:
        bad = False
        for key in badkeys:
            if key in i:
                bad = True
        #     if i.split("//")[-1].split(".")[0]=="de":
        #         dlinks.append(i)
        #    dlinks.append(i.split("/")[-1])
        if not bad:
            dlinks.append("https://de.wikipedia.org"+i)
    return dlinks

def a(init_url,req = False):
    global suited_links
    global discarded_links
    global current_iteration
    global discarded_links
    #sosososososososososo
    #wewewe do this thing and then blubblub
    #arghghghghghghghghgh
    #we have a main link first
    #this main link is scraped, then all the new main links contained in it are stored in the links list
    #every single one of these links is first scraped without going deeper, then, once we are there and our desired listsize is still not reached
    #we create a new list of links based on these new mainpages
    #this list is always stored globally under suited links and (for now) updated periodically upon entering a new iteration
    links = []
    sub_links = []
    while len(suited_links)<desired_suited:
        if len(suited_links)==0:
            response = requests.get(init_url)
            soup = bs(response.content, 'html.parser')
            gather_content(soup)
            links = retrieve_links(soup)
            suited_links.append(init_url)
            print("inny")
            print(suited_links)
        else:
            url = links.pop(-1)
            if url not in suited_links:
                response = requests.get(url)
                soup = bs(response.content, 'html.parser')
                suited = gather_content(soup)
                if suited:
                    print(url)
                    sub_links.append(retrieve_links(soup))
                    suited_links.append(url)
                if len(links) == 0:
                    links = sub_links
                    sub_links = []

    print(len(suited_links))

    # links = []
    # for url in urls:
    #     suited = gather(url)
    #     if suited:
    #         suited_links.append(url)
    #         desired_suited-=1
    #     else:
    #         discarded_links.append(url)
    #
    #
    #     for i in dlinks:
    #         if i not in scraped_links and len(scraped_links)<page_number and upper_max > 0:
    #             upper_max-=1
    #             scraped_links.append(i)
    #             a(i)
    #     if len(scraped_links)<page_number:
    #         while len(scraped_links)<page_number:
    #             scraped_links

#fname = 'keywiki_{}.pickle'.format(url.split("/")[-1])
# if os.path.isfile(fname):
#     with open(fname, 'rb') as f:
#         data = pickle.load(f)
#         pile = data["pile"]
#         current_iteration = data["current_iteration"]
#         suited_links = data["suited_links"]
#         discarded_links = data["discarded_links"]
#         current_url_index = data["current_url_index"]
#     if desired_suited<data["desired_suited"]:
#         while desired_suited<data["desired_suited"]:
#             if len([pile][-1])==0:
#                 current_iteration-=1
#             pile[current_iteration].pop(-1)
#             desired_suited+=1
#     else:
#         a()

a(url,req = True)

# with open(os.path.join(os.path.dirname(__file__), fname), 'wb') as p:
#     data = {
#         "pile":pile,
#         "current_iteration":current_iteration,
#         "current_url_index":current_url_index,
#         "suited_links":suited_links,
#         "discarded_links":discarded_links,
#         "desired_suited":desired_suited
#     }
#     pickle.dump(data, p)
with open("keywiki.srt","w") as f:
    # f.write(str(wordlist))
    f.write(pile)
print(pile)
print("okok")
