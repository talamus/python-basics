
def TITLE(TITLE):
    print("\n--- "+ (TITLE+" ").ljust(40, "-"))

#============================================================================

class Item:
    name = None
    messages = None

    def __init__(self, name="", messages={}, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.messages = messages

    def __getattr__(self, attr_name):
        if attr_name in self.__dict__:
            return self.__dict__[attr_name]
        else:
            return None

#============================================================================

class Lockable:
    key = None
    is_locked = True
    def __init__(self, key="", is_locked=True, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.is_locked = is_locked

class Invisible:
    is_invisible = True

class Inventory:
    inventory = None
    def __init__(self, inventory = [], **kwargs):
        super().__init__(**kwargs)
        self.inventory = inventory

    def remove_item(self, item):
        if self.is_invisible:
            print("It's not visible!")
            return None

        if self.is_locked:
            print("It's locked!")
            return None

        elif item in self.inventory:
            i = self.inventory.index(item)
            return self.inventory.pop(i)

        else:
            print(item.name, "was not in there.")
            return None

class Chest(Item, Inventory, Lockable, Invisible):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("kwargs type:", type(kwargs))

#============================================================================

apple = Item("an apple")
banana = Item("a banana")
TITLE("Create chest")
chest = Chest(
    name="a wooden chest",
    messages={ "open": "Creak!" },
    inventory=[ banana, apple ],
#    key=Item("a wooden key"),
#    is_locked=False
)
TITLE("Print chest")
print(chest, chest.__dict__)
TITLE("Take item from chest")
item = chest.remove_item(banana)
TITLE("The item")
if item:
    print(item.name)
else:
    print(item)
TITLE("Print chest")
print(chest, chest.__dict__)
