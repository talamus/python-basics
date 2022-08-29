import pickle
from pprint import pprint

class VaikeaLuokka:
    nimi = "marsu"
    hamsteri = False
    lukumaara = 123

    def make_hamster(self):
        self.hamsteri = True

    def __str__(self):
        return "Marsu on " + str(self.__dict__)

marsu1 = VaikeaLuokka()
marsu2 = VaikeaLuokka()

marsu2.make_hamster()

lista = [ marsu1, marsu2 ]
for marsu in lista:
    print(marsu)

pikkelsi = pickle.dumps(lista)
print("pikkelsi:", pikkelsi)

lista_kakkonen = pickle.loads(pikkelsi)
for marsu in lista_kakkonen:
    print(marsu)


