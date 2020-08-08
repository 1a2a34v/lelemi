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

    def generate_deck(self):
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
        print("mimimi")
        i = 0
        words = []
        for word in self.words:
            if i<3:
                words.append({word:self.words[word]})
            i+=1
        sorted_wordlist = sorted(self.words.values(), key=itemgetter("count"))
        print(words)
        #[{[{}]}]?
        for word,values in self.words.items():
            card = generate_flashcard.generate_flashcard(word,values)
            if card:
                my_note = genanki.Note(
                    model=my_model,
                    fields=[card["front"], card["back"]])
                ankideck.add_note(my_note)
        my_package = genanki.Package(ankideck)
        # my_package.media_files = ['format.jpg']
        my_package.write_to_file(os.path.join(os.path.dirname(__file__),'ankidecks/'+self.name+'_ankideck.apkg'))
