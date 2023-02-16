import urllib.request
import json

def get_data(player_tag):
    with open("my_key.txt", "r") as f:
        my_key = f.read().rstrip("\n")

    base_url = "https://api.clashroyale.com/v1"
        
    endpoint = f"/players/%23{player_tag[1:]}"

    request = urllib.request.Request(
                        base_url+endpoint,
                        None,
                        {
                            "Authorization": "Bearer %s" % my_key
                        }
                )
    response = urllib.request.urlopen(request).read().decode("utf-8")

    return json.loads(response)

def player_stats(player_tag):
    
    return get_data(player_tag)

def cardList(player_tag):
    
        data=get_data(player_tag)
        levels={}
        
        i = 0
        while True:
            try:
                x = data["cards"][i]["maxLevel"]
                if x==6:
                    levels[data["cards"][i]["name"]] = data["cards"][i]["level"] + 8
                elif x==4:
                    levels[data["cards"][i]["name"]] = data["cards"][i]["level"] + 10
                elif x==9:
                    levels[data["cards"][i]["name"]] = data["cards"][i]["level"] + 5
                elif x==12:
                    levels[data["cards"][i]["name"]] = data["cards"][i]["level"] + 2
                else:
                    levels[data["cards"][i]["name"]] = data["cards"][i]["level"]

                i += 1
            except:
                return levels
            #print(data["cards"]["level"])
            #print("Name: %s\nTrophies: %d\nArena: %s\nTag: %s\n\n" % (item["name"], item["trophies"], item["arena"], item["tag"]))
    
def cardImage():

    with open("my_key.txt", "r") as f:
        my_key = f.read().rstrip("\n")

        base_url = "https://api.clashroyale.com/v1/cards"

        request = urllib.request.Request(
                        base_url,
                        None,
                        {
                            "Authorization": "Bearer %s" % my_key
                        }
                )
        response = urllib.request.urlopen(request).read().decode("utf-8")

        data = json.loads(response)
        
        x = data["items"]
        cardIcons = {}
        for i in x:
            tempName = i['name']
            tempPNG = i['iconUrls']['medium']
            cardIcons[tempName] = tempPNG
        return cardIcons

def clan_members(clan_tag):

    with open("my_key.txt", "r") as f:
        my_key = f.read().rstrip("\n")

        base_url = "https://api.clashroyale.com/v1"

        endpoint = f"/clans/%23{clan_tag[1:]}/members"

        request = urllib.request.Request(
                        base_url+endpoint,
                        None,
                        {
                            "Authorization": "Bearer %s" % my_key
                        }
                )
        response = urllib.request.urlopen(request).read().decode("utf-8")
        response = eval(response)
        x = response["items"] #x is a list
        newDict = {}
        for i in x:
            newDict[i["tag"]] = i["name"]        
        return newDict

if __name__=="__main__":
    print(cardList("#YCRYQV8"))
    print(cardImage())
    print(player_stats("#YCRYQV8"))
