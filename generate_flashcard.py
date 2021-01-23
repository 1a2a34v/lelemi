import re

def generate_flashcard(word, values):
    if values.get("wadoku",None):
        frontside = "<b>{}</b>, 回数: {}".format(word,values["count"])
    else:
        frontside = "<b>{}</b>, {}, domain-frequency: {}\n".format(word,values["wtype"],values["count"])
    assert values.get("count",None)
    reverseside=""

    # if "picture" in values.keys():
    #     from PIL import Image
    #     img = Image.new("RGB", (800, 1280), (255, 255, 255))
    #     path = "/Users/mieko/Library/Application Support/Anki2/User 1/collection.media/{}.png".format(word)
    #     img.save(path, "PNG")
    #     loc  = "file://storage/emulated/0/AnkiDroid/media/{}.png".format(word)
    #     reverseside+='<p><a href="{}"><img src="{}.png" width="350" height="450"></a></p>'.format(loc,word)

    if values.get("jisho",None):
        if reverseside == "":
            reverseside+='<h3 style="background-color:DodgerBlue;">単語翻訳:</h3>\n'
        i=0
        for j in values["jisho"]:
            # re.sub(r'0x\w{2}', '',s)
            if i<6 and not j["jp"] in reverseside and "xa0" not in j["en"]:
                reverseside+="{} --- {}<hr/>".format(j["en"],j["jp"])
                i+=1

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

    if values.get("krdict",None):
        frontside+="<br>{}".format(values.get("romanization"))

        if reverseside == "":
            reverseside+='<h3 style="background-color:DodgerBlue;">KRdict result:</h3>\n'
        i=0
        for a in values["krdict"]:
            for key,v in a.items():
                    reverseside+="<b>{}:</b><br>".format(key)
                    i=1
                    for c in v:
                        reverseside+="{}: {}<br>".format(i,c["translation"])
                        reverseside+='<font color="red">{}</font><br>'.format(c["koreanex"])
                        reverseside+='<font color="blue">{}</font><br>'.format(c["engex"])
                        reverseside+='<font color="yellow">{}</font><br>'.format(c["romanization"])

    if values.get("tatoeba",None):
        if values.get("wadoku",None):
            reverseside+='\n\n<h3 style="background-color:Tomato;">例文翻訳:</h3>\n'
        else:
            reverseside+='\n\n<h3 style="background-color:Tomato;">use in sentences:</h3>\n'
        i=0
        for tt in values["tatoeba"]:
            reverseside+="{}<br><br>{}<hr/>".format(tt["de"],tt["np"])
            i+=1
            
    return {"front":frontside, "back":reverseside}
