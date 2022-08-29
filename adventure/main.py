from Rooms import Rooms                                 # import dictionary Rooms from file Rooms.py
from Creature import *                                  # import all classes, variables, etc. from Creature.py (so they can be used without adding Creature. in front)
from utils import *                                     # import all classes, variables, etc. from utils.py (like join_neatly is there now)


# The Main Program:

player = Player()

player.location = "red"                                                         # starting location ("red" is found from the list of keys that is made automatically)
describe_room(player.location)                                                  # use function describe_room with parameter 'player_location'

while (True):                                                                   # just a trick to make this into a loop that runs constantly :D

    movement = input("\nWhere do you want to go? ")

    if (movement in Rooms[player.location]["exits"]):                           # check if the input string of 'movement' matches any values in exits of the room
        if (Rooms[player.location]["exits"][movement] == "wasteland"):
            print ("\nYou will not survive without water in the Wastleland.")
        else:
            player.location = Rooms[player.location]["exits"][movement]         # change player_location to new room (using string input of movement as key to find the value for new room)  
            describe_room(player.location)                                      # use function describe_room with parameter 'player_location'

    else:
        print("You can't go that way")
