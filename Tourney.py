import API_Extraction as api

maxTrophies=7500

#(3 crown wins)*3 /battle count* (win percentage/100 +best trophies/max trophies)
def formulae(threeCrownWins,battleCount,win_percentage,bestTrophies):
    global maxTrophies
    return threeCrownWins*3/battleCount * (win_percentage/100+bestTrophies/maxTrophies)

def info(player_tag):
    stats=api.get_data(player_tag)
    info={"threeCrownwins":stats["threeCrownWins"],"battleCount":stats["battleCount"],"win_percentage":stats["wins"]/(stats["wins"]+stats["losses"]),"bestTrophies":stats["battleCount"]}
     
    return info

bracket={}
clan=api.clan_members("#GRY2LP8P")

for i in clan:
    unpack=list(info(i).values())
    bracket.update({clan[i]:formulae(unpack[0],unpack[1],unpack[2],unpack[3])})

extraction=list(bracket.items())
extraction.sort(key=lambda x:x[1])

j=0
while j<len(extraction):
    print(api.get_data(extraction[j][1])['name']+"paired with"+api.get_data(extraction[j+1][1])["name"])
    
    j+=2