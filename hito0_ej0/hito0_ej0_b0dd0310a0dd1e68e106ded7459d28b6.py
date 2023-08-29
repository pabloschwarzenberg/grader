# hola profesor, los integrantes son:
#Eitan Dvorquez
#Ana Arredondo
#Camilo Sanchez
#Felipe Donoso
#Isaac Gallegos
#Alexander Barrera

import random
class Pokemon:
    def __init__(self,nombre,tipo,habilidades):
        n=random.randint(5,25)
        self.nombre=nombre
        self.nivel=n
        self.tipo=tipo
        self.habilidades=habilidades
        self.hp=n*3
        self.veces_heleado=0

    def __str__(self):
        a=self.nombre+", Nivel: "+str(self.nivel)+", Hp: "+str(self.hp)+", "+self.tipo+", Habilidades: "
        for hab in self.habilidades:
            a=a+"  ->"
            for part in hab:
                a=a+","+str(part)
        return a


def leer_poquemones(nombre_archivo):
    archivo=open(nombre_archivo,"r")
    ar=list(archivo.readlines())
    archivo.close()
    fin=[]
    for l in ar:
        seleccionado=l.split(",")
        nom=seleccionado.pop(0)
        tip=seleccionado.pop(0)
        hab=[]
        k=0
        i=0
        while i < len(seleccionado)//3:
            n=seleccionado[k]
            t=seleccionado[k+1]
            s=int(seleccionado[k+2].replace("\n",""))
            a=[n,t,s]
            hab.append(a)
            k=k+3
            i=i+1
        poq=Pokemon(nom,tip,hab)
        fin.append(poq)
    return fin

class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pokemones = []

    def elegir_pokemon(self,listapokemon):
        k = 0
        for n in listapokemon:
            print(str(k) + " " + str(n))
            k += 1
            continue
        print("Debes tener 6 pokemones para empezar.")
        while len(self.pokemones) < 6:
            elegidos = str(input("Elija un pokemon:\n->"))
            while elegidos.isdigit() == False or int(elegidos) > len(lista_pokemones):
                print("No existe ese pokemon, elija otro.")
                elegidos = str(input("Elija un pokemon:\n->"))
            pok=listapokemon[int(elegidos)]
            nombre=pok.nombre
            tipo=pok.tipo
            habil=pok.habilidades
            hp=pok.hp
            niv=pok.nivel
            pk2=Pokemon(nombre,tipo,habil)
            pk2.hp=hp
            pk2.nivel=niv
            self.pokemones.append(pk2)
        return

    def mostrar_pokemones (self):
        for p in self.pokemones:
            print(p)
        return

def mayor_nivel(x, y):
    if x.nivel == y.nivel:
        return random.choice([0, 1])
    elif x.nivel > y.nivel:
        return 0
    elif x.nivel < y.nivel:
        return 1

def mult_ataque(x,y):
    if x[1]== "agua":
        if y.tipo== "fuego":
            return 2
        if y.tipo=="hierba":
            return 0.5
        if y.tipo=="agua":
            return 0.5
        if y.tipo=="electricidad":
            return 1
    elif x[1]== "fuego":
        if y.tipo== "fuego":
            return 0.5
        if y.tipo=="hierba":
            return 2
        if y.tipo=="agua":
            return 0.5
        if y.tipo=="electricidad":
            return 1
    elif x[1]== "electricidad":
        if y.tipo== "fuego":
            return 1
        if y.tipo=="hierba":
            return 0.5
        if y.tipo=="agua":
            return 2
        if y.tipo=="electricidad":
            return 0.5
    elif x[1]== "hierba":
        if y.tipo== "fuego":
            return 0.5
        if y.tipo=="hierba":
            return 0.5
        if y.tipo=="agua":
            return 2
        if y.tipo=="electricidad":
            return 1

def ataque(x,y):
    print("Seleccione una de las siguientes Habilidades:")
    c=1
    for i in x.habilidades:
        print(str(c)+")"+i[0]+", tipo:"+i[1]+ ", Daño estimado:" +str(i[2]))
        c=c+1
    opcion=int(input("->"))
    while opcion > len(x.habilidades)+1:
        print(len(x.habilidades))
        print("ingreso incorrecto")
        print("Seleccione una de las siguientes Habilidades:")
        c = 1
        for i in x.habilidades:
            print(str(c) + ")" + i[0] + ", tipo:" + i[1] + ", Daño estimado:" + str(i[2]))
            c = c + 1
        opcion = int(input("->"))
    print(str(x.nombre) +" ha utilizado " + str(x.habilidades[opcion-1][0]))
    dano= x.habilidades[opcion-1][2]* mult_ataque(x.habilidades[opcion-1],y)
    y.hp= y.hp-dano
    print(str(x.habilidades[opcion-1][0])+" Impacta Directamente! causando un daño de "+str(dano)+" puntos de salud")
    return y.hp

