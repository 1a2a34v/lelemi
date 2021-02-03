# -*- coding: utf-8 -*-
from operator import itemgetter
import pickle
import regex as re
import genanki
import generate_flashcard
import os

class DeckGenerator():
    def __init__(self,name,words):
        self.name = name
        self.words = words

    def load_pickle(self):
        with open('genbun_kotoba/'+self.name+'.pickle', 'rb') as f:
            self.words = pickle.load(f)

    def sort_deck(self):
        sorted_list = []
        for it,w in self.words.items():
            found_place = False
            for i,sw in enumerate(sorted_list):
                if sw[1]["count"]<=w["count"]:
                    ok = (it,w)
                    sorted_list.insert(i,(it,w))
                    break
            if not found_place:
                sorted_list.append((it,w))
        self.words = {}
        for i in sorted_list:
            self.words[i[0]]=i[1]
        #    #i am so fucking depressed
        #    print(w)
        #    print("aiaiai")

    def generate_deck(self):
        self.sort_deck()
        my_model = genanki.Model(
            2042686211,
            'Example',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
            ],
            templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<script>document.body.innerHTML;</script>{{Answer}}',
            },
          ])
        ankideck = genanki.Deck(
            1724897887,
            self.name)
        i = 0
        words = []
        for word in self.words:
            if i<3:
                words.append({word:self.words[word]})
            i+=1
        sorted_wordlist = sorted(self.words.values(), key=itemgetter("count"))
        for word,values in self.words.items():
            card = generate_flashcard.generate_flashcard(word,values)
            if card:
                my_note = genanki.Note(
                    model=my_model,
                    fields=[card["front"], card["back"]])
                ankideck.add_note(my_note)
        my_package = genanki.Package(ankideck)
        my_package.write_to_file(os.path.join(os.path.dirname(__file__),'ankidecks/'+self.name+'_ankideck.apkg'))
