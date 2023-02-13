import urllib.request
import json
import random

with open("my_key.txt", "r") as f:
    my_key = f.read().rstrip("\n")

    base_url = "https://api.clashroyale.com/v1"

    player_tag = "#22VVQLYLV"

    endpoint = f"/players/%23{player_tag[1:]}"

    request = urllib.request.Request(
                    base_url+endpoint,
                    None,
                    {
                        "Authorization": "Bearer %s" % my_key
                    }
            )
    response = urllib.request.urlopen(request).read().decode("utf-8")

    data = json.loads(response)
    i = 0
    while True:
        print(data["cards"][i]["name"], end = ": ")
        x = data["cards"][i]["maxLevel"]
        if x==6:
            print(data["cards"][i]["level"] + 8)
        elif x==4:
            print(data["cards"][i]["level"] + 10)
        elif x==9:
            print(data["cards"][i]["level"] + 5)
        elif x==12:
            print(data["cards"][i]["level"] + 2)
        else:
            print(data["cards"][i]["level"])
        i += 1
        #print(data["cards"]["level"])
        #print("Name: %s\nTrophies: %d\nArena: %s\nTag: %s\n\n" % (item["name"], item["trophies"], item["arena"], item["tag"]))