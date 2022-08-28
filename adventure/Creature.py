
class Creature:
    name = None                         # Attributes!
    description = None
    current_location = None
    items = []

    def __init__(self, attributes):     # Methods! 

        def set_attribute_for_self(key, value):
            setattr(self, key, value)

        map(set_attribute_for_self, attributes.keys(), attributes.values())

        #---------

        for key, value in attributes.items():
            setattr(self, key, value)

    def describe(self):
        print(self.description)


class Dragon(Creature):
    is_sleep = True

    def speak(self):
        print("Roar! My name is "+ self.name)


class Player(Creature):
    def move(self, new_location):
        # check if the player can move to new location
        self.current_location = new_location

#------------------------
# In the Main file:

player = Player({ "name": "Joakim", "location": "red" })
print(player.current_location)
player.move("green")
print(player.current_location)
