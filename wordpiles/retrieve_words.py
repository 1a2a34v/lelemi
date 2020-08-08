import spacy
with open("gerb1","r") as f:
    d = f.read()

d = d.split("VS_03")

wordlist = []
receivingwords = False
for page in d:
    receivingwords = True
    lines = page.split("\n")
    i=0
    while receivingwords:
        if not len(lines[i])==0:
            print(lines[i])
            word = lines[i]
            if "," in word:
                word = word.split(",")[0]

            wordlist.append(word)

            # if not len()=1
            # word = i
            # if "," in i:
            #     word = i.split(",")
            # print(i)
            # print("k")
            if lines[i][0]=="1" or ("." in lines[i] and not ".)" in lines[i]):
                receivingwords = False
        i+=1

def filter(word):
    #regrets are deadly
    a = len(word)==1


words = ""
#wordlist = ["irgendirgendein"]
for i in wordlist:
    words+=i+" "
nlp=spacy.load('de')
bob=nlp(words)
k=[]
for w in bob:
    print(w.pos_)
    if (w.pos_=="NOUN" or w.pos_=="AUX"  or w.pos_=="VERB" or w.pos_=="ADV") and w.lemma_ not in k:
        k.append(w.lemma_)
seq = ""
for word in k:
    seq+=word+" "

with open("gerb1_wordslist.txt","w") as f:
    # f.write(str(wordlist))
    f.write(seq)