class Batalla():
    def __init__(self,contrincantes):
       self.contrincantes=contrincantes

    def turno(self):
        opcion1=10
        pokemon1= self.contrincantes[0].pokemones[0]
        pokemon2 = self.contrincantes[1].pokemones[0]
        inicial=mayor_nivel(pokemon1,pokemon2)
        print()
        print("Empieza el entrenador "+str(self.contrincantes[inicial].nombre))
        print("Con el pokemon: "+self.contrincantes[inicial].pokemones[0].nombre+", Hp: "+str(self.contrincantes[inicial].pokemones[0].hp))
        while opcion1 != 4:
            opcion1=input("""Cual va a ser tu movimiento?
                1) Utilizar Habilidad
                2) Regeneracion
                3) Cambiar Pokemón
                """)
            while opcion1!="1" and opcion1!="2" and opcion1!="3":
               print("ingreso incorrecto")
               opcion1 =input("""Cual va a ser tu movimiento?
                1) Utilizar Habilidad
                2) Regeneracion
                3) Cambiar Pokemón
                """)
            opcion1=int(opcion1)
            if opcion1==1:
                self.contrincantes[inicial-1].pokemones[0].hp=ataque(self.contrincantes[inicial].pokemones[0],self.contrincantes[inicial-1].pokemones[0])
                print("Hp de: "+self.contrincantes[inicial-1].pokemones[0].nombre+" es "+str(self.contrincantes[inicial-1].pokemones[0].hp))
                if self.contrincantes[inicial-1].pokemones[0].hp <= 0:
                    print("oow, el pokemon muere ")
                    a=[]
                    p=1
                    while p < len(self.contrincantes[inicial-1].pokemones):
                        print(self.contrincantes[inicial-1].pokemones[p])
                        a.append(self.contrincantes[inicial-1].pokemones[p])
                        p=p+1
                    self.contrincantes[inicial - 1].pokemones=a
                opcion1=4
            elif opcion1==2:
                if self.contrincantes[inicial].pokemones[0].veces_heleado<2:
                    if self.contrincantes[inicial].pokemones[0].nivel*3<self.contrincantes[inicial].pokemones[0].hp+20:
                        self.contrincantes[inicial].pokemones[0].hp=self.contrincantes[inicial-1].pokemones[0].nivel*3
                        print(self.contrincantes[inicial].pokemones[0].nombre+" es heleado a su vida maxima")
                        print("Hp de: " + self.contrincantes[inicial].pokemones[0].nombre + " ahora es " +str(self.contrincantes[inicial ].pokemones[0].hp))
                    else:
                        self.contrincantes[inicial].pokemones[0].hp=self.contrincantes[inicial].pokemones[0].hp+20
                        print(self.contrincantes[inicial].pokemones[0].nombre + " es heleado en 20 pts")
                        print("Hp de: " + self.contrincantes[inicial].pokemones[0].nombre + " ahora es " +str(self.contrincantes[inicial].pokemones[0].hp))
                    self.contrincantes[inicial].pokemones[0].veces_heleado=self.contrincantes[inicial].pokemones[0].veces_heleado+1
                    opcion1=4
                else:
                    print("Ya ha alcanzado el limite de curaciones, elija otra opcion")
            elif opcion1==3:
                print("¿Por que poquemon quiere intercambiar a "+self.contrincantes[inicial].pokemones[0].nombre+" ?")
                k=1
                for i in self.contrincantes[inicial].pokemones:
                    if k==1:
                        pass
                    else:
                        print(str(k)+") "+str(i))
                    k=k+1
                ingreso=input("-> ")
                while ingreso!="2" and ingreso!="3" and ingreso!="4" and ingreso!="5" and ingreso!="6" and ingreso!="1":
                    print("ingreso incorrecto")
                    ingreso=input("Ingrese nuevamente \n-> ")
                ingreso=int(ingreso)-1
                a=self.contrincantes[inicial].pokemones[0]
                b=self.contrincantes[inicial].pokemones[ingreso]
                self.contrincantes[inicial].pokemones[ingreso]=a
                self.contrincantes[inicial].pokemones[0]=b
                print("Ahora combate "+str(self.contrincantes[inicial].pokemones[0]))
                opcion1=4
        print()
        print("Continua el entrenador " + str(self.contrincantes[inicial-1].nombre))
        print("Con el pokemon: "+self.contrincantes[inicial-1].pokemones[0].nombre+", Hp: "+str(self.contrincantes[inicial-1].pokemones[0].hp))
        opcion1=0
        while opcion1 != 4:
            opcion1=input("""Cual va a ser tu movimiento?
                1) Utilizar Habilidad
                2) Regeneracion
                3) Cambiar Pokemón
                """)
            while opcion1!="1" and opcion1!="2" and opcion1!="3":
               print("ingreso incorrecto")
               opcion1 =input("""Cual va a ser tu movimiento?
                1) Utilizar Habilidad
                2) Regeneracion
                3) Cambiar Pokemón
                """)
            opcion1=int(opcion1)
            if opcion1==1:
                self.contrincantes[inicial].pokemones[0].hp=ataque(self.contrincantes[inicial-1].pokemones[0],self.contrincantes[inicial].pokemones[0])
                print("Hp de: "+self.contrincantes[inicial].pokemones[0].nombre+" es "+str(self.contrincantes[inicial].pokemones[0].hp))
                if self.contrincantes[inicial].pokemones[0].hp <= 0:
                    print("oow, el pokemon muere ")
                    a = []
                    p = 1
                    while p < len(self.contrincantes[inicial ].pokemones):
                        print(self.contrincantes[inicial ].pokemones[p])
                        a.append(self.contrincantes[inicial ].pokemones[p])
                        p = p + 1
                opcion1=4
            elif opcion1==2:
                if self.contrincantes[inicial-1].pokemones[0].veces_heleado<2:
                    if self.contrincantes[inicial-1].pokemones[0].nivel*3<self.contrincantes[inicial-1].pokemones[0].hp+20:
                        self.contrincantes[inicial-1].pokemones[0].hp=self.contrincantes[inicial-1].pokemones[0].nivel*3
                        print(self.contrincantes[inicial-1].pokemones[0].nombre+" es heleado a su vida maxima")
                        print("Hp de: " + self.contrincantes[inicial-1].pokemones[0].nombre + " ahora es " +str(self.contrincantes[inicial-1].pokemones[0].hp))
                    else:
                        self.contrincantes[inicial-1].pokemones[0].hp=self.contrincantes[inicial-1].pokemones[0].hp+20
                        print(self.contrincantes[inicial-1].pokemones[0].nombre + " es heleado en 20 pts")
                        print("Hp de: " + self.contrincantes[inicial-1].pokemones[0].nombre + " ahora es " +str(self.contrincantes[inicial-1].pokemones[0].hp))
                    self.contrincantes[inicial-1].pokemones[0].veces_heleado=self.contrincantes[inicial-1].pokemones[0].veces_heleado+1
                    opcion1=4
                else:
                    print("Ya ha alcanzado el limite de curaciones, elija otra opcion")
            elif opcion1==3:
                print("¿Por que poquemon quiere intercambiar a "+self.contrincantes[inicial-1].pokemones[0].nombre+" ?")
                k=1
                for i in self.contrincantes[inicial-1].pokemones:
                    if k==1:
                        pass
                    else:
                        print(str(k)+") "+str(i))
                    k=k+1
                ingreso=input("-> ")
                while ingreso!="2" and ingreso!="3" and ingreso!="4" and ingreso!="5" and ingreso!="6":
                    print("ingreso incorrecto")
                    ingreso=input("Ingrese nuevamente \n-> ")
                ingreso=int(ingreso)-1
                a=self.contrincantes[inicial-1].pokemones[0]
                b=self.contrincantes[inicial-1].pokemones[ingreso]
                self.contrincantes[inicial-1].pokemones[ingreso]=a
                self.contrincantes[inicial-1].pokemones[0]=b
                print("Ahora combate "+str(self.contrincantes[inicial-1].pokemones[0]))
                opcion1=4
                
