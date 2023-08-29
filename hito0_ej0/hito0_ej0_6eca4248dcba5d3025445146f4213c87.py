import random

class Pokemon:
    def __init__(self,nombre_pokemon,nivel,tipo,ataque,vida):
        self.nombre_pokemon=nombre_pokemon
        self.nivel=nivel
        self.tipo=tipo
        self.ataque=ataque
        self.vida=vida

class Entrenador:
    def __init__(self,nombre_entrenador,pokemones,capacidad):
        self.nombre_entrenador=nombre_entrenador
        self.pokemones=pokemones
        self.capacidad=capacidad

pokemones=[]
archivo_datos=open("pokemon.csv","r")
for linea in archivo_datos:
    linea=linea.strip()
    linea=linea.split(",")
    nivel=random.randint(5,25)
    pokemon=Pokemon(linea[0],nivel,linea[1],linea[0],nivel*3)
    pokemones.append(pokemon)

print(len(pokemones))
for pokemon in pokemones:
    print(pokemon.nombre_pokemon)

nombre_entrenador=input("Ingrese nombre del entrenador: ")
lista_pokemones=pokemones
print(lista_pokemones)
lista_pokemones.pop(5)
print(lista_pokemones)

