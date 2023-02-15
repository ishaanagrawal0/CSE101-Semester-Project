import random
import API_Extraction as api

allCards = ['Royal Giant', 'Minions', 'Ram Rider', 'Royal Hogs', 'Rascals', 'Archer Queen', 'Royal Recruits', 'Goblins', 'Golem', 'Three Musketeers', 'Archers', 'X-Bow', 'Mother Witch', 'Spear Goblins', 'Barbarians', 'Skeleton Dragons', 'Lava Hound', 'Wall Breakers', 'Goblin Drill', 'Prince', 'Mortar', 'Bomber', 'Barbarian Hut', 'Hunter', 'Dart Goblin', 'Guards', 'Mini P.E.K.K.A', 'Furnace', 'Goblin Hut', 'Witch', 'Mega Minion', 'Skeleton Army', 'Giant', 'Goblin Cage', 'Ice Wizard', 'Dark Prince', 'Heal Spirit', 'Skeleton Barrel', 'Poison', 'Ice Spirit', 'Arrows', 'Goblin Gang', 'Giant Skeleton', 'Flying Machine', 'Clone', 'Fisherman', 'Zappies', 'Night Witch', 'Battle Ram', 'Fire Spirit', 'Mighty Miner', 'Inferno Tower', 'Earthquake', 'Princess', 'Electro Giant', 'Lightning', 'Skeleton King', 'Executioner', 'Electro Spirit', 'Cannon Cart', 'Tombstone', 'Wizard', 'Sparky', 'Goblin Barrel', 'Battle Healer', 'Valkyrie', 'Golden Knight', 'Bats', 'Elite Barbarians', 'Elixir Golem', 'Knight', 'Hog Rider', 'Mega Knight', 'Elixir Collector', 'Cannon', 'Minion Horde', 'Goblin Giant', 'Tesla', 'The Log', 'Mirror', 'Graveyard', 'Baby Dragon', 'Royal Delivery', 'Bowler', 'P.E.K.K.A', 'Magic Archer', 'Fireball', 'Zap', 'Royal Ghost', 'Bandit', 'Phoenix', 'Electro Wizard', 'Firecracker', 'Rocket', 'Freeze', 'Electro Dragon', 'Lumberjack', 'Inferno Dragon', 'Rage', 'Tornado', 'Musketeer', 'Bomb Tower', 'Barbarian Barrel', 'Miner', 'Ice Golem', 'Giant Snowball', 'Balloon', 'Skeletons', 'Monk']

win_conditions = [ 'Mortar', 'Goblin Barrel', 'Battle Ram', 'Goblin Giant', 'X-Bow', 'Royal Giant', 'Ram Rider', 'Royal Hogs', 'Three Musketeers', 'Golem', 'Lava Hound', 'Wall Breakers', 'Goblin Drill', 'Prince', 'Giant', 'Skeleton Barrel', 'Night Witch', 'Mighty Miner', 'Electro Giant', 'Skeleton King', 'Sparky', 'Elite Barbarians', 'Hog Rider', 'Mega Knight', 'Elixir Golem', 'P.E.K.K.A', 'Balloon', 'Graveyard']

spells = ['Giant Snowball', 'Mirror', 'The Log', 'Poison', 'Arrows', 'Clone', 'Lightning', 'Rocket', 'Freeze', 'Fireball', 'Zap', 'Royal Delivery', 'Earthquake', 'Rage', 'Tornado']

air_hitting = ['Hunter', 'Wizard', 'Princess', 'Executioner', 'Archers', 'Dart Goblin', 'Archer Queen', 'Mother Witch', 'Minions', 'Spear Goblins', 'Skeleton Dragons', 'Mega Minion', 'Baby Dragon', 'Magic Archer', 'Firecracker', 'Electro Dragon', 'Inferno Dragon', 'Ice Wizard', 'Flying Machine', 'Zappies', 'Bats', 'Minion Horde', 'Phoenix', 'Electro Wizard', 'Musketeer']

buildings = ['Goblin Hut', 'Barbarian Hut', 'Inferno Tower', 'Cannon', 'Tombstone', 'Tesla', 'Bomb Tower', 'Furnace', 'Elixir Collector']

