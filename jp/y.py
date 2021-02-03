# -*- coding: utf-8 -*-

import os

def nono(string):
    nono = ["------"]
    for i in nono:
        if i in string:
            return True
    return False

cwd = os.getcwd()
if "jp" not in cwd:
    cwd = cwd+"/jp"
def get_subs():

    dir = cwd+"/jani"
    numbers = [0,1,2,3,4,5,6,7,8,9]
    subs = ""
    k = 0
    for path, dirs, files in os.walk(dir):
        for file in files:
            try:
                ending=file.split(".")[-1]
                if ending =="ass":
                    f = open(path+"/"+file, "r", encoding='utf-8', errors='ignore')
                    sub=str(f.read())
                    for i in sub.split("\n"):
                        if "Dialogue" in i:
                            i=i.split(",,")[-1]
                            if not nono(i):
                                subs+=i+" "
                    f.close()
                elif ending=="srt":
                    f = open(path+"/"+file, "r", encoding='utf-8', errors='ignore')
                    sub=str(f.read())
                    for i in sub.split("\n"):
                        isnum = False
                        for a in numbers:
                            if str(a) in i:
                                isnum = True
                        if not isnum and not nono(i):
                            subs+=i+" "
                    f.close()
            except Exception as e:
                print("ee",e)
                print("fail ",path, file)
        k+=1
        print(k)
        if k==15:
            print("brbr")
            break
    f = open(os.getcwd()+"/subs", "w", encoding='utf-8')
    f.write(subs)
    f.close()
get_subs()

# f = open("subss", "r", encoding='utf-8')
# sub=f.read()
# print(sub)
# f.close()
