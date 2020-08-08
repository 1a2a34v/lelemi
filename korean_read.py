# -*- coding: utf-8 -*-
import import_source
import create_flashcards
import pickle
import os


#blablabalbalbalbala
#import sub and pass language marker to converter class
#converter selects scraping functions based on set language
directory = "subs"
seq = ""
domain = "kr"
native = "en"
name = "soo"

for filename in os.listdir(directory):
    if filename.endswith(".srt"):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = os.path.join(directory, filename)
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path, 'r', errors='ignore') as sub:
            seq+=sub.read()

seq = "Drogo"

converted_sequence = import_source.SequenceConverter(seq,name,domain,native)
converted_sequence.generate_wordlist()
print(converted_sequence.words)
# converted_sequence.retrieve_wordinfo()
# # # words = {'Verweigern': {'iter': 1, 'tatoeba': [{'de': 'Ich verweigere mich, dem Plan zuzustimmen.', 'np': 'その計画に同意するこ とを拒否します。'}, {'de': 'Banken versuchen dir einen Regenschirm zu leihen an einem sonnigen Tag, aber verweigern dir das an einem Regentag.', 'np': '銀行と言うのはお天気の日に傘を貸したがるが、雨の日には、人を見捨てようとするところだ。'}], 'wadoku': [{'de': 'ablehnen, absagen, abschlagen, abwehren, verweigern, Veto einlegen.', 'np': '不承知の'}, {'de': 'ablehnen, abweisen, verweigern, sich nichts sagen lassen, immun sein.', 'np': '不承知の'}, {'de': 'ablehnen, absagen, verweigern.', 'np': '不承知の'}, {'de': '‑ma', 'np': '不承知の'}, {'de': '‑ra', 'np': '不承知の'}, {'de': 'umgehen, ausweichen, vermeiden, ablehnen, verweigern.', 'np': '不承知の'}, {'de': '‑ra', 'np': '不承知の'}, {'de': 'ablehnend, abschlägig, missbilligend, zurückweisend, verweigernd, nicht einverstanden.', 'np': '不承知の'}, {'de': 'ablehnend, abschlägig, missbilligend, zurückweisend, verweigernd, nicht einverstanden.', 'np': '不承知の'}]}}
# anki = create_flashcards.DeckGenerator(name,converted_sequence.words)
# #anki.load_pickle()
# anki.generate_deck()
