from program.classes.creatures import Player
from data.rooms import Rooms
from data.items import backpack

player = Player()               # Create a "player" object from the "Player" class
player.location = "red"
player.inventory = [backpack]