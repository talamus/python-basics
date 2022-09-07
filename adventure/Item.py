from Noun import Noun

class Item(Noun):
    def __init__(self, name, messages={}):
        super().__init__(name)
        self.messages = messages

class Fixture(Item):
    pass