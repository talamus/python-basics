
class Item:
    name = None
    #...

class Openable:
    is_opened = False

    def open(self):
        self.is_opened = True
       
    def close(self):        
        self.is_opened = False

class Container:
    items_inside = []

class Chest(Item, Openable, Container):

# --------------------

item = Chest()

if item is Openable and item.is_opened:
    
    ...