support = ['Rascals', 'Royal Recruits', 'Goblins', 'Guards', 'Mini P.E.K.K.A', 'Witch', 'Skeleton Army', 'Goblin Cage', 'Dark Prince', 'Heal Spirit', 'Ice Spirit', 'Goblin Gang', 'Giant Skeleton', 'Fisherman', 'Fire Spirit', 'Electro Spirit', 'Cannon Cart', 'Battle Healer', 'Valkyrie', 'Golden Knight', 'Bowler', 'Bandit', 'Barbarian Barrel', 'Miner', 'Ice Golem', 'Skeletons', 'Monk', 'Barbarians', 'Bomber', 'Knight', 'Royal Ghost', 'Lumberjack']

cardImageDict = api.cardImage()

def randomDeck():
    deck = []
    cardImage = []

    win_conditions = ['Goblin Barrel', 'Battle Ram', 'Goblin Giant', 'X-Bow', 'Royal Giant', 'Ram Rider', 'Royal Hogs', 'Three Musketeers', 'Golem', 'Lava Hound', 'Wall Breakers', 'Goblin Drill', 'Prince', 'Giant', 'Skeleton Barrel', 'Night Witch', 'Mighty Miner', 'Electro Giant', 'Skeleton King', 'Sparky', 'Elite Barbarians', 'Hog Rider', 'Mega Knight', 'Elixir Golem', 'P.E.K.K.A', 'Balloon', 'Graveyard']

    spells = ['Giant Snowball', 'Mirror', 'The Log', 'Poison', 'Arrows', 'Clone', 'Lightning', 'Rocket', 'Freeze', 'Fireball', 'Zap', 'Royal Delivery', 'Earthquake', 'Rage', 'Tornado']

    air_hitting = ['Hunter', 'Wizard', 'Princess', 'Executioner', 'Archers', 'Dart Goblin', 'Archer Queen', 'Mother Witch', 'Minions', 'Spear Goblins', 'Skeleton Dragons', 'Mega Minion', 'Baby Dragon', 'Magic Archer', 'Firecracker', 'Electro Dragon', 'Inferno Dragon', 'Ice Wizard', 'Flying Machine', 'Zappies', 'Bats', 'Minion Horde', 'Phoenix', 'Electro Wizard', 'Musketeer']

    buildings = ['Goblin Hut', 'Barbarian Hut', 'Mortar', 'Inferno Tower', 'Cannon', 'Tombstone', 'Tesla', 'Bomb Tower', 'Furnace', 'Elixir Collector']

    support = ['Rascals', 'Royal Recruits', 'Goblins', 'Guards', 'Mini P.E.K.K.A', 'Witch', 'Skeleton Army', 'Goblin Cage', 'Dark Prince', 'Heal Spirit', 'Ice Spirit', 'Goblin Gang', 'Giant Skeleton', 'Fisherman', 'Fire Spirit', 'Electro Spirit', 'Cannon Cart', 'Battle Healer', 'Valkyrie', 'Golden Knight', 'Bowler', 'Bandit', 'Barbarian Barrel', 'Miner', 'Ice Golem', 'Skeletons', 'Monk', 'Barbarians', 'Bomber', 'Knight', 'Royal Ghost', 'Lumberjack']

    champions = ['Archer Queen', 'Skeleton King', 'Golden Knight', 'Mighty Miner', 'Monk']
    
    x = random.choice(win_conditions)
    win_conditions.remove(x)
    allCards.remove(x)
    deck.append(x)

    x = random.choice(win_conditions)
    win_conditions.remove(x)
    allCards.remove(x)
    deck.append(x)

    x = random.choice(spells)
    spells.remove(x)
    allCards.remove(x)
    deck.append(x)

    x = random.choice(spells)
    spells.remove(x)
    allCards.remove(x)
    deck.append(x)

    x = random.choice(air_hitting)
    air_hitting.remove(x)
    allCards.remove(x)
    deck.append(x)

    x = random.choice(buildings)
    buildings.remove(x)
    allCards.remove(x)
    deck.append(x)

    x = random.choice(support)
    support.remove(x)
    allCards.remove(x)
    deck.append(x)

    x = random.choice(allCards)
    allCards.remove(x)
    deck.append(x)

    for i in deck:
        cardImage.append(cardImageDict[i])


    counter = 0
    for i in deck:
        if i in champions:
            counter += 1
    if counter > 1:
        randomDeck()
    else:
        return deck, cardImage

print(randomDeck())