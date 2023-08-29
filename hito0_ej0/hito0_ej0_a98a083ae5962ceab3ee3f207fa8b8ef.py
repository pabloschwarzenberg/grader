import random

class Pokemon:
    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.nivel=random.randint(5,25)
        self.tipo=tipo
        if tipo=="hierba":
            self.ataque = "Latigo cepa"
        elif tipo=="fuego":
            self.ataque= "Lanzallamas"
        elif tipo=="electrico":
            self.ataque="Impactrueno"
        elif tipo=="agua":
            self.ataque="Surf"
        self.vida=self.nivel*3
        self.vida_actual=self.vida

class Entrenador:
    def __init__(self,nombre):
        self.nombre=nombre
        self.mispk=[]
        self.recuperar_restantes=2
        print("De la siguiente lista escoja 6 pokemones")
        print(" ")
        contador=1
        for x in listapokemones:
            print("Pokemon Número: %s"%contador)
            print("Nombre:", x[0])
            print("Tipo:",x[1])
            print(" ")
            contador+=1
        while len(self.mispk)<6:
            eleccion=int(input("Ingrese el numero del pokemon que desea añadir a su team"))
            eleccion-=1
            pokemonchs=listapokemones[eleccion]
            elegido=Pokemon(pokemonchs[0],pokemonchs[1])
            self.mispk.append(elegido)

    def estado(self):
        p=1
        for cada in self.mispk:
            print("%s) "%p, cada.nombre, "- Nivel:", cada.nivel, "- HP: %s/%s" %(cada.vida_actual, cada.vida))
            p+=1

class Batalla:
    def __init__(self,pj1,pj2):
        self.contrincantes=[]
        self.contrincantes.append(pj1)
        self.contrincantes.append(pj2)
        if (pj1.mispk[0]).nivel >= (pj2.mispk[0]).nivel :
            self.inicio=1
        else:
            self.inicio=2
    def atacar(self):
        k=self.inicio-1
        actualjugando = self.contrincantes[k]
        if k==0:
            enemigo=self.contrincantes[1]
        if k==1:
            enemigo=self.contrincantes[0]
        limite=actualjugando.mispk[0].nivel / 25 * 2.6
        limite=int(limite)
        dmg=random.randint(0,limite)
        tipo1=actualjugando.mispk[0].tipo
        tipo2=enemigo.mispk[0].tipo
        print("%s ha usado %s" %(actualjugando.mispk[0].nombre,actualjugando.mispk[0].ataque))
        if tipo1=="agua":
            if tipo2=="fuego":
                dmg=dmg*2
                print("Ataque muy efectivo!")
            elif tipo2=="hierba":
                dmg=dmg/2
                print("Ataque poco efectivo")
            elif tipo2=="agua":
                dmg=dmg/2
                print("Ataque poco efectivo")
            else:
                print("Un ataque normal")
        elif tipo1=="fuego":
            if tipo2=="fuego":
                dmg=dmg/2
                print("Ataque poco efectivo")
            elif tipo2=="hierba":
                dmg=dmg*2
                print("Ataque muy efectivo!")
            elif tipo2=="agua":
                dmg=dmg/2
                print("Ataque poco efectivo")
            else:
                print("Un ataque normal")
        elif tipo1=="electrico":
            if tipo2=="fuego":
                print("Un ataque normal")
            elif tipo2=="hierba":
                dmg=dmg/2
                print("Ataque poco efectivo")
            elif tipo2=="agua":
                dmg=dmg*2
                print("Ataque muy efectivo!")
            else:
                dmg=dmg/2
                print("Ataque poco efectivo")
        else:
            if tipo2=="fuego":
                dmg=dmg/2
                print("Ataque poco efectivo")
            elif tipo2=="hierba":
                dmg=dmg/2
                print("Ataque poco efectivo")
            elif tipo2=="agua":
                dmg=dmg*2
                print("Ataque muy efectivo!")
            else:
                print("Un ataque normal")
        enemigo.mispk[0].vida_actual-=dmg
        print(" ")
        print("Daño realizado al pokemon enemigo:" ,dmg)

        if enemigo.mispk[0].vida_actual <=0:
            enemigo.mispk.pop(0)
            print("Pokemon enemigo derrotado!")
        else:
            print("Vida actual del pokemon enemigo:", enemigo.mispk[0].vida_actual)
        self.sgteturno(k)

    def cambiar(self):
        k = self.inicio - 1
        actualjugando=self.contrincantes[k]
        print("Ingrese el numero del pokemon al cual desea cambiar")
        actualjugando.estado()
        acambiar=input(">>>")
        acambiar=int(acambiar)-1
        extraccion=actualjugando.mispk.pop(acambiar)
        actualjugando.mispk.insert(0, extraccion)
        self.sgteturno(k)
        print("Cambio realizado correctamente!")
        print("Actual pokemon elegido:", actualjugando.mispk[0].nombre)

    def recuperar(self):
        k=self.inicio-1
        if self.contrincantes[k].recuperar_restantes>0:

            diferencia=(self.contrincantes[k].mispk[0]).vida - (self.contrincantes[k].mispk[0]).vida_actual
            if diferencia>=20:
                (self.contrincantes[k].mispk[0]).vida_actual+=20
                print("Curación realizada correctamente")
                print("Vida actual del pokemon:", (self.contrincantes[k].mispk[0]).vida_actual)
            else:
                (self.contrincantes[k].mispk[0]).vida_actual=(self.contrincantes[k].mispk[0]).vida
                print("Curación realizada correctamente")
                print("Vida actual del pokemon:", (self.contrincantes[k].mispk[0]).vida_actual)
            self.contrincantes[k].recuperar_restantes-=1
            self.sgteturno(k)

        else:
            print("No quedan recuperar restantes")
    def sgteturno(self,k):
        if k==0:
            self.inicio = 2
        elif k==1:
            self.inicio = 1



listapokemones=[]
open_f=open("pokemon.csv","r")
lista_temp=open_f.readlines()
for cada in lista_temp:
    cada=cada.split("\n")
    cada=cada[0].split(",")
    listapokemones.append(cada)

open_f.close()

print("Ingrese nombre del primer entrenador")
name=input(">>>")
pj1=Entrenador(name)
print(" ")
print("Ingrese nombre del segundo entrenador")
name=input(">>>")
pj2=Entrenador(name)

batalla=Batalla(pj1,pj2)

while True:
    if len(batalla.contrincantes[batalla.inicio-1].mispk)==0:
        print("No le quedan pokemones al jugador %s" %(batalla.contrincantes[batalla.inicio-1].nombre))
        print("Ha ganado el otro jugador!")
        break
    print(" ")
    print("Actualmente turno del jugador numero:",batalla.inicio)
    print("Entrenador actual:", batalla.contrincantes[batalla.inicio-1].nombre)
    print("Pokemon actual:", batalla.contrincantes[batalla.inicio-1].mispk[0].nombre)
    print("Tipo:", batalla.contrincantes[batalla.inicio-1].mispk[0].tipo, "- HP: %s/%s" %(batalla.contrincantes[batalla.inicio-1].mispk[0].vida_actual,batalla.contrincantes[batalla.inicio-1].mispk[0].vida))
    if batalla.inicio==2:
        print("Pokemon enemigo:", batalla.contrincantes[0].mispk[0].nombre)
        print("Tipo:",batalla.contrincantes[0].mispk[0].tipo, "- HP: %s/%s" % (batalla.contrincantes[0].mispk[0].vida_actual, batalla.contrincantes[0].mispk[0].vida))
    else:
        print("Pokemon enemigo:", batalla.contrincantes[1].mispk[0].nombre)
        print("Tipo:", batalla.contrincantes[1].mispk[0].tipo,
              "- HP: %s/%s" % (batalla.contrincantes[1].mispk[0].vida_actual, batalla.contrincantes[1].mispk[0].vida))

    print("Que desea hacer?")
    print("1) Atacar 2) Cambiar pokemon 3) Curar pokemon actual 4) Ver estado actual de mis pokemones")
    decision=int(input(">>>"))
    if decision==1:
        batalla.atacar()
    elif decision==2:
        batalla.cambiar()
    elif decision==3:
        batalla.recuperar()
    elif decision==4:
        jugadoractual=batalla.contrincantes[(batalla.inicio)-1]
        jugadoractual.estado()


