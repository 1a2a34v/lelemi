# -*- coding: utf-8 -*-
import requests
import sqlite3
import pickle
import re
from bs4 import BeautifulSoup
import json
from html.parser import HTMLParser
import threading
from queue import Queue
import time
import logging
import os
from time import sleep
import gather
import parser
from korean_romanizer.romanizer import Romanizer

#abilty to select how to append to present datafile containing all domain words
#create logging object for each session
#create testengine for all sites
#create jsonreading pickleloader

log = logging.getLogger()

class Flashcard_Collection():

    def __init__(self,wordsequence,name,domain,native,minimum_frequency):
        #self.domain_nlp_lookup = {"de":"de","en":"en_core_web_sm",}
        # self.nlp = spacy.load(self.domain_nlp_lookup[domain])
        self.wordsequence = None
        self.domain = domain
        self.native = native
        self.name = name
        self.minimum_frequency = minimum_frequency
        self.words = {}
        self.wlist = []
        self.dictionaries={
            "enjp":["jisho",["tatoeba","jpn","eng"]],
            "dejp":["wadoku",["tatoeba","jpn","deu"]],
            "jpde":["wadoku",["tatoeba","deu","jpn"],["tatoeba","deu","jpn"]],
            "jpen":["jisho",["tatoeba","eng","jpn"],["tatoeba","eng","deu"],"gpic"],
            #"ende":[["wordref","ende"],["tatoeba","eng","deu"]],
            #"deen":[["wordref","deen"],["tatoeba","deu","eng"],["tatoeba","deu","jpn"]],
            #"dejp":[["wordref","deen"],["tatoeba","deu","eng"],["tatoeba","deu","jpn"]],
            "defr":[["wordref","defr"],["tatoeba","fra","deu"]],
            "enko": ["picture","krdict",["tatoeba","kor","eng"]]
        }
        self.words = parser.parse(wordsequence,domain)
        self.connected = True

    def see_inc(self, word):
        lem = word.pos_
        for i in range(15):
            w = self.nlp(str(word))
            a = w[0].pos_
            if a is not lem:
                return a
        return None

    def threa(self):
        while len(self.wlist)>0:
            try:
                word = self.wlist.pop(0)
                print("downloading ",word)
                for i in self.dictionaries[self.native+self.domain]:
                    print("iii",i)
                    result = gather.gather(i,word)
                    print("okoko")
                    if isinstance(i, str):
                        print("okokokk")
                        self.words[word][i]=result
                    else:
                        print("okokokkk")
                        if i[0] in self.words[word].keys():
                            self.words[word][i[0]]+=result
                        else:
                            self.words[word][i[0]]=result
                print("okokok")
                isempty = True
                for key,val in self.words[word].items():
                    if key!="count" and key!="wtype" and val!=[]:
                        isempty = False
                if isempty:
                    print("no information found for ",str(word))
                    self.words.pop(word)
            except:
                self.connected = False
                self.wlist.append(word)
                break
            print("goinf")

    def retrieve_wordinfo(self):
        start = time.time()
        self.wlist = list(self.words.keys())
        print("hahahahaha")
        print(self.wlist)
        for x in range(1):
             t = threading.Thread(target=self.threa)
             t.daemon = True
             t.start()
        while len(self.wlist)>0:
            sleep(1)
            if not self.connected:
                while not self.connected:
                    try:
                    	request = requests.get("http://google.com", timeout=5)
                    	self.connected = True
                    except (requests.ConnectionError, requests.Timeout) as exception:
                    	print("Reconnecting")


        sleep(5)
        print('Entire job took:',time.time() - start)
        with open(os.path.join(os.path.dirname(__file__), 'saved_wordlists/'+self.name+'.pickle'), 'wb') as p:

            pickle.dump(self.words, p)



# save_obj(wordlist,"words.sy")
