Control Flow:
    main.py is filled with information about domain language, target language and target directory
    main.py is called and uses the import_source.py module to create a Flashcard_Collection object with the provided parameters
    import_source.py iterates over every word in the target folder, normalizes it and counts each occurence in the Flashcard_Collection __init__ function
    main.py calls import_source.retrieve_wordinfo() on the created object to initiate the download of translation information and example sentences using the gather.py module    
    main.py calls the create_flashcards.py module with the dictionary containing our information
    create_flashcards.py iterates over every word and uses the create_flashcard.py module to create a flashcard for each word with a generic html front and backside
    create_flashcards.py creates an anki deck and saves it in the ankidecks directory
    
Improvements:
    find way to dynamically generate decks, pass info and desired decks to be created via external file
    input json file for automated dekgeneration,skip those that are already present in ankidecksfolder/picklefolder
    Better management of different lemmatizers for different languages (spacy, konlpy)
    use nltk corpus for global frequency and for sorting of non domain related media
    create corpus directory with subdirectories en de jp etc. for sorting language leaerning vocabulary hierarchy (lowprio)
    always preemptively look for present pickle data and see if data can be appended, maybe inlcude overwrite option in json?
