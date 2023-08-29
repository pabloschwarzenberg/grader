# hola profesor, los integrantes son:
#Eitan Dvorquez
#Ana Arredondo
#Camilo Sanchez
#Felipe Donoso
#Isaac Gallegos
#Alexander Barrera

class Pokemon:
    def __init__(self,nombre,tipo,habilidades):
        n=random.randint(5,25)
        self.nombre=nombre
        self.nivel=n
        self.tipo=tipo
        self.habilidades=habilidades
        self.hp=n*3

    def __str__(self):
        a=self.nombre+", Nivel: "+str(self.nivel)+", Hp: "+str(self.hp)+", "+self.tipo+", Habilidades: "
        for hab in self.habilidades:
            a=a+"  ->"
            for part in hab:
                a=a+","+str(part)
        return a
    pass
    
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
            elegidos = str(input("Elija un pokemon: "))
            while elegidos.isdigit() == False or int(elegidos) > len(lista_pokemones):
                print("No existe ese pokemon, elija otro.")
                elegidos = str(input("Elija un pokemon: "))
            self.pokemones.append(listapokemon[int(elegidos)])
        return

    def mostrar_pokemones (self):
        for p in self.pokemones:
            print(p)
        return

    pass
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
    opcion=int(input(""))
    while opcion >= len(x.habilidades):
        print("ingreso incorrecto")
        print("Seleccione una de las siguientes Habilidades:")
        c = 1
        for i in x.habilidades:
            print(str(c) + ")" + i[0] + ", tipo:" + i[1] + ", Daño estimado:" + str(i[2]))
            c = c + 1
    print(str(x.nombre) +" ha utilizado " + str(x.habilidades[opcion-1][0]))
    dano= x.habilidades[opcion-1][2]* mult_ataque(x.habilidades[opcion-1],y)
    y.hp= y.hp-dano
    print(str(x.habilidades[opcion-1][0])+" Impacta Directamente! causando un daño de "+str(dano)+" puntos de salud")
    return y.hp
    
class Batalla:
    def __init__(self,contrincantes):
       self.contrincantes=contrincantes

    def turno(self):
        pokemon1= self.contrincantes[0].pokemones[0]
        pokemon2 = self.contrincantes[1].pokemones[0]
        inicial=mayor_nivel(pokemon1,pokemon2)
        print("Empieza el entrenador "+str(self.contrincantes[inicial].nombre))
        print("Con el poquemon: "+self.contrincantes[inicial].pokemones[0].nombre+", Hp: "+str(self.contrincantes[inicial].pokemones[0].hp))
        opcion1= int(input("""Cual va a ser tu movimiento?
        1) Utilizar Habilidad
        2) Regeneracion
        3) Cambiar Pokemón
        """))
        while opcion1!=0 and opcion1!=1 and opcion1!=2:
            print("ingreso incorrecto")
            opcion1 = int(input("""Cual va a ser tu movimiento?
                    1) Utilizar Habilidad
                    2) Regeneracion
                    3) Cambiar Pokemón
                    """))
        if opcion1==1:
            self.contrincantes[inicial-1].pokemones[0].hp=ataque(self.contrincantes[inicial].pokemones[0],self.contrincantes[inicial-1].pokemones[0])
            print("Hp de: "+self.contrincantes[inicial-1].pokemones[0].nombre+" es "+self.contrincantes[inicial-1].pokemones[0].hp)
            if self.contrincantes[inicial-1].pokemones[0].hp <= 0:
                print("oow, el pokemon muere ")
                self.contrincantes[inicial-1].pokemones.pop[0]


        print("Continua el entrenador "+str(self.contrincantes[inicial-1].nombre))
        print("Con el poquemon: "+self.contrincantes[inicial-1].pokemones[0].nombre+", Hp: "+str(self.contrincantes[inicial-1].pokemones[0].hp))
        opcion1= int(input("""Cual va a ser tu movimiento?
        1) Utilizar Habilidad
        2) Regeneracion
        3) Cambiar Pokemón
        """))
        while opcion1!=1 and opcion1!=2 and opcion1!=3:
            print("ingreso incorrecto")
            opcion1 = int(input("""Cual va a ser tu movimiento?
                    1) Utilizar Habilidad
                    2) Regeneracion
                    3) Cambiar Pokemón
                    """))
        if opcion1==1:
            self.contrincantes[inicial].pokemones[0].hp = ataque(self.contrincantes[inicial-1].pokemones[0],self.contrincantes[inicial].pokemones[0])
            print("Hp de: " + self.contrincantes[inicial].pokemones[0].nombre + " es " +self.contrincantes[inicial].pokemones[0].hp)
            if self.contrincantes[inicial].pokemones[0].hp <= 0:
                print("oow, el pokemon muere ")
                self.contrincantes[inicial].pokemones.pop[0]        
    pass
      