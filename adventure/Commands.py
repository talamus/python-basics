from Rooms import Rooms
from creatures import player
from utils import *


def take(something):
    if (something in (Rooms[player.location]["items"])):
        index = Rooms[player.location]["items"].index(something)
        item = Rooms[player.location]["items"].pop(index)
        player.inventory.append(item)

        print("You take", item.the() +".")
    
    elif (something in (Rooms[player.location]["fixtures"])):
        index = Rooms[player.location]["fixtures"].index(something)
        item = Rooms[player.location]["fixtures"][index]
        print("You can't take", item.the() + ".")
    
    else:
        print("There is no such thing here.")


def drop(something):
    if (something in player.inventory):
        index = player.inventory.index(something)
        item = player.inventory.pop(index)
        Rooms[player.location]["items"].append(item)
        print("You drop", item.the(), "to the floor.")
    else:
        print("You can't drop what you don't have.")


def go(direction):
    room = Rooms[player.location]
    if direction in room["exits"]:
        if (room["exits"][direction] == "wasteland"):         
            print ("\nYou will not survive without water in the Wastleland.")
        else:
            player.location = room["exits"][direction]         
            describe_room(player.location)                                      
    else: 
        print("You can't go that way") 


def examine(item):
    print("The", " ".join(item), "looks very complicated.")


def look_around():
    describe_room(player.location)


def inventory():
    if player.inventory:
        print("\nYou are carrying " + join_neatly(map(str, player.inventory))+ " in your pockets.")
    else:
        print("Your only find pocket lint.")
