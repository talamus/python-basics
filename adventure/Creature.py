from math import nan


class Creature:                                # this is the main class, that the other creatures derive stuff from
    name: None
    description: None
    health: nan
    location: None
    inventory: []

    hostile: None


class Dragon(Creature):
    sleeping = True


class Player(Creature):                             # Note: jos class on tyhjä, kirjoita sinne 'pass', muuten tulee virhe :)
    pass

class Rat(Creature):
    hostile = False

class BossRat(Rat):
    hostile = True



