# -*- coding: utf-8 -*-
import anki_tsukure
import unittest
import pickle
class TestAT(unittest.TestCase):
    def test_generate_card(self):

        word = "Verweigern"
        value = {
        'iter': 1,
        'tatoeba':[
        {'de': 'Ich verweigere mich, dem Plan zuzustimmen.','np': 'その計画に同意することを拒否します。'},
        {'de': 'Banken versuchen dir einen Regenschirm zu leihen an einem sonnigen Tag, aber verweigern dir das an einem Regentag.',
        'np': '銀行と言うのはお天気の日に傘を貸したがるが、雨の日には、人を見捨てようとするところだ。'}
        ],
        'wadoku': [
        {'de': '‑ra', 'np': '不承知の'},
        {'de': 'umgehen, ausweichen, vermeiden, ablehnen, verweigern.', 'np': '不承知の'},
        {'de': '‑ra', 'np': '不承知の'}, {'de': 'ablehnen, absagen, abschlagen, abwehren, verweigern, Veto einlegen.',
        'np': '不承知の'}, {'de': 'ablehnen, abweisen, verweigern, sich nichts sagen lassen, immun sein.', 'np': '不承知の'},
        {'de': 'ablehnen, absagen, verweigern.', 'np': '不承知の'}, {'de': '‑ma', 'np': '不承知の'},
        {'de': 'ablehnend, abschlägig, missbilligend, zurückweisend, verweigernd, nicht einverstanden.', 'np': '不承知の'},
        {'de': 'ablehnend, abschlägig, missbilligend, zurückweisend, verweigernd, nicht einverstanden.', 'np': '不承知の'}]}
        name = "wiederda"

        wiederda = anki_tsukure.DeckGenerator(name)
        wiederda.load_pickle()
        ww=""

        #wiederda_anki.generate_deck()
if __name__ == "__main__":
    unittest.main()
