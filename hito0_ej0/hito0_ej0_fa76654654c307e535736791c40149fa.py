import random
lista_pokemon = []

class pokemon: #definimos clase pokemón
    def __init__(self,nombre,tipo,ataque="0| 0"):
        self.nombre = nombre
        self.nivel = random.randint(5,25)
        self.tipo = tipo
        self.ataque = ataque.split("| ") #Ataque como lista[nombre ataque, tipo ataque]
        self.ataque_nombre = self.ataque[0]
        self.ataque_tipo = self.tipo[1]
        self.HP = 3 * self.nivel
    def __str__(self):

        return "{0} ({1})".format(self.nombre[0].upper()+self.nombre[1:], self.tipo) #retorna el nombre y tipo del pokemón

def pedir_lista(): #Me entrega una lista "bonita" con los pokemones y su tipo
    for i in range(len(lista_pokemon)):
        print("{0}) {1}".format(i+1, str(lista_pokemon[i])))
          
        
from random import *

class Entrenador:
    def __init__(self,nombre):
        self.nombre=nombre
        self.pokemones=[]

    def agregar_pokemon(self,pokemon):
        if isinstance(pokemon,Pokemon)==False:
            print("Este no es un Pokemon")
            return False
        if len(self.pokemones)>6:
            print("Ya hay 6 pokemones")
            return False
        self.pokemones.append(pokemon)

    def __str__(self):
        s=""
        for pokemon in self.pokemones:
            s+=str(pokemon)+"\n"*2
        return s

    def eliminar_pokemon(self,pokemon):
        if isinstance(pokemon,Pokemon)==False:
            print("Este no es un pokemon")
            return False
        if pokemon not in self.pokemones:
            print("No puedes quitar un pokemon que no tienes")
            return False
        self.pokemones.remove(pokemon)

class Batalla:
    def __init__(self,contrincantes):
        if isinstance(contrincantes[0],Entrenador)==False or isinstance(contrincantes[0],Entrenador)==False or len(contrincantes)!=2:
            print("Sus contrincantes no son validos")
            return False
        self.contrincantes=contrincantes

    def atacar(self,posicion_atacante):  #1ro lista siemppre
        if posicion_atacante not in range(2):
            return False
        pokemon_atacante=self.contrincantes[posicion_atacante].pokemones[0]
        pokemon_atacado=self.contrincantes[(posicion_atacante+1)%2].pokemones[0]
        ataque=randrange
        if pokemon_atancante.tipo=="agua":
            if pokemon_atacado.tipo=="fuego":
                ataque*=2
            elif pokemon_atacado.tipo=="Hierba":
                ataque/=2
            elif pokemon_atacado.tipo=="agua":
                ataque/=2
        if pokemon_atancante.tipo=="fuego":
            if pokemon_atacado.tipo=="fuego":
                ataque/=2
            elif pokemon_atacado.tipo=="hierba":
                ataque*=2
            elif pokemon_atacado.tipo=="agua":
                ataque/=2
        if pokemon_atancante.tipo=="electricidad":
            if pokemon_atacado.tipo=="electricidad":
                ataque/=2
            elif pokemon_atacado.tipo=="hierba":
                ataque/=2
            elif pokemon_atacado.tipo=="agua":
                ataque*=2
        if pokemon_atancante.tipo=="hierba":
            if pokemon_atacado.tipo=="fuego":
                ataque/=2
            elif pokemon_atacado.tipo=="hierba":
                ataque/=2
            elif pokemon_atacado.tipo=="agua":
                ataque*=2
        pokemon_atacado.HP-=ataque
        self.contrincantes[(posicion_atacante+1)%2].pokemones[0]=pokemon_atacado
        if pokemon_atacado.HP<=0:
            self.contrincantes[(posicion_atacante+1)%2].pokemones.remove(pokemon_atacado)

    def cambiar_pokemon(self,pokemon_querido,posicion_contrincante):
        lista_pokemones=self.contrincantes[posicion_contrincante].pokemones.copy()
        if pokemon_querido not in lista_pokemones:
            return False
        pokemon=lista_pokemones.pop(lista_pokemones.find(pokemon_querido))
        lista_pokemones.insert(0,pokemon)
        self.contrincantes[posicion_contrincante].pokemones=lista_pokemones

    def recuperar(self,posicion_contrincante):
        self.contrincantes[posicion_contrincantes].pokemones[0].HP+=20

if __name__ == "__main__":
    nombre1=input("Ingrese el nombre del 1er contrincante: ")
    nombre2=input("Ingrese el nombre del 2do contrincante: ")
    contrincante1=Entrenador(nombre1)
    contrincante2=Entrenador(nombre2)
    batalla=Batalla([contrincante1,contrincante2])
    for i in range(2):
        while len(batalla.contrincates[i].pokemones)<7:
            accion=input("¿Desea agregar o quitar un pokemon? ")
            pokemon=input("¿Cual pokemon quiere?")
            pokemon=lista_pokemon[pokemon-1]
            pedir_lista()
            if accion.lower()=="agregar":
                batalla.contrincates[i].agregar_pokemon(pokemon)
                lista_pokemon.pop(pokemon-1)
            elif accion.lower()=="quitar":
                batalla.contrincates[i].eliminar(pokemon)
