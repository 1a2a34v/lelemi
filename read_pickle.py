# -*- coding: utf-8 -*-
import unittest
import pickle
import os
import sys
import create_flashcards
class TestP(unittest.TestCase):
    def test_generate_card(self):
        name = "koh"
        #previous_wordlist = []
        #words = {}
        with open('saved_wordlists/'+name+'.pickle', 'rb') as f:
            words = pickle.load(f)
        # for filename in os.listdir(os.path.dirname(os.path.realpath(__file__))+"/genbun_kotoba"):
        #     if filename.endswith(".pickle"):
        #         with open('genbun_kotoba/'+filename, 'rb') as f:
        #             words = {**words, **pickle.load(f)}


        anki = create_flashcards.DeckGenerator("kohs",words)
        #anki.load_pickle()
        anki.generate_deck()
        # for i in words:
        #     print(i)
        #
        # with open('genbun_kotoba/tango_oboezumi.pickle', 'wb') as p:
        #     pickle.dump(self.words, p)
        #wiederda_anki.generate_deck()
if __name__ == "__main__":
    unittest.main()
