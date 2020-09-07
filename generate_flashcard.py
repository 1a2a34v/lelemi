import re

def generate_flashcard(word, values):
    # if values.get("count",None) and values.get("wadoku",None) and values.get("tatoeba",None):
    # frontside = "<b>{}</b>, 回数: {}".format(word,values["count"])
    frontside = "<b>{}</b>, {}, domain-frequency: {}".format(word,values["wtype"],values["count"])
    assert values.get("count",None)

    #reverseside='<h3 style="background-color:DodgerBlue;">類語-翻訳:</h3>\n'
    reverseside=""

    if values.get("wordref",None):
        if reverseside == "":
            reverseside+='<h3 style="background-color:DodgerBlue;">sentence-translations:</h3>\n'
        i=0
        for wd in values["wordref"]:
            # re.sub(r'0x\w{2}', '',s)
            if i<6:
                reverseside+="{}<hr/>".format(wd)
            i+=1

    if values.get("wadoku",None):
        if reverseside == "":
            reverseside+='<h3 style="background-color:DodgerBlue;">単語翻訳:</h3>\n'
        i=0
        for wd in values["wadoku"]:
            # re.sub(r'0x\w{2}', '',s)
            if i<6 and not wd["np"] in reverseside and "xa0" not in wd["de"]:
                reverseside+="{} --- {}<hr/>".format(wd["de"],wd["np"])
                i+=1

    if values.get("tatoeba",None):
        if values.get("wadoku",None):
            reverseside+='\n\n<h3 style="background-color:Tomato;">例文翻訳:</h3>\n'
        else:
            reverseside+='\n\n<h3 style="background-color:Tomato;">use in sentences:</h3>\n'
        i=0
        print(values["tatoeba"])
        for tt in values["tatoeba"]:
            # if i<5:
            # gerstr = tt["de"]
            # regex = re.compile(r'(\b({}))'.format(word), re.IGNORECASE)
            # regex.sub(r'<u style="background-color:Tomato;">\1</u>', gerstr)
            reverseside+="{}<br><br>{}<hr/>".format(tt["de"],tt["np"])
            i+=1
    else:
        return None

    return {"front":frontside, "back":reverseside}
    # else:
    #     print(word)
    #     print(values.get("count",None))
    #     print(values.get("wadoku",None))
    #     print(values.get("tatoeba",None))
    #     return None