if __name__ == "__main__":
  lista_pokemones=leer_poquemones("listapokemones.txt")
  print("Bienvenido a Batallas pokemon!!!\n")
  jug1=input("ingrese el nombre de el entrenador 1:\n->")
  jug2=input("ingrese el nombre de el entrenador 2:\n->")
  com=""
  while com!="fin":
      entrenador1=Entrenador(jug1)
      entrenador2=Entrenador(jug2)
      print(jug1+" Elija sus poquemones de la lista:")
      entrenador1.elegir_pokemon(lista_pokemones)
      print(jug2+" Elija sus poquemones de la lista:")
      entrenador2.elegir_pokemon(lista_pokemones)
      batalla=Batalla([entrenador1,entrenador2])
      while len(entrenador1.pokemones)!=0 and len(entrenador2.pokemones)!=0 :
          batalla.turno()
      print("Fin del juego, el jugador ganador es: ")
      if len(entrenador1.pokemones)!=0:
          print(jug1)
      elif len(entrenador2.pokemones)!=0:
          print(jug2)
      fin=input("¿Desea jugar nuevamente?\n1) si\n2) no\n")
      if fin=="2":
          com="fin"
if __name__ == "__main__":
  lista_pokemones=leer_poquemones("listapokemones.txt")
  jug1=input("ingrese el nombre de el entrenador 1:\n->")
  jug2=input("ingrese el nombre de el entrenador 2:\n->")
  com=""
  while com!="fin":
      entrenador1=Entrenador(jug1)
      entrenador2=Entrenador(jug2)
      print(jug1+" Elija sus poquemones de la lista:")
      entrenador1.elegir_pokemon(lista_pokemones)
      print(jug2+" Elija sus poquemones de la lista:")
      entrenador2.elegir_pokemon(lista_pokemones)
      batalla=Batalla([entrenador1,entrenador2])
      while len(entrenador1.pokemones)!=0 and len(entrenador2.pokemones)!=0 :
          batalla.turno()  
      print("Fin del juego, el jugador ganador es: ")
      if len(entrenador1.pokemones)!=0:
          print(jug1)
      elif len(entrenador2.pokemones)!=0:
          print(jug2)
      fin=input("¿Desea jugar nuevamente?\n1) si\n2) no\n")
      if fin=="2":
          com="fin"