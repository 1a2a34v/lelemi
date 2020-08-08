# -*- coding: utf-8 -*-
import spacy
import genbun_yomikomi
import unittest
import pickle

class TestYo(unittest.TestCase):
    def test_tatoeba(self):
        a = genbun_yomikomi.SequenceConverter("","kotobaatume")
        result = a.get_tatoeba("Schule")
        result = a.get_wadoku("Schule")
        print(result)
# class TestAT(unittest.TestCase):
#     def test_generate_card(self):
#         # a = genbun_yomikomi.SequenceConverter("verkaufen","wiederda")
#         #w = a.get_wadoku("verkaufen")
#         #print(w)
#         nlp = spacy.load('de')
#         name = "kotobaatume"
#         seq = open("hondana/"+name+".book", "r")
#         seq = nlp(seq.read())
#         a = genbun_yomikomi.SequenceConverter(seq,"wiederda")
#         #t = a.get_tatoeba("verkaufen")
#         a.generate_wordlist()
#         a.generate_dict()
if __name__ == "__main__":
    unittest.main()
#sososososososo
#I want to put in a new book. I want to be able to define an order for these books, but manually putting 1.234_ in  front of every
#entry would be taxing. or would it?
#and once you do have the folder with all the stuffystuff blublublublub it is still annoying...but there is no way around.
#so you have the genbun_kotoba thingy doing its other thingy.
#i am so bored out of my mind. I am so bored out of my mind.
#multiple steps involved:
#   genbun_yomikomi takes the 1.2345_name.book file and generates a 1.2345_name.pickle file containing the hierarchy dict. (spacy main)
#   netto_kakiatsume takes the 1.2345_name.pickle file , which NOW is still a nested dict with{word:{},word:{}...}, and fills it with
# wadoku and tatoeba entries. if more are to come they are all added in this module. (requests main)
# anki tsukure takes a dict, regardless of how it's filled, verifies the entries of each word and then writes the deck. (anki/html main)
# main is called with multiple possible options.
###---redo recreates all decks for all books in the hondana directory. a backup of decks and pickles is created before any change.
###--cleanup is used after rearranging the hondana hierarchies. anki decks are backed up and then recreated based on the new order
###if no keyword is provided main will simply create entries for books for which no pickles exist.
#     )
# fuck wie soll ich mich um dabbel drumrum winden. je länger ich hier bin desto tiefer werde ich reingezogen. desto mehr werde ich teil
# vom kern was das alles hier FUCKFUCKFUCK ausmmacht. natürlich ist abel nett zu mir. wie viele sind schoon bereit um zu leben glas zu essen?
# muss ja schön sein wie LS mit schreiben und style seine existenzberechtigung aufzubauen.
