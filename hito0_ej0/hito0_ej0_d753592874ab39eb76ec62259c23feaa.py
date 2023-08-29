### Pokemones ###
import random
from tkinter import *
#from pip3 import *

class Pokemon:
    def __init__(self,nombre,tipo,nivel):
        self.nombre=nombre
        self.nivel=nivel
        self.tipo=tipo
        self.ataque=0
        self.vida_total=self.nivel * 3
        self.vida_actual=self.nivel * 3

    def Asignar_fuerza_ataque(self):
        self.ataque = int(random.random() * (self.nivel / 25) * 2.6)
        print(self.ataque)

    def Pierde_vida(self,golpe):
        self.vida_actual-=golpe
        print("Has perdido vida {0}!".format(self.nombre))

    def Recupera_vida(self):
        self.vida_actual=self.vida_actual+(self.vida_total/2)

    def __repr__(self):
        return ("\n"+"\n Nombre: "+str(self.nombre)+"\n Nivel: "+str(self.nivel)+"\n Tipo: "+str(self.tipo)+" Ataque: "+ str(self.ataque)+"\n Vida: "+str(self.vida_total)+"\n Vida actual: "+str(self.vida_actual))

    def __str__(self):
        return(self.__repr__())

    

class Entrenador:
    def __init__(self, nombre):
        self.nombre=nombre
        self.pokemones=[]

    def Recupera_pokemon(self,pokemon):
        pokemon.Recupera_vida()
        print("Has recuperado la vida de tu pokemon.")

    def __repr__(self):
        return ("\n"+"\n Nombre: "+str(self.nombre)+"\n TUS POKEMONES: "+str(self.pokemones)+"\n")

    def __str__(self):
        return(self.__repr__())

    def mostrar_mis_pokemones(self):
        for pokemon in self.pokemones:
            print(pokemon.nombre)
            print(pokemon.nivel)
            print(pokemon.vida_actual)
           
"""
def Crear_entrenador(entrenador):
    print(Pokemones)
    print("\nEl primer pokemon de tu lista será tu pokemon de partida en el juego.")
    print("No puedes repetir tus Pokemones. Solo puedes elegir 6 de la lista.")

    i=0
    while i<6:
        pokemon_a_elegir=int(input("\n Elige un pokemon de la lista diciendo su número: \n(-1) Para mostrar la lista de pokemones  \n(-2)Para salir \n "))
        if pokemon_a_elegir==-1:
            i-=1
            print(Pokemones)
        elif pokemon_a_elegir==-2:
            break
        else:
            if Pokemones[pokemon_a_elegir] not in entrenador.pokemones:
                entrenador.pokemones.append(Pokemones[pokemon_a_elegir])
            else:
                print("Inténtalo de nuevo")
                i-=1
                print(Pokemones)
        i+=1

i=0
entrenadores=[]
while i<2:
    a=i+1
    Nombre_entrenador=input("Bienvenido entrenador {0}. Ingresa tu nombre: ".format(a))
    entrenador=Entrenador(Nombre_entrenador)
    entrenadores.append(entrenador)
    i+=1

Entrenadores=[]
for entrenador in entrenadores:
    a=Crear_entrenador(entrenador)
    Entrenadores.append(a)

### Crear funcion Atacar
    # Funcion cambiar pokemon
    # Funcion recuperar
    
#for pokemon in Pokemones:
#    print(pokemon)
"""
############################################################################################################

class JUEGO_POKEMON:

    def __init__(self):
        self.entrenadores=[]
        self.Pokemones=[]
        self.imagenes = {}
        principal=Tk()
        principal.title("Pokemon")
        self.Crea_lista_general_Pokemones()

        self.vacio=PhotoImage(file="vacio.png")
        self.gris=PhotoImage(file="gris.png")
        self.ataque=PhotoImage(file="ataque.png")
        self.tablero = []
        for i in range(3):
            fila = []
            for j in range(6):
                b1 = Button(principal, image=self.vacio, width="80", height="80")
                b1.bind("<Button-1>", escoger)
                b1.x = i
                b1.y = j
                b1.pokemon=""
                b1.ocupado=False
                b1.grid(row=i, column=j)
                fila.append(b1)
            self.tablero.append(fila)
        b1 = Button(principal,image=self.ataque, width="100", height="100")
        b1.grid(row=4,column=0)
        b1.bind("<Button-1>", self.atacar)


    def Crea_lista_general_Pokemones(self):   
        archivo_pokemones=open("pokemon.csv","r")
        for linea in archivo_pokemones.read().split("\n"):
            if linea == "":
                continue
            m=linea.split(",")
            #linea.strip().split(",")
            a=random.randint(5,25)
            pokemon1=Pokemon(m[0],m[1],a)
            pokemon1.Asignar_fuerza_ataque()
            self.Pokemones.append(pokemon1)
            imagen = PhotoImage(file=m[0] + ".png")
            self.imagenes[m[0]] = imagen
        archivo_pokemones.close()

        ### Inicio Entrenadores ####
        #self.entrenadores=self.Crea_jugadores()
        #####print("Eres chico(0) o chica(1)?")
   
    def Crear_entrenador_pokemones(self, entrenador):
        print(self.Pokemones)
        print("\nEl primer pokemon de tu lista será tu pokemon de partida en el juego.")
        print("No puedes repetir tus Pokemones. Solo puedes elegir 6 de la lista.")

        i=0
        while i<6:
            pokemon_a_elegir=int(input("\n Elige un pokemon de la lista diciendo su número: \n(-1) Para mostrar la lista de pokemones  \n(-2)Para salir \n(-3)Mostrar los pokemones elegidos \n "))
            if pokemon_a_elegir==-1:
                i-=1
                print(self.Pokemones)
            elif pokemon_a_elegir==-2:
                break
            elif pokemon_a_elegir==-3:
                print(entrenador.mostrar_mis_pokemones())
            else:
                if self.Pokemones[pokemon_a_elegir] not in entrenador.pokemones:
                    entrenador.pokemones.append(self.Pokemones[pokemon_a_elegir])
                else:
                    print("Inténtalo de nuevo")
                    i-=1
                    print(self.Pokemones)
            i+=1
            return entrenador

    def Crea_jugadores(self):
        i=0
        entrenadores=[]
        while i<2:
            a=i+1
            Nombre_entrenador_pokemones=input("Bienvenido entrenador {0}. Ingresa tu nombre: ".format(a))
            entrenador=Entrenador(Nombre_entrenador_pokemones)
            entrenadores.append(entrenador)
            i+=1

        for entrenador in entrenadores:
            a=self.Crear_entrenador_pokemones(entrenador)
            self.entrenadores.append(a)
        return self.entrenadores
        
        
    def Turno(entrenador1,entrenador2):
        opcion=print("Qué deseas hacer? (0)Atacar   (1)Cambiar Pokemon   (2)Recuperar a tu Pokemon")
        if opcion==0:
            self.Atacar(entrenador1,entrenador2)
        elif opcion==1:
            otro_pokemon=input("Que pokemon quires que combata?")
            self.Cambiar_Pokemon(entrenador1,otro_pokemon)
        elif opcion==2:
            self.Recuperar_Pokemon(entrenador1)
        else:
            print("Intente de nuevo")
            return
        


    def atacar(self, evento):
        pokemon1=juego.tablero[1][2].pokemon
        pokemon2=juego.tablero[1][3].pokemon
        if pokemon1!="" and pokemon2!="":
            messagebox.showinfo("Pokemon","Se enfrentan {0} y {1}".format(pokemon1,pokemon2))
        
        else:
            messagebox.showinfo("Pokemon","Cada contrincante debe seleccionar su pokemon")

        #while pokemon1.vida_actual>0 or pokemon2.vida_actual>0:
        if pokemon1.tipo=="agua":
            if pokemon2.tipo=="fuego":
                a=pokemon1.ataque*2
            elif pokemon2.tipo=="hierba" or pokemon2.tipo=="agua":
                a=(pokemon1.ataque)*0.5
            else:
                a=0
                print("Tu ataque no surtió efecto {0}.".format(pokemon2.nombre))
                return
            pokemon2.Pierde_vida(a)
            
        if pokemon1.tipo=="fuego":
            if pokemon2.tipo=="hierba":
                a=pokemon1.ataque*2
            elif pokemon2.tipo=="fuego" or pokemon2.tipo=="agua":
                a=(pokemon1.ataque)*0.5
            else:
                a=0
                print("Tu ataque no surtió efecto {0}.".format(pokemon1.nombre))
                return
            pokemon2.Pierde_vida(a)

        if pokemon1.tipo=="electricidad":
            if pokemon2.tipo=="agua":
                a=pokemon1.ataque*2
            elif pokemon2.tipo=="hierba" or pokemon2.tipo=="electricidad":
                a=(pokemon1.ataque)*0.5
            else:
                a=0
                return
                print("Tu ataque no surtió efecto {0}.".format(pokemon1.nombre))
            pokemon2.Pierde_vida(a)

        if pokemon1.tipo=="hierba":
            if pokemon2.tipo=="agua":
                a=pokemon1.ataque*2
            elif pokemon2.tipo=="hierba" or pokemon2.tipo=="fuego":
                a=(pokemon1.ataque)*0.5
            else:
                a=0
                print("Tu ataque no surtió efecto {0}.".format(pokemon1.nombre))
                return
            
            pokemon2.Pierde_vida(a)
