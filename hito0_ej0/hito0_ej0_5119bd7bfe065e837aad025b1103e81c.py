#PERDON POR EL DESORDEN, HAY ALGUNOS PROBLEMAS CON EL RANDOM.RANDINT QUE INTENTÉ RESOLVER. PERO LO HICE SÓLO ASI QUE COSTÓ MÁS DEPURARLO. OJALÁ TE GUSTE EL CÓDIGO.
#LA PLATAFORMA NO ME PERMITE SUBIR EL ARCHIVO PYTHON CON INPUTS, ASÍ QUE SÓLO SUBÍ CLASES, FUNCIONES Y METODOS. CUALQUIER DUDA, PUEDEN AVISARME A YMDORON@UC.CL

import random 
import math

class Entrenador:
    def __init__(self,nombre,pokemones):
        self.nombre=nombre
        self.pokemones=pokemones
        

class Pokemon:
    def __init__(self,nombre,nivel,tipo,ataque,HP,nombre_dano):
        self.nombre=nombre
        self.nivel=nivel
        self.tipo=tipo
        self.ataque=ataque
        self.HP=HP
        self.nombre_dano=nombre_dano

class Batalla:
    def __init__(self,entrenador1,entrenador2,pokemon1,pokemon2,recuperar1,recuperar2):
        contrincantes=[]
        contrincantes.append(entrenador1)
        contrincantes.append(entrenador2)
        self.entrenador1=entrenador1
        self.entrenador2=entrenador2
        self.pokemon1=pokemon1
        self.pokemon2=pokemon2
        self.recuperar1=0
        self.recuperar2=0


    def Atacar(self,pokemon1,pokemon2):
            if (pokemon1.tipo=="Agua" and pokemon2.tipo=="Fuego") or (pokemon1.tipo=="Fuego" and pokemon2.tipo=="Hierba") or (pokemon1.tipo=="Electricidad" and pokemon2.tipo=="Agua") or (pokemon1.tipo=="Hierba" and pokemon2.tipo=="Agua"):
                pokemon2.HP=pokemon2.HP-(pokemon1.ataque)*2
                return (pokemon1,"ataca por",pokemon1.ataque,"puntos de daño!")
                
            elif (pokemon1.tipo=="Agua" and pokemon2.tipo=="Hierba") or (pokemon1.tipo=="Agua" and pokemon2.tipo=="Agua") or (pokemon1.tipo=="Fuego" and pokemon2.tipo=="Fuego") or (pokemon1.tipo=="Fuego" and pokemon2.tipo=="Agua") or (pokemon1.tipo=="Electricidad" and pokemon2.tipo=="Hierba") or (pokemon1.tipo=="Electricidad" and pokemon2.tipo=="Electricidad") or (pokemon1.tipo=="Hierba" and pokemon2.tipo=="Fuego") or (pokemon1.tipo=="Hierba" and pokemon2.tipo=="Hierba"):
                pokemon2.HP=pokemon2.HP-(pokemon1.ataque)*(1/2)
                return (pokemon1,"ataca por",pokemon1.ataque,"puntos de daño!")

            elif (pokemon1.tipo=="Agua" and pokemon2.tipo=="Electricidad") or (pokemon1.tipo=="Fuego" and pokemon2.tipo=="Electricidad") or (pokemon1.tipo=="Electricidad" and pokemon2.tipo=="Fuego") or (pokemon1.tipo=="Hierba" and pokemon2.tipo=="Electricidad"):
                pokemon2.HP=pokemon2.HP-(pokemon1.ataque)
                return (pokemon1,"ataca por",pokemon1.ataque,"puntos de daño!")


    def Cambiar_Pokemon(self,pokemon):
        e=self.pokemones
        e.remove(pokemon)
        e.insert(0,pokemon)
        self.pokemon=e[0]


    def Recuperar(self,pokemon):
        if self.recuperar<2:
            pokemon.HP=pokemon.HP+20
            self.recuperar1=self.recuperar1+1
            return (pokemon,"ha recuperado 20 de HP!")
        else:
            print("Ya haz recuperador a tu Pokemon 2 veces, no puedes recuperar más!")
            return none


def gameover(p1,p2):
    gm=0
    for i in p1:
        if i.HP==0:
            gm=gm+1
    if gm==len(p1):
        print("Se acabó! El jugador 2 gana!")
    o=0
    for i in p2:
        if i.HP==0:
            o=o+1
    if o==len(p2):
        print("Se acabó! El jugador 1 gana!")