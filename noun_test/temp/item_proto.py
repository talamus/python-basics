
class Item():

    def __init__(self, name, *properties):                      # *properties - kaikki namen jälkeen tuleva menee listaan properties (* on lista, ** olisi dictionary)
#        super().__init__(name)
        for property in properties:
            if callable(property):                              # jos property on callable (ei objekti koska obj ei ole callable)
                property = property()                           # niin ota property ja aja se funktiona --> ulos property objekti
            self.gain_property(property)                        # ajetaan metodi gain_property objektin (self) joka propertylle

    def gain_property(self, property):                                  # metodi (joka siis on funktio)
        setattr(self, property.__class__.__name__.lower(), property)    # aseta attribuutti: objekti, luokan nimi (string), ja property
                                                                        # tämä tallentuu objektin sisäiseen dictionaryyn
                                                                        # key-value parina joka osoittaa property objektiin
    def lose_property(self, property):
        print("?????", property)

#---------------------------

class Property:
    pass

class Wearable(Property):
    messages = {
        "wear": "You put the thing on.",
        "take off": "You take the thing off.",
        "already worn": "You are already wearing it.",
        "not wearing": "You are not wearing it."
    }

    def __init__(self, worn=False, messages={}):
        self.worn = worn
        self.messages = self.messages | messages

    def wear(self):                                     # 'wear' on objektin metodi!!! usage outside: object.wearable.wear (object kohtaan objektin nimi esim. ring)
        if self.worn:
            print(self.messages["already worn"])
        else:
            self.worn = True
            print(self.messages["wear"])

    def remove(self):
        if self.worn:
            self.worn = False
            print(self.messages["take off"])
        else:
            print(self.messages["not wearing"])

#----------------------------

ring = Item("a small golden ring",
    Wearable(messages={
        "wear": "The left pinky is the only finger that the ring fits on.",
        "take off": "It was a struggle, but the golden ring is finally off!"
    })
)              # [Wearable(True)] runs Wearable function and sets the attribute to True (it only has two and the first is self so this goes into the second)

ring2 = Item("a large iron ring",
    Wearable(messages={
        "wear": "The right thumb is the only finger that the ring stays on.",
        "take off": "The iron ring falls off without a struggle."
    })
)


print("============================")
print(ring.__dict__)
print(ring.wearable)
ring.wearable.wear()
print(ring.wearable.worn)
ring.wearable.wear()
ring.wearable.remove()
print(ring.wearable.worn)
ring.wearable.remove()

print("============================")
print(ring2.__dict__)
print(ring2.wearable)
ring2.wearable.wear()
print(ring2.wearable.worn)
ring2.wearable.wear()
ring2.wearable.remove()
print(ring2.wearable.worn)
ring2.wearable.remove()

