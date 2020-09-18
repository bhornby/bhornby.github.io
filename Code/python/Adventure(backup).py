
from dataclasses import dataclass

import random

@dataclass

class Item:
    '''Class to represent an item.'''
    desc: str
    actions: []

@dataclass

class Room:
    '''Class to represent a room or locaion.'''
    desc: str
    contents: {}


# contents

bogbrush = Item (desc="No toothpaste please", actions=["brandish"])

tv = Item (desc="Gogglebox", actions=["cry"])

eclaire = Item (desc="mmmm cream slice", actions=["watch"])


#rooms

hall = Room (desc="A light and airy hall", contents={})

toilet = Room (desc="Phew!", contents={})

study = Room (desc="A shrine to achievement", contents={})

secretpassage = Room (desc="A tunnel to nextdoor", contents={})

living = Room (desc="A place of relaxation", contents={"bogbrush":bogbrush})

chimney = Room (desc="Pigeon's resting place", contents={})

kitchen = Room (desc="the palace of the enlightened eclaire", contents={"eclaire":eclaire})

rooms = [
    [ None, hall, study, secretpassage, ],
    [ toilet, hall, living, chimney ],
    [ None, kitchen, living],
    # [ basement, ]
    # [ garden, ]
]
nolocation="You can't go that way"

x = 1
y = 0
inventory = {}
while True:
    print(rooms[y][x].desc)
    cmd = input("\n> ")
    if cmd == "exit":
        break
    if cmd == "help":
        print("Type exit to exit,  and then look at the code!")
    elif cmd == "look":
        for k,v in rooms[y][x].contents.items():
            print("{}, {}".format(k, v.desc))
    elif cmd == "inv":
        print(inventory)
    elif cmd.startswith("take "):
        verb, itemname = cmd.split(" ")
        if itemname in rooms[y][x].contents:
            inventory[itemname] = rooms[y][x].contents[itemname]
            del rooms[y][x].contents[itemname]
    elif cmd == "n":
        if y - 1 >= 0 and rooms[y-1][x] is not None:
            y = y - 1
        else:
            print(nolocation)
    elif cmd == "s":
        if y + 1 < len(rooms) and rooms[y+1][x] is not None:
            y = y + 1
        else:
            print(nolocation)
    elif cmd == "e":
        if x + 1 < len(rooms[y]) and rooms[y][x+1] is not None:
            x = x + 1
        else:
            print(nolocation)
    elif cmd == "w":
        if x - 1 >= 0 and rooms[y][x-1] is not None:
            x = x - 1
        else:
            print(nolocation)
    else:
        verb, itemname = cmd.split(" ")
        if itemname in inventory:
            if verb in inventory[itemname].actions:
                print("You {} the {} valiantly!".format(verb, itemname))
            else:
                if random.randint(0,10)>5:
                    print("You can't {} the {}".format(verb, itemname))
                else: 
                    print("You don't want to {} the {}".format(verb, itemname))
        else:
            print("You don't have a {}".format(itemname))




