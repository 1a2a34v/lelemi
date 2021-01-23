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
from time import sleep
import gather
import textwrap
from korean_romanizer.romanizer import Romanizer

#abilty to select how to append to present datafile containing all domain words


log = logging.getLogger()

class SequenceConverter():

    def __init__(self,seq,name,domain,native,minimum_frequency):
        #self.domain_nlp_lookup = {"de":"de","en":"en_core_web_sm",}
        # self.nlp = spacy.load(self.domain_nlp_lookup[domain])
        self.seq = None
        self.domain = domain
        self.native = native
        self.name = name
        self.minimum_frequency = minimum_frequency
        self.words = {}
        self.wlist = []
        self.lu ={
            "Ã¤":"ä",
            "Ã¼":"ü",
            "Ã¶":"ö",
            "ÃŸ":"ß"
        }
        self.numbers = [1,2,3,4,5,6,7,8,9,0]
        self.dictionaries={
            "jpde":["wadoku",["tatoeba","deu","jpn"],["tatoeba","deu","jpn"]],
            "jpen":["jisho",["tatoeba","eng","jpn"],["tatoeba","eng","deu"],"gpic"],
            #"ende":[["wordref","ende"],["tatoeba","eng","deu"]],
            #"deen":[["wordref","deen"],["tatoeba","deu","eng"],["tatoeba","deu","jpn"]],
            #"dejp":[["wordref","deen"],["tatoeba","deu","eng"],["tatoeba","deu","jpn"]],
            "defr":[["wordref","defr"],["tatoeba","fra","deu"]],
            "enko": ["picture","krdict",["tatoeba","kor","eng"]]
        }
        if self.domain == "ko":
            from konlpy.tag import Okt
            okt = Okt()
            pos = okt.pos(seq)
            words = {}
            for i in pos:
                if i[1]!="Alpha" and i[1]!="Foreign":
                    if i[0] not in words.keys():
                        words[i[0]] = {
                            "count":1,
                            "wtype":i[1]
                        }
                    else:
                        words[i[0]]["count"]+=1
                    try:
                        words[i[0]]["romanization"] = Romanizer(i[0]).romanize()
                    except:
                        words[i[0]]["romanization"] = "Romaerror"
            self.words = words
        else:
            self.nlp = spacy.load(domain)
            self.seq_raw = seq
            if len(self.seq_raw)>1000000:
                for i in textwrap.wrap(self.seq_raw, 900000):
                    self.seq = self.nlp(i)
                    self.generate_wordlist()
            else:
                self.seq = self.nlp(seq)
                self.generate_wordlist()

    def see_inc(self, word):
        lem = word.pos_
        for i in range(15):
            w = self.nlp(str(word))
            a = w[0].pos_
            if a is not lem:
                return a
        return None

    def generate_wordlist(self):
        if self.domain == "ko":
             from konlpy.tag import Okt
             okt = Okt()
             pos = okt.pos(p)
             words = {}
             for i in pos:
                 if i[1]!="Alpha" and i[1]!="Foreign":
                     if i[0] not in words.keys():
                         words[i[0]] = {
                             "counter":1,
                             "wtype":i[1]
                         }
                     else:
                         words[i[0]]["counter"]+=1
             self.words = words
        else:
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
                if (w.pos_=="NOUN" or w.pos_=="AUX"  or w.pos_=="VERB" or w.pos_=="ADV" or w.pos_=="ADJ") and not isnum:
                    if word in self.words:
                        self.words[word]["count"]+=1
                    else:
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
            if not self.words:
                self.words = words
            else:
                self.words={**self.words, **words}

    def threa(self):
        while len(self.wlist)>0:
            word = self.wlist.pop(0)
            print("downloading ",word)
            for i in self.dictionaries[self.native+self.domain]:
                result = gather.gather(i,word)
                if isinstance(i, str):
                    self.words[word][i]=result
                else:
                    if i[0] in self.words[word].keys():
                        self.words[word][i[0]]+=result
                    else:
                        self.words[word][i[0]]=result
            isempty = True
            for key,val in self.words[word].items():
                if key!="count" and key!="wtype" and val!=[]:
                    isempty = False
            if isempty:
                print("no information found for ",str(word))
                self.words.pop(word)

    def retrieve_wordinfo(self):
        start = time.time()
        self.wlist = list(self.words.keys())
        print("hahahahaha")
        for x in range(1):
             t = threading.Thread(target=self.threa)
             t.daemon = True
             t.start()
        while len(self.wlist)>0:
            sleep(1)
        sleep(5)
        print('Entire job took:',time.time() - start)
        with open(os.path.join(os.path.dirname(__file__), 'saved_wordlists/'+self.name+'.pickle'), 'wb') as p:

            pickle.dump(self.words, p)



# save_obj(wordlist,"words.sy")
