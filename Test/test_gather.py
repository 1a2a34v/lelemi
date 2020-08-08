# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import gather
import unittest
import pickle
from unittest import mock
import import_source
import create_flashcards
#
# @patch.object(requests, 'get')
# def test_service_post(mock_request_post):
#     data = {'number': 0000, 'user_id': 0, 'name': 'john'}
class TestAT(unittest.TestCase):
    def test_gather_wordref_deen(self):
        domain = "de"
        native = "en"
        seq = "verweigern"
        name = "mimimi"
        converted_sequence = import_source.SequenceConverter(seq,name,domain,native)
        converted_sequence.generate_wordlist()
        print(converted_sequence.words)
        converted_sequence.retrieve_wordinfo()
        anki = create_flashcards.DeckGenerator(name,converted_sequence.words)
        #anki.load_pickle()
        anki.generate_deck()


        #wiederda_anki.generate_deck()
if __name__ == "__main__":
    unittest.main()
