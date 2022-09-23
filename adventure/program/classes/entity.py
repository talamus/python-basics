from program.classes.noun import Noun


class Entity:

    def __init__(self, name, *properties):                      # *properties - kaikki namen jälkeen tuleva menee listaan properties (* on lista, ** olisi dictionary)
        super().__init__(name)
        for property in properties:
            if callable(property):                              # jos property on callable (ei objekti koska obj ei ole callable)
                property = property()                           # niin ota property ja aja se funktiona --> ulos property objekti
            self.gain_property(property)                        # ajetaan metodi gain_property objektin (self) joka propertylle


    def __getattr__(self, attr_name):                      # def getattribute
        try:
            return self.__dict__[attr_name]                     # katso onko self dictionaryssä attr_name (esim wearable)
        except KeyError:                                        # jos ei löydy, palauttaa key error
            return None                                         # silloin return None niin ei ohjelma kaadu :)



    def gain_property(self, property):                                  # metodi (joka siis on funktio)
        setattr(self, property.__class__.__name__.lower(), property)    # aseta attribuutti: objekti, luokan nimi (string), ja property
                                                                        # tämä tallentuu objektin sisäiseen dictionaryyn
                                                                        # key-value parina joka osoittaa property objektiin
   # def lose_property(self, property):

class Item(Entity):
    pass

class Fixture(Entity):
    pass



