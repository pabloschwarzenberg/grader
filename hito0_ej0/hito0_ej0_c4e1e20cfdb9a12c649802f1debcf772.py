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

class Batalla:
    def __init__(self,contrincante1,contrincate2):
        self.contrincante1=contrincante1
        self.contrincante2=contrincante2
        pokemon1=contrincante1.primer_pokemon()
        pokemon2=contrincante2.primer_pokemon()
        

    def comparar_nivel(self):
        
        nivel1=pokemon1.nivel
        nivel2=pokemon2.nivel
        if nivel1>nivel2:
            return "ataca"+pokemon1
        if nivel2>nivel1:
            return "ataca"+pokemon2
        if nivel1==nivel2:
            lista=[pokemon1,pokemon2]
            x=random.choice(lista)
            return "ataca"+x

    def atacar(self):
        

    def cambiar_pokemon(self,
    
batalla1=Batalla(hola,chao)
comparar_nivel.#falta