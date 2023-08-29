class Pokemon:
        import random

class Pokemon:
    def __init__(self,nombre,tipo,ataque):
        self.nombre=nombre
        self.nivel=random.randint(range(5,26))
        self.tipo=tipo
        self.ataque=ataque
        self.HP=self.nivel*3

lista_pokemon = []
archivo_datos = open("pokemon.csv")
for linea in archivo_datos:
    linea = linea.strip()
    linea = linea.split(",")
    lista_pokemon.append(linea)
print(lista_pokemon)
class Entrenador:
        pass
class Batalla:
        pass
      