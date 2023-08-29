#PARTE 1 OOP POKEMON IIC1103
#Pokemon.py con las definiciones de Pokemon y Entrenador
#Clase Pokemon y clase Entrenador
#Atributos de las clases
#Batalla.py con la clase batalla y el programa principal


###CLASE POKEMON
#nombre
#nivel que es un numero al azar entre 5 y 25
#un ataque con nombre y tipo
#una vida (HP) la cual se modifica. Es igual al nivel multiplicado por 3
#disponemos de un csv con información de pokemons

import random

class Pokemon:
    def _init_(self, nombre, tipo, nivel, hp, ataques):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.hp = hp
        self.ataques = ataques

class MiEquipo:
    def _init_(self):
        self.equipo = []

    def agregar_pokemon(self, pokemon):
        self.equipo.append(pokemon)

    def mostrar_equipo(self):
        for pokemon in self.equipo:
             print("Nombre: {0} \nTipo: {1} \nNivel: {2} \nHP: {3} \nAtaques: {4} \n-----------"
                  "".format(pokemon.nombre, pokemon.tipo, pokemon.nivel, pokemon.hp, pokemon.ataques))




Equipo = MiEquipo()

###############################################################################
###################################Selección de Equipo#########################
a=input("ingrese el numero de su primera elección pokemon:")
b=input("ingrese el numero de su segunda elección pokemon:")
c=input("ingrese el numero de su tercera elección pokemon:")
d=input("ingrese el numero de su cuarta elección pokemon:")
e=input("ingrese el numero de su quinta elección pokemon:")
f=input("ingrese el numero de su sexta elección pokemon:")

pokemon1 = "t"+a
pokemon2 = "t"+b
pokemon3 = "t"+c
pokemon4 = "t"+d
pokemon5 = "t"+e
pokemon6 = "t"+f

print(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
###############################POKEDEX##########################################
X=random.randint(1, 25)
t1 = Pokemon("charizard","fuego", X, 3*X, "Ataques1")
X=random.randint(1,25)
t2 = Pokemon("blastoise","agua", X, 3*X, "Ataques1")
X=random.randint(1,25)
t3 = Pokemon("vileplum","hierba", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon4 = Pokemon("sudowido","hierba", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon5 = Pokemon("chikorita","hierba", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon6 = Pokemon("cogollin","hierba", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon7 = Pokemon("cogollon","hierba", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon8 = Pokemon("gloom","hierba", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon9 = Pokemon("psyduck","agua", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon10 = Pokemon("Pikachu","electricidad", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon11 = Pokemon("Raichu","electricidad", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon12 = Pokemon("victribel","hierba", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon13 = Pokemon("Ninetales","fuego", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon14 = Pokemon("Rapidash","fuego", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon15 = Pokemon("Jairo","dios", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon16 = Pokemon("Kingler","agua", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon17 = Pokemon("zapdos","electricidad", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon18 = Pokemon("moltres","fuego", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon19 = Pokemon("Gyarados","agua", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon20 = Pokemon("Exeggutor","hierba", X, 3*X, "Ataques1")
X=random.randint(1,25)
pokemon21 = Pokemon("charmandaer","fuego", X, 3*X, "Ataques1")
X=random.randint(1,25)
t22 = Pokemon("typhlosion","fuego", X, 3*X, "Ataques1")
X=random.randint(1,25)
t23 = Pokemon("electrode","electricidad", X, 3*X, "Ataques1")
X=random.randint(1,25)
t24 = Pokemon("Seadra","agua", X, 3*X, "Ataques1")
X=random.randint(1,25)
t25 = Pokemon("Magikarp","agua", X, 3*X, "Ataques1")

print(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)


Equipo.agregar_pokemon(pokemon1)
Equipo.agregar_pokemon(pokemon2)
Equipo.agregar_pokemon(pokemon3)
Equipo.agregar_pokemon(pokemon4)
Equipo.agregar_pokemon(pokemon5)
Equipo.agregar_pokemon(pokemon6)
Equipo.mostrar_equipo()