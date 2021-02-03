# -*- coding: utf-8 -*-
import import_source
import create_flashcards
import pickle
import os

# directory = "gotsubs"
# seq = ""
# domain = "en"
# native = "de"
# name = "game"
# directory = "mimiddle"
# seq = ""
# domain = "en"
# native = "jp"
# name = "mimiddle"
# minimum_frequency = 1
# directory = "AKMU"
# words = ""
# native = "en"
# domain = "ko"
# name = "akmuakmu"
# minimum_frequency = 1
directory = "jp"
words = ""
native = "de"
domain = "jp"
name = "ajp"
minimum_frequency = 1

for filename in os.listdir("sources/"+directory):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = os.path.join("sources/",directory, filename)
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, 'r', errors='ignore') as seq:
        words+=seq.read()

converted_sequence = import_source.Flashcard_Collection(words,name,domain,native,minimum_frequency)
converted_sequence.retrieve_wordinfo()
anki = create_flashcards.DeckGenerator(name,converted_sequence.words)
#anki.load_pickle()
anki.generate_deck()
