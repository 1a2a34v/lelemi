from konlpy.tag import Okt
import spacy
import textwrap
import unicodedata
spacymacy = {
 "jp":'ja_core_news_sm'
}

lu ={
    "Ã¤":"ä",
    "Ã¼":"ü",
    "Ã¶":"ö",
    "ÃŸ":"ß"
}
numbers = [1,2,3,4,5,6,7,8,9,0]

def parse(wordsequence,domain):
    words = {}

    if domain == "ko":
        okt = Okt()
        pos = okt.pos(wordsequence)
        words = {}
        for i in pos:
            if i[1]!="Alpha" and i[1]!="Foreign":
                if i[0] not in words.keys():
                    words[i[0]] = {
                        "count":1,
                        "wtype":i[1]
                    }
                else:
                    words[i[0]]["count"]+=1
                try:
                    words[i[0]]["romanization"] = Romanizer(i[0]).romanize()
                except:
                    words[i[0]]["romanization"] = "Romaerror"
    else:
        if domain in spacymacy.keys():
            nlp = spacy.load(spacymacy[domain])
        else:
            nlp = spacy.load(domain)
        seq_raw = wordsequence
        if len(seq_raw)>1000000:
            nlps = []
            for i in textwrap.wrap(seq_raw, 900000):
                nlps.append(1)
                print(i)
            print(len(nlps))
            nlps = []
            for i in textwrap.wrap(seq_raw, 900000):
                nlps.append(nlp(i))
        else:
            nlps = [nlp(wordsequence)]
        words = {}
        for wordsequence in nlps:
            for w in wordsequence:
                word = w.lemma_
                for i,val in lu.items():
                    if i in str(word):
                        word = str(word).replace(i,val)
                isnum = False
                for i in numbers:
                    if str(i) in word:
                        isnum = True
                haskanj = True
                if domain=="jp":
                    haskanj = False
                    line = ""
                    for a in str(word):
                        try:
                            print([a])
                            nam = unicodedata.name(a)
                            if "CJK UNIFIED" in nam:
                                haskanj = True
                            line+=a
                        except:
                            pass
                    word = line
                if (w.pos_=="NOUN" or w.pos_=="AUX"  or w.pos_=="VERB" or w.pos_=="ADV" or w.pos_=="ADJ") and not isnum and haskanj:
                    print(word)
                    if word in words:
                        words[word]["count"]+=1
                    else:
                        words[word]={"count":1,"wtype":w.pos_}
    return words
