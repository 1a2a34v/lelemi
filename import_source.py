# -*- coding: utf-8 -*-
import spacy
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

import gather

log = logging.getLogger()

class SequenceConverter():

    def __init__(self,seq,name,domain,native,minimum_frequency):
        #self.domain_nlp_lookup = {"de":"de","en":"en_core_web_sm",}
        # self.nlp = spacy.load(self.domain_nlp_lookup[domain])
        self.nlp = spacy.load(domain)
        self.seq = self.nlp(seq)
        self.domain = domain
        self.native = native
        self.name = name
        self.minimum_frequency = minimum_frequency
        self.words = None
        self.wlist = []
        self.lu ={
            "Ã¤":"ä",
            "Ã¼":"ü",
            "Ã¶":"ö",
            "ÃŸ":"ß"
        }
        self.numbers = [1,2,3,4,5,6,7,8,9,0]
        self.dictionaries={
            "jpde":["wadoku",["tatoeba","deu","jpn"]],
            #"ende":[["wordref","ende"],["tatoeba","eng","deu"]],
            #"deen":[["wordref","deen"],["tatoeba","deu","eng"],["tatoeba","deu","jpn"]],
            #"dejp":[["wordref","deen"],["tatoeba","deu","eng"],["tatoeba","deu","jpn"]],
            "defr":[["wordref","defr"],["tatoeba","fra","deu"]]
        }

    def generate_wordlist(self):
        words = {}
        for w in self.seq:
            word = w.lemma_
            for i,val in self.lu.items():
                if i in str(word):
                    word = str(word).replace(i,val)
            isnum = False
            for i in self.numbers:
                if str(i) in word:
                    isnum = True
            print(w.lemma_)
            print(w.pos_)
            print(self.nlp)
            if (w.pos_=="NOUN" or w.pos_=="AUX"  or w.pos_=="VERB" or w.pos_=="ADV") and not isnum:
                if word in words:
                    words[word]["count"]+=1
                    words[word]["wtype"]=w.pos_
                else:
                    words[word]={"count":1,"wtype":w.pos_}
        for word,values in list(words.items()):
            if values["count"]<self.minimum_frequency:
                r = dict(words)
                del r[word]
                words = r
        self.words = words

    # def threa(self):
    #     while len(self.wlist)>0:
    #         word = self.wlist.pop(0)
    #         print(word)
    #         try:
    #             print(self.words[word])
    #             for i in self.dictionaries[self.domain]:
    #                 print("mimimi")
    #                 result = gather.gather(i,word)
    #                 self.words[word][str(i)]=result
    #                 print(self.words[word][i])
    #                 print("okokok")
    #         except Exception as e:
    #             print(e)


    def retrieve_wordinfo(self):
        start = time.time()
        self.wlist = list(self.words.keys())
        print("hahahahaha")
        # for x in range(1):
        #      t = threading.Thread(target=self.threa)
        #      t.daemon = True
        #      t.start()
        while len(self.wlist)>0:
            word = self.wlist.pop(0)
            print(self.dictionaries[self.native+self.domain])
            try:
                for i in self.dictionaries[self.native+self.domain]:
                    result = gather.gather(i,word)
                    #if result is just "wordref" or ["tatoeba", "blabla"]
                    if isinstance(i, str):
                        self.words[word][i]=result
                    else:
                        if i[0] in self.words[word].keys():
                            print(result)
                            self.words[word][i[0]]+=result
                        else:
                            self.words[word][i[0]]=result
                isempty = True
                for key,val in self.words[word].items():
                    if key!="count" and key!="wtype" and val!=[]:
                        isempty = False
                if isempty:
                    self.words.pop(word)
            except Exception as e:
                print("brbr")
                print(e)
            #   time.sleep(1)
        print('Entire job took:',time.time() - start)
        with open(os.path.join(os.path.dirname(__file__), 'saved_wordlists/'+self.name+'.pickle'), 'wb') as p:
            pickle.dump(self.words, p)

#
# save_obj(wordlist,"words.sy")
