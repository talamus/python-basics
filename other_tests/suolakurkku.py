# This programs turns complex objects into a binary blob -- and restores them back to life.

import pickle

class VaikeaLuokka:          # ComplexClass
    nimi = "marsu"           # name = "guinea pig"
    hamsteri = False         # not a hampster!
    lukumaara = 123          # count = 123

    def make_hamster(self):  # Force to be a hampster!
        self.hamsteri = True

    def __str__(self):       # Return this object as a string
        return "Marsu on " + str(self.__dict__)

# Main program:

marsu1 = VaikeaLuokka()      # guinea_pig_1 = ComplexClass()
marsu2 = VaikeaLuokka()

marsu2.make_hamster()        # Force guinea_pig_2 to be a hampster! (Heresy!)

lista = [ marsu1, marsu2 ]   # List = all the guinea pigs
for marsu in lista:
    print(marsu)             # Print them!

pikkelsi = pickle.dumps(lista)   # Pickle the guinea pigs! 
print("pikkelsi:", pikkelsi)     # Print out!

lista_kakkonen = pickle.loads(pikkelsi)   # Turn pickle into a new list
for marsu in lista_kakkonen:  
    print(marsu)             # Print them!
