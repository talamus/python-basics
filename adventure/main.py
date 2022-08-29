from Rooms import Rooms         # Import (only) dictionary Rooms from file Rooms.py
from creatures import *         # Import all classes, variables, etc. from file creatures.py (so they can be used without adding "creatures." in front)
from utils import *             # Import all classes, variables, etc. from utils.py (Utilities like "join_neatly" are there now.)

# The Main Program:

player = Player()               # Create a "player" object from the "Player" class

player.location = "red"                                                         # Starting location ("red" is a key in the Rooms dictionary)
describe_room(player.location)                                                  # Use function "describe_room" with "location" attribute of the "player" object

while (True):                                                                   # Just a trick to make this into a loop that runs constantly :D

    movement = input("\nWhere do you want to go? ")                             # Create variable "movement" that takes in the user input

    if (movement in Rooms[player.location]["exits"]):                           # Check if the input string of "movement" matches any values in "exits" of the current "player.location" room
        if (Rooms[player.location]["exits"][movement] == "wasteland"):          # Special case! :P For now...
            print ("\nYou will not survive without water in the Wastleland.")
        else:
            player.location = Rooms[player.location]["exits"][movement]         # Change "player.location" to new room (using string input of movement as key to find the value for new room)
            describe_room(player.location)                                      # Use function "describe_room" with "location" attribute of the "player" object

    else:
        print("You can't go that way")                                          # This is shown if the "movement" was not found as a key in the current room's "exits" dictionary
