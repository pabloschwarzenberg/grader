import random
import os

class Pokemon:
    def __init__(self,nombre,tipo,ataque):
        self.nombre=nombre
        self.level=random.randint(5,25)
        self.tipo=tipo
        self.ataque=ataque
        self.hp=self.level*3
    def __str__(self):
        string = ""
        string+= self.nombre
        string+="\n"+ str(self.level)
        string+="\n"+ (str(self.hp))
        string+="\n"+ (self.tipo)
        string+="\n"+ (self.ataque)  
        return string

class Entrenador:
    def __init__(self,nombre):
        self.nombre=nombre
        self.lista_pokemon=[]
    def agregar_poke(self):
        self.lista_pokemon.append()
    def __str__(self):
        return self.nombre
    
pokemon=[]
archivo_datos=open("pokemon.csv", "r")
for linea in archivo_datos:
    linea=linea.strip()
    linea=linea.split(",")
    pokemon.append(linea)


bulbasaur=Pokemon(pokemon[0][0],pokemon[0][1], "Látigo Cepa, hierba")
charmander=Pokemon(pokemon[1][0],pokemon[1][1], "Lanzallamas, fuego")
chikorita=Pokemon(pokemon[2][0],pokemon[2][1], "Látigo Cepa, hierba")
chimchar=Pokemon(pokemon[3][0],pokemon[3][1], "Lanzallamas, fuego")
flareon=Pokemon(pokemon[4][0],pokemon[4][1], "Lanzallamas, fuego")
lapras=Pokemon(pokemon[5][0],pokemon[5][1], "Surf, agua")
magmar=Pokemon(pokemon[6][0],pokemon[6][1], "Lanzallamas, fuego")
magnetime=Pokemon(pokemon[7][0],pokemon[7][1], "Impactrueno, electrico")
pikachu=Pokemon(pokemon[8][0],pokemon[8][1],"Impactrueno, electrico")
rotom=Pokemon(pokemon[9][0],pokemon[9][1], "Impactrueno, electrico")
squirtle=Pokemon(pokemon[10][0],pokemon[10][1], "Hidrobomba, agua")
sunflora=Pokemon(pokemon[11][0],pokemon[11][1], "Látigo Cepa, hierba")
tentacool=Pokemon(pokemon[12][0],pokemon[12][1], "Surf, agua")
treecko=Pokemon(pokemon[13][0],pokemon[13][1], "Látigo Cepa, hierba")
wartortle=Pokemon(pokemon[14][0],pokemon[14][1], "Hidrobomba, agua")
zebstrika=Pokemon(pokemon[15][0],pokemon[15][1], "Impactrueno, electrico")

print("Ingrese su nombre de entrenador")
entrenador=input()
entrenador=Entrenador(str(entrenador))
print(entrenador)
i=0
while i<6:
    print("Qué Pokemon deseas escoger?")
    pokemon=input()
    Entrenador.agregar_poke(pokemon)

print(self.lista_pokemon)
