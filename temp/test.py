def print_kwargs(label, **kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for key, value in kwargs.items():
        result += f" ( {key} : {value} ) "
    print(label +":", result)


class Item:
    name = None
    messages = None
    def __init__(self, name="", messages={}, **kwargs):
        print("I'm running Item constructor! I'm", name)
        print_kwargs("item_before", **kwargs)
        super().__init__(**kwargs)
        print_kwargs("item_after", **kwargs)
        self.name = name
        self.messages = messages
        print("Item constructor done.")

class Lockable:
    key = None
    is_locked = True
    def __init__(self, key="", is_locked=True, **kwargs):
        print("I'm running Lockable constructor!")
        print_kwargs("lockable_before", **kwargs)
        super().__init__(**kwargs)
        print_kwargs("lockable_after", **kwargs)
        self.key = key
        self.is_locked = is_locked
        print("Lockable constructor done.")

class Container:
    inventory = None
    def __init__(self, inventory = [], **kwargs):
        print("I'm running Container constructor!")
        print_kwargs("container_before", **kwargs)
        super().__init__(**kwargs)
        print_kwargs("container_after", **kwargs)
        self.inventory = inventory
        print("Container constructor done.")

class Chest(Item, Lockable, Container):
    def __init__(self, **kwargs):
        print("Creating a chest...")
        print_kwargs("chest_before", **kwargs)
        super().__init__(**kwargs)
        print_kwargs("chest_after", **kwargs)
        print("Chest done!")


print("-------------")
chest = Chest(
    name="a wooden chest",
    messages={ "open": "Creak!" },
    inventory=[ Item("a banana") ],
    key=Item("a wooden key")
)
print("-------------")
print(chest, chest.__dict__)
print("-------------")

