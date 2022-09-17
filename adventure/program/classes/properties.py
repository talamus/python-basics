class Property:
    pass

class Reveal(Property):
    pass

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

class Hidden(Property):
    def __init__(self, hidden=True):
        self.hidden = hidden