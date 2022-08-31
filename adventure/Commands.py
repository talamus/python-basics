from operator import inv
from Rooms import Rooms
from creatures import player
from utils import *



def take(item):
    item = " ".join(item)
    if (item in (Rooms[player.location]["items"])):
        player.inventory.append(item)
        Rooms[player.location]["items"].remove(item)
        print("You take the " + item +".")
    else:
        print("There is no such thing here.")


def drop(item):
    item = " ".join(item)

    if (item in player.inventory):
        player.inventory.remove(item)
        Rooms[player.location]["items"].append(item)
        print("You drop the " + item +" to the floor.")
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
        print("\nYou are carrying " + join_neatly( map(add_an_article, player.inventory) ) + " in your pockets.")
    else: print("Your only find pocket lint.") 