if __name__ == "__main__":
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
            self.HPMax = 3*self.nivel
        def __str__(self):

            return "{0} ({1})".format(self.nombre[0].upper()+self.nombre[1:], self.tipo) #retorna el nombre y tipo del pokemón
        def __vida__(self):
            linea = "-"*self.HPMax
            lineahp = "="*self.HP
            lineahpneg = " "*(self.HPMax-self.HP)+"|"
            return ("{0} Nivel: {1}".format(self.nombre, self.nivel) + """
    {0}
    {1}{2}
    {3}""".format(linea, lineahp, lineahpneg, linea))
                
    archivo_datos = open("pokemon.csv","r") #abrimos el archivo con los pokemones

    for linea in archivo_datos:
        
        linea = linea.strip() #listas de cada fila
        linea = linea.split(",") #Cada fila hace listas separando por la ","
        lista_pokemon.append(pokemon(linea[0],linea[1])) #[[pokemón1(nombre1,tipo1)],[pokemón2(nombre2,tipo2)],[pokemón3(nombre3,tipo3)],...

    archivo_datos.close() #cerramos el archivo con los pokemones
    lista_nombres_pokemones = [] #Creo lista para poner los nombres de los distintos pokemones
    for pokemon in lista_pokemon:
        lista_nombres_pokemones.append(str(pokemon.nombre)) #Agrego el atributo nombre de cada pokemon en la lista
    def pedir_lista(): #Me entrega una lista "bonita" con los pokemones y su tipo
        for i in range(len(lista_pokemon)):
            print("{0}) {1}".format(i+1, str(lista_pokemon[i])))

    class Entrenador:
        def __init__(self,nombre):
            self.nombre=nombre
            self.pokemones=[]
            self.is_battle = ""
        def agregar_pokemon(self,pokemon):
            if len(self.pokemones)>6:
                print("Ya hay 6 pokemones")
                return False
            self.pokemones.append(pokemon)

        def __str__(self):
            return "{0}{1}".format(self.nombre[0].upper(), self.nombre[1:])
        def eliminar_pokemon(self,pokemon):
            if pokemon not in self.pokemones:
                print("No puedes quitar un pokemon que no tienes")
                return False
            self.pokemones.remove(pokemon)
        def lista_pkmn(self):
            s=""
            for pokemon in self.pokemones:
                s+=str(pokemon)+"\n"*2
            print(s)
        def is_battler(self, pokemon):
            self.is_battle = pokemon
        def cambiar_pokemon(self, posicion):
            self.pokemones[posicion], self.pokemones[0] = self.pokemones[0], self.pokemones[posicion]
            
    class Batalla:
        def __init__(self,contrincantes):
            if not isinstance(contrincantes[0], object) or not isinstance(contrincantes[1], object) or len(contrincantes)!=2:
                print("Sus contrincantes no son validos")
                return False
            self.contrincantes=contrincantes

        def atacar(self,posicion_atacante):  #1ro lista siemppre
            if posicion_atacante not in range(2):
                return False
            pokemon_atacante=self.contrincantes[posicion_atacante].pokemones[0]
            pokemon_atacado=self.contrincantes[posicion_atacante-1].pokemones[0]
            ataque=randint(0, int(((self.contrincantes[posicion_atacante].pokemones[0].nivel/25)*2.6)//1))
            if pokemon_atacante.tipo=="agua":
                if pokemon_atacado.tipo=="fuego":
                    ataque*=2
                elif pokemon_atacado.tipo=="hierba":
                    ataque/=2
                elif pokemon_atacado.tipo=="agua":
                    ataque/=2
            if pokemon_atacante.tipo=="fuego":
                if pokemon_atacado.tipo=="fuego":
                    ataque/=2
                elif pokemon_atacado.tipo=="hierba":
                    ataque*=2
                elif pokemon_atacado.tipo=="agua":
                    ataque/=2
            if pokemon_atacante.tipo=="electricidad":
                if pokemon_atacado.tipo=="electricidad":
                    ataque/=2
                elif pokemon_atacado.tipo=="hierba":
                    ataque/=2
                elif pokemon_atacado.tipo=="agua":
                    ataque*=2
            if pokemon_atacante.tipo=="hierba":
                if pokemon_atacado.tipo=="fuego":
                    ataque/=2
                elif pokemon_atacado.tipo=="hierba":
                    ataque/=2
                elif pokemon_atacado.tipo=="agua":
                    ataque*=2
            print("{0} de {1} le ha inflingido {2} a {3}".format(self.contrincantes[posicion_atacante].pokemones[0].ataque_nombre, self.contrincantes[posicion_atacante].pokemones[0].nombre, ataque, self.contrincantes[posicion_atacante-1].pokemones[0].nombre))
            pokemon_atacado.HP-=int(ataque//1)
            self.contrincantes[(posicion_atacante+1)%2].pokemones[0]=pokemon_atacado
            if pokemon_atacado.HP<=0:
                self.contrincantes[(posicion_atacante+1)%2].pokemones.remove(pokemon_atacado)

        def recuperar(self,posicion_contrincante):
            self.contrincantes[posicion_contrincante].pokemones[0].HP+=20

    #_____________________Flujo_______________________________
    nombre1 = input("Ingrese el nombre del 1er contrincante: ")
    nombre2 = input("Ingrese el nombre del 2do contrincante: ")
    contrincante1=Entrenador(nombre1)
    contrincante2=Entrenador(nombre2)
    batalla=Batalla([contrincante1,contrincante2])
    for i in range(2):
        print("\nTurno de {0}{1}".format(str(batalla.contrincantes[i]), "\n"))
        while len(batalla.contrincantes[i].pokemones)<6:
            accion=input("¿Desea agregar o quitar un pokemon?\n")
            if accion.lower()=="agregar":
                pedir_lista()
                pokemon=int(input("¿Cual pokemon quiere?\n"))
                pkmn=lista_pokemon[pokemon-1]
                batalla.contrincantes[i].agregar_pokemon(pkmn)
                lista_pokemon.pop(pokemon-1)
                
            elif accion.lower()=="quitar":
                if len(batalla.contrincantes[i].pokemones) >= 1:
                    for j in batalla.contrincantes[i].pokemones:
                        print("{0}) {1}".format(batalla.contrincantes[i].pokemones.index(j)+1, str(j)))
                    pokemon=int(input("¿Cual pokemon quiere eliminar?\n"))
                    batalla.contrincantes[i].eliminar_pokemon(batalla.contrincantes[i].pokemones[pokemon-1])
                else:
                    pass
            if len(batalla.contrincantes[i].pokemones) > 0 :
                print("Equipo:")
                for j in batalla.contrincantes[i].pokemones:
                            print("{0}) {1}".format(batalla.contrincantes[i].pokemones.index(j)+1, str(j)))
            elif len(batalla.contrincantes[i].pokemones) == 0 :
                print("{0} no tiene pokemones".format(str(batalla.contrincantes[i])))
    while len(contrincante1.pokemones) != 0 or len(contrincante2.pokemones) != 0:
        turno = 1
        for i in range(len(batalla.contrincantes)):
            print("=================================Turno de {0}==============================================".format(str(batalla.contrincantes[i])))
            breaker = True
            while breaker:
                if isinstance(batalla.contrincantes[i].is_battle, str):
                    print("Equipo:")
                    for j in batalla.contrincantes[i].pokemones:
                        print("{0}) {1}".format(batalla.contrincantes[i].pokemones.index(j)+1, str(j)))
                    n2 = int(input("Elija pokemon: "))
                    batalla.contrincantes[i].is_battler(batalla.contrincantes[i].pokemones[n2-1])
                    batalla.contrincantes[i].cambiar_pokemon(n2-1)
                else:
                    print(batalla.contrincantes[i].pokemones[0].__vida__())
                    n3 = input("""¿Que desea hacer?
        1) Atacar       2) Curar
        3) Cambiar pkmn 4) Correr
        """)
                    if n3 == "1":
                        batalla.atacar(i)
                        print(batalla.contrincantes[i-1].pokemones[0].__vida__())
                        breaker = False

                    elif n3 == "2":
                        batalla.recuperar(i)
                        breaker = False
                    elif n3 == "3":
                        print("Equipo:")
                        for j in batalla.contrincantes[i].pokemones:
                            print("{0}) {1}".format(batalla.contrincantes[i].pokemones.index(j)+1, str(j)))
                        n4 = int(input("Elija pokemon: "))
                        batalla.contrincantes[i].is_battle(batalla.contrincantes[i].pokemones[n4-1])
                        batalla.contrincantes[i].cambiar_pokemon(n4-1)
                        breaker = False
                    elif n3 == "4":
                        print("No corra de su destino")
    for i in range(len(batalla.contrincantes)):
        if len(batalla.contrincantes[i].pokemones) == 0:
            print("{0} ha ganado la batalla!".format(str(batalla.contrincantes[i-1])))