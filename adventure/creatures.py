from math import nan            # "nan" is a numeric 'nothing' value that Tero wanted to use...

class Creature:                 # This is the main class, that the other creatures derive stuff from
    name: None
    description: None
    health: nan                 # Health is a number!
    location: None
    inventory: []

    hostile: None

class Dragon(Creature):
    sleeping = True

class Player(Creature):
    pass                        # Note: if class is empty, you have to add "pass". Otherwise you get an error! :P

class Rat(Creature):
    hostile = False             # Good rat

class BossRat(Rat):
    hostile = True              # Bad rat!!!
