class Property:
    pass

#--------------- erikoisluokka ---------------

class SwitchProperty(Property):
    default = True                                      # switch state class
    def __init__(self, state=default):                     # def__init__ ottaa sisään self, ja state joka defaulttina True
        self.state = state                              # tallennetaan state muuttujaan self.state (eli alustetaan se tilaan True tässä kohtaa)
    def set(self, state):                               # def set (funktio) joka syö self, state, tämä muuttaa tilaa state (True tai False)
        self.state = state                              # tallenetaan state muuttujaan self.state
    def __bool__(self):                                 # def __bool__ funktio, palauttaa self.state joka on totuusarvo True/False
        return self.state                               # (tämä on joskus hyvin käytännöllistä :D)



#--------------- käyttöluokat ---------------


class Wearable(Property):
    def __init__(self, worn=False):
        self.worn = worn

    def wear(self):                                     # 'wear' on objektin metodi!!! usage: object.wear (object kohtaan objektin nimi)
        if self.worn:
            print("You are already wearing it.")
        else:
            self.worn = True
            print("You put the thing on.")

    def remove(self):
        if self.worn:
            self.worn = False
            print("You take the thing off.")
        else:
            print("You are not wearing it.")


class Equipable(Property):
    def __init__(self, equipped=True):
        self.equipped = equipped

    def equip(self):                                     # 'wear' on objektin metodi!!! usage: object.wear (object kohtaan objektin nimi)
        if self.equipped:
            print("It is already equipped.")
        else:
            self.equipped = True
            print("You equip yourself with it.")

    def unequip(self):
        if self.equipped:
            self.worn = False
            print("You unequip it.")
        else:
            print("You have not equipped it.")


class Inventory(Property):
    def __init__(self, inventory):
        self.inventory = inventory

class Container(Property):
    def __init__(self, content = None):
        self.content = content


class Metallic(Property):
    def __init__(self, conductive=True, rusting=False)
        self.conductive = conductive
        self.rusting = rusting

class Golden(Metallic):
    pass

class Iron(Metallic):
    rusting = True


class Fragile(Property):
    def __init__(self, broken = False)
        self.broken = broken

class Glass(Fragile):
    pass




#--------------- switch property luokat ---------------


class Invisible(SwitchProperty):
    pass

class Blessed(SwitchProperty):
    default = False

class Cursed(SwitchProperty):
    default = False





