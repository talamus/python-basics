import program
from data import player

def main():                                     # The Main Program:

    program.describe_room(player.location)      # Use function "describe_room" with "location" attribute of the "player" object

    while True:                                 # Just a trick to make this into a loop that runs constantly :D
        command = input("\nWhat next? ")        # take input as command
        program.parse(command.lower())          # send input string to parser
