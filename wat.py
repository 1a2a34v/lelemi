# import unicodedata
#
# for i in "いざ参る！":
#     print(unicodedata.name(i))


import spacy
a="いざ参る！"
b="参参参"

nlp = spacy.load('ja_core_news_sm')

a = nlp(a)
b = nlp(b)

c = a.merge(b)
# aa = """차가우니까"""
# #frontside contexts with respective songnames
# #make all selectable, allow html modification for desired examples and translations
# #allow for selfcreated drawings as mnemonic
# #also create big list of images (low space?) and let user select
# #order all preselected info nicely at the top part of the backside from then on
#
#
# o="""걷고 싶어 아무 상관없이 시선"""
# p = """
# 부끄러운지도 모르는 어릴 때로 돌아가서
# 집 없이 살고 싶어 온 세계를 누비며
# 두 눈에 담은 것도 없이 방에 갇혀있긴 싫어
# 얼룩말을 타고 달려
# 횡단보도 건너 hands up, yeah, yeah
# 하고싶은 대로 yeah, yeah
# 물웅덩이 위로 굴러
# 담벼락을 넘어 jump up, yeah, yeah
# 숨 쉬는 것 freedom
# 날 보는 것 freedom
# 날 사랑하는 것 free 알아가는 것 freedom
# 노래 하는 것 freedom
# 춤 추는 것 freedom
# 내 편이 되는 것 free, I'm just so free
# 길 없이 걷고싶어 잠자리를 따라서
# 나의 발자국이 그 곳에 처음 찍히도록
# 돈 없이 살고 싶어 온 세상을 가지며
# 시대를 맞이하기 위해 두 손을 비우고 싶어
# 저질러 네가 타고난 걸
# 높이 두 팔 벌려 hands up, yeah
# 하고 싶은대로 yeah, yeah
# 꽉 막힌 친구들 다 불러
# 바 바 바깥바람 좀 쐬여 yeah, yeah
# 숨 쉬는 것 freedom
# 날 보는 것 freedom
# 날 사랑하는 것 free 알아가는 것 freedom
# 노래 하는 것 freedom
# 춤 추는 것 freedom
# 내 편이 되는 것 free, I'm just so free
# 꿈 꾸는 것 freedom
# 푹 자는 것 freedom
# Oh, 기부하는 것 free 안하는 것 freedom
# 투표 하는 것 freedom
# 표현하는 것 freedom
# 내 팬이 되는 것 free, I'm just so free"""
#
# from konlpy.tag import Okt
# okt = Okt()
# pos = okt.pos(p)
# words = {}
# for i in pos:
#     if i[1]!="Alpha" and i[1]!="Foreign":
#         if i[0] not in words.keys():
#             words[i[0]] = {
#                 "counter":1,
#                 "wtype":i[1]
#             }
#         else:
#             words[i[0]]["counter"]+=1
# print(words)
