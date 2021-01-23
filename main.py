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
directory = "AKMU"
seq = ""
native = "en"
domain = "ko"
name = "akmuakmu"
minimum_frequency = 1

for filename in os.listdir(directory):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = os.path.join("sources/",directory, filename)
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, 'r', errors='ignore') as :
        seq+=sub.read()

converted_sequence = import_source.Flashcard_Collection(seq,name,domain,native,minimum_frequency)
converted_sequence.retrieve_wordinfo()
anki = create_flashcards.DeckGenerator(name,converted_sequence.words)
anki.generate_deck()