###
        if pokemon2.tipo=="agua":
            if pokemon1.tipo=="fuego":
                a=pokemon2.ataque*2
            elif pokemon1.tipo=="hierba" or pokemon1.tipo=="agua":
                a=(pokemon2.ataque)*0.5
            else:
                a=0
                print("Tu ataque no surtió efecto {0}.".format(pokemon2.nombre))
                return
            pokemon1.Pierde_vida(a)
            
        if pokemon2.tipo=="fuego":
            if pokemon1.tipo=="hierba":
                a=pokemon2.ataque*2
            elif pokemon1.tipo=="fuego" or pokemon1.tipo=="agua":
                a=(pokemon2.ataque)*0.5
            else:
                a=0
                print("Tu ataque no surtió efecto {0}.".format(pokemon2.nombre))
                return
            pokemon1.Pierde_vida(a)

        if pokemon2.tipo=="electricidad":
            if pokemon1.tipo=="agua":
                a=pokemon2.ataque*2
            elif pokemon1.tipo=="hierba" or pokemon1.tipo=="electricidad":
                a=(pokemon2.ataque)*0.5
            else:
                a=0
                return
                print("Tu ataque no surtió efecto {0}.".format(pokemon2.nombre))
            pokemon1.Pierde_vida(a)

        if pokemon2.tipo=="hierba":
            if pokemon1.tipo=="agua":
                a=pokemon2.ataque*2
            elif pokemon1.tipo=="hierba" or pokemon1.tipo=="fuego":
                a=(pokemon2.ataque)*0.5
            else:
                a=0
                print("Tu ataque no surtió efecto {0}.".format(pokemon2.nombre))
                return
            
            pokemon1.Pierde_vida(a)



            
            
    def Cambiar_Pokemon(self,entrenador1,otro_pokemon):
        lista_nueva=[]
        otro_pokemon=otro_pokemon.upper()
        for pokemon in entrenador1.pokemones():
            if otro_pokemon==pokemon.nombre:
                lista_nueva[0]=(pokemon)
        for pokemon in entrenador1.pokemones():
            if otro_pokemon!=pokemon.nombre:
                lista_nueva.append(pokemon)
        self.entrenador1.pokemones=lista_nueva

    def Recuperar_Pokemon(self,entrenador1):
        entrenador1.Recupera_pokemon(entrenador1.pokemones[0])

    def Juego(self):
        self.Crea_lista_general_Pokemones()
        self.entrenadores=self.Crea_jugadores()
        i=0
        while i < len(self.entrenadores):
            print(self.entrenadores[i])
            i+=1
        #print(self.entrenadores[0].pokemones[0].nivel)
        #if self.entrenadores[0].pokemones[0].nivel>self.entrenadores[1].pokemones[0].nivel:
        #    Jugador1=self.entrenadores[0]
         #   Jugador2=self.entrenadores[1]
        #else:
         #   Jugador1=self.entrenadores[1]
          #  Jugador2=self.entrenadores[0]

def escoger(evento):
    if evento.widget.x!=1:
        if evento.widget.pokemon=="":
            pokemon=random.choice(juego.Pokemones)
            juego.Pokemones.remove(pokemon)
            evento.widget["image"]=juego.imagenes[pokemon.nombre]
            evento.widget.pokemon=pokemon
            evento.widget.ocupado=True
        elif evento.widget.ocupado:
            slot=2 if evento.widget.x==0 else 3
            if juego.tablero[1][slot].ocupado==False:
                juego.tablero[1][slot]["image"]=evento.widget["image"]
                juego.tablero[1][slot].ocupado=True
                juego.tablero[1][slot].contrincante=evento.widget.y
                juego.tablero[1][slot].pokemon=evento.widget.pokemon
                evento.widget["image"]=juego.gris
                evento.widget.ocupado=False
            else:
                messagebox.showinfo("Pokemon","Ya estas usando a "+juego.tablero[1][slot].pokemon.nombre)
    elif evento.widget.y in [2,3]:
        if evento.widget.ocupado:
            jugador=0 if evento.widget.y==2 else 2
            juego.tablero[jugador][evento.widget.contrincante]["image"]=evento.widget["image"]
            juego.tablero[jugador][evento.widget.contrincante].ocupado=True
            evento.widget["image"]=juego.vacio
            evento.widget.ocupado=False
    

def atacar(evento):
    pokemon1=juego.tablero[1][2].pokemon
    pokemon2=juego.tablero[1][3].pokemon
    if pokemon1!="" and pokemon2!="":
        messagebox.showinfo("Pokemon","Se enfrentan {0} y {1}".format(pokemon1,pokemon2))
    
    else:
        messagebox.showinfo("Pokemon","Cada contrincante debe seleccionar su pokemon")


"""            
        while len(Jugador1.pokemones)>0 or len(Jugador2.pokemones)>0:
            
            self.Turno(Jugador1,Jugador2)
            if Jugador1.pokemones[0].vida_actual<=0:
                Jugador1.pokemones.remove(Jugador1.pokemones[0])
            if Jugador2.pokemones[0].vida_actual<=0:
                Jugador2.pokemones.remove(Jugador1.pokemones[0])
                
            self.Turno(Jugador1,Jugador2)
            if Jugador1.pokemones[0].vida_actual<=0:
                Jugador1.pokemones.remove(Jugador1.pokemones[0])
            if Jugador2.pokemones[0].vida_actual<=0:
                Jugador2.pokemones.remove(Jugador1.pokemones[0])          

        if len(Jugador1.pokemones)>0:
            print("Felicidades, ganaste entrenador {0}".format(Jugador1.nombre))

        if len(Jugador2.pokemones)>0:
            print("Felicidades, ganaste entrenador {0}".format(Jugador2.nombre))
"""


###### Principal ######

juego=JUEGO_POKEMON()