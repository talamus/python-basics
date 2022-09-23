from data import Rooms, player
from program.utils import *


def take(something):
    if something in (Rooms[player.location]["items"]):
        index = Rooms[player.location]["items"].index(something)
        item = Rooms[player.location]["items"].pop(index)
        player.inventory.append(item)

        print("You take", item.the() +".")

    elif something in (Rooms[player.location]["fixtures"]):
        index = Rooms[player.location]["fixtures"].index(something)
        item = Rooms[player.location]["fixtures"][index]
        print("You can't take", item.the() + ".")

    else:
        print("There is no such thing here.")


def drop(something):
    if something in player.inventory:
        index = player.inventory.index(something)
        item = player.inventory[index]
        if item.wearable and item.wearable.worn:                            # katso ensin item.wearable, jos siitä tulee None, lopeta, jos ei, tarkista worn
            print("You have to remove it first.")
            return
        item = player.inventory.pop(index)
        Rooms[player.location]["items"].append(item)
        print("You drop", item.the(), "to the floor.")
    else:
        print("You can't drop what you don't have.")

def wear(something):
    if something in player.inventory:
        index = player.inventory.index(something)
        item = player.inventory[index]

        if item.wearable:
            item.wearable.wear()

def remove(something):
    if something in player.inventory:
        index = player.inventory.index(something)
        item = player.inventory[index]
        if item.wearable:
            item.wearable.remove()

def equip(something):
    if something in player.inventory:
        index = player.inventory.index(something)
        item = player.inventory[index]
        if item.equipable:
            item.equipable.equip()


def unequip(something):
    if something in player.inventory:
        index = player.inventory.index(something)
        item = player.inventory[index]
        if item.equipable.equipped:
            if backpack in player.inventory:
                item.equipable.unequip(item)
                backpack.inventory.append(item)
                print("You unequip it and put it in your backpack.")
            else:
                drop(item)
                print("You don't have any place to store it so you drop it to the floor.")


    elif item.equipable.unequiped:
        print("You have already equipped that.")

def go(direction):
    room = Rooms[player.location]

    if direction not in room["exits"]:
        if ring.wearable.worn and "hidden "+direction in room["exits"]:
            direction = "hidden "+direction

    if direction in room["exits"]:
        if room["exits"][direction] == "wasteland":
            print ("\nYou will not survive without water in the Wastleland.")
        else:
            player.location = room["exits"][direction]
            describe_room(player.location)
    else:
        print("You can't go that way")


def examine(something):
    item = None

    if something in player.inventory:
        index = player.inventory.index(something)
        item = player.inventory[index]

    elif something in Rooms[player.location]["items"]:
        index = Rooms[player.location]["items"].index(something)
        item = Rooms[player.location]["items"][index]

    elif something in Rooms[player.location]["fixtures"]:
        index = Rooms[player.location]["fixtures"].index(something)
        item = Rooms[player.location]["fixtures"][index]


    if item:
        print("It looks very plain.")
    else:
        print("You see no such thing.")



   # print("The", " ".join(item), "looks very complicated.")


def look_around():
    describe_room(player.location)


def inventory():
    if player.inventory:
        print("\nYou are carrying " + join_neatly(map(str, player.inventory))+ " in your pockets.")
    else:
        print("Your only find pocket lint.")


#def reveal():

    # check if item has reveal property then
    # either error message
    # or send stuff to properties to handle
