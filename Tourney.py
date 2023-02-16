import API_Extraction as api

cards=[]
with open("Tourney.txt") as F:
    player=F.readline().split()
    cards.append(api.cardList(player))
#print(api.cardList("#22VVQLYLV"))
print(api.cardList("#YCRYQV8"))