from adventure.program.classes.entity import Item, Fixture
from program.classes.properties import *

apple = Item("an apple"

#  messages={
#     "examine": "It's a Granny Smith.",
#     "eat": "You eat the apple. It's crisp, the flesh is hard, and it has a very sharp taste.",
#}

)

ring = Item(" a golden ring", Wearable)

sword = Item("an iron sword", Equipable, Iron)

backpack = Item("a trusty old backpack", Equipable, Wearable, Inventory, inventory = [])