from pprint import pprint

class Noun:
    def __init__(self, name):
        self.name = name

class Invisible:
    def __init__(self, invisible=True):
        self.invisible = invisible
    def set(self, invisible):
        self.invisible = invisible
    def __bool__(self):
        return self.invisible

class Description:
    def __init__(self, text=""):
        self.text = text
    def __str__(self):
        return self.text

class Wooden:
    def __bool__(self):
        return True

class Inventory:
    default_messages = {
        "multiple": "It contains {items}.",
        "one item": "It contains only {item}.",
        "empty": "It's empty."
    }
    def __init__(self, items=[], messages={}):
        self.items = items
        self.messages = self.default_messages | messages
    def __str__(self):
        if self.items:
            if len(self.items) == 1:
                return self.messages["one item"].format(item = self.items[0])
            else:
                return self.messages["multiple"].format(items = " and ".join(self.items))
        else:
            return self.messages["empty"]

class Item(Noun):
    def __init__(self, name, *properties):
        super().__init__(name)

        def return_only_objects(thing):
            if isinstance(thing, type):
                return thing()
            else:
                return thing

        properties = map(return_only_objects, properties)

        for property in properties:
            setattr(self, property.__class__.__name__.lower(), property)

        self.properties = properties

    def __getattr__(self, attr_name):
        try:
            return self.__dict__[attr_name]
        except KeyError:
            return None

#===============================================================

chest = Item(
    "a wooden chest",
    Wooden,
    Description("It's a large wooden chest."),
    Invisible,
    Inventory([ "banana", "apple" ], { "empty": "The wooden chest is totally empty." })
)

#===============================================================
print(chest, chest.properties)
pprint(vars(chest))
print(">", chest.inventory)
print(chest.inventory.items)
print(chest.description)
if chest.wooden:
    print("The chest is on fire!")
else:
    print("No fire.")

if chest.invisible:
    print("The chest is invisible.")
else:
    print("You see a chest.")

chest.invisible.set(False)

if chest.invisible:
    print("The chest is invisible.")
else:
    print("You see a chest.")

print(">", chest.inventory)
chest.inventory.items = []
print(">", chest.inventory)
print("-------------------")

player_inventory = Inventory(
    items=[],
    messages={
        "one item": "You have only {item}.",
        "empty": "Your pockets are empty.",
        "multiple": "You have {items}!"
    }
)
print(player_inventory)
player_inventory.items = [ "makkara" ]
print(player_inventory)
player_inventory.items = [ "makkara", "ketsuppi" ]
print(player_inventory)


