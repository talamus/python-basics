from Rooms import Rooms         # Import (only) dictionary Rooms from file Rooms.py
from creatures import *         # Import all classes, variables, etc. from file creatures.py (so they can be used without adding "creatures." in front)
from utils import *             # Import all classes, variables, etc. from utils.py (Utilities like "join_neatly" are there now.)
import Commands
from parser import parse

# The Main Program:

describe_room(player.location)                                                  # Use function "describe_room" with "location" attribute of the "player" object

while (True):                                                                   # Just a trick to make this into a loop that runs constantly :D
    command = input("\nWhat next? ")                                            # take input as command
    parse(command)                                                              # send input string to parser
 