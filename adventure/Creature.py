
class Creature:
    name = None                         # Attributes!
    description = None
    current_location = None
    items = []

    def __init__(self, attributes):     # Methods! 
        # init attributes from dictionary
        pass

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

player = Player({})

player.move("red")
print(player.current_location)

player.move("green")
print(player.current_location)
