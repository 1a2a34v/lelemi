import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import gather
import unittest
import pickle
from unittest import mock
import import_source
import create_flashcards

#blablabalbalbalbala
#import sub and pass language marker to converter class
#converter selects scraping functions based on set language
directory = "subs"
seq = ""
domain = "en"
native = "de"
pickle_name = "game"
name = "game_sorted"

with open(os.path.join(os.path.dirname(__file__), '../saved_wordlists/'+pickle_name+'.pickle'), 'rb') as f:
    words = pickle.load(f)
# # words = {'Verweigern': {'iter': 1, 'tatoeba': [{'de': 'Ich verweigere mich, dem Plan zuzustimmen.', 'np': 'その計画に同意するこ とを拒否します。'}, {'de': 'Banken versuchen dir einen Regenschirm zu leihen an einem sonnigen Tag, aber verweigern dir das an einem Regentag.', 'np': '銀行と言うのはお天気の日に傘を貸したがるが、雨の日には、人を見捨てようとするところだ。'}], 'wadoku': [{'de': 'ablehnen, absagen, abschlagen, abwehren, verweigern, Veto einlegen.', 'np': '不承知の'}, {'de': 'ablehnen, abweisen, verweigern, sich nichts sagen lassen, immun sein.', 'np': '不承知の'}, {'de': 'ablehnen, absagen, verweigern.', 'np': '不承知の'}, {'de': '‑ma', 'np': '不承知の'}, {'de': '‑ra', 'np': '不承知の'}, {'de': 'umgehen, ausweichen, vermeiden, ablehnen, verweigern.', 'np': '不承知の'}, {'de': '‑ra', 'np': '不承知の'}, {'de': 'ablehnend, abschlägig, missbilligend, zurückweisend, verweigernd, nicht einverstanden.', 'np': '不承知の'}, {'de': 'ablehnend, abschlägig, missbilligend, zurückweisend, verweigernd, nicht einverstanden.', 'np': '不承知の'}]}}
anki = create_flashcards.DeckGenerator(name,words)
#anki.load_pickle()
anki.generate_deck()
