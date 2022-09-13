from program.classes.noun import Noun

class Item(Noun):
    messages = None
    def __init__(self, name, messages={}):
        super().__init__(name)
        self.messages = messages

class Fixture(Item):
    pass
