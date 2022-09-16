from program.classes.noun import Noun

class Item(Noun):
    def __init__(self, name, messages={}, properties=[]):
        super().__init__(name)
        self.messages = messages
        self.properties = properties

        for property in properties:
            

class Fixture(Item):
    pass