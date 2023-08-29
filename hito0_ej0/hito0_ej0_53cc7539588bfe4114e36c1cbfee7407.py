import random
def obtener_pokemon(numero):
    numero=numero-1
    pokemon=open("pokemon.txt","r")
    pokemon_l=list(pokemon)
    for n in range(len(pokemon_l)):
        pokemon_l[n]=pokemon_l[n].split(",")
        for e in range(3):
            pokemon_l[n][e]=pokemon_l[n][e].rstrip()
    for z in range(len(pokemon_l)):
        if numero==z:
            return pokemon_l[z][0]
def obtener_lista():
    pokemon=open("pokemon.txt","r")
    pokemon_l=list(pokemon)
    for n in range(len(pokemon_l)):
        pokemon_l[n]=pokemon_l[n].split(",")
        for e in range(3):
            pokemon_l[n][e]=pokemon_l[n][e].rstrip()
    for l in range(len(pokemon_l)):
        print(l+1,") Nombre : ",pokemon_l[l][0])
        print("    Tipo : ",pokemon_l[l][1])
        print("    Ataque : ",pokemon_l[l][2])
    pokemon.close
    return()

def info_pokemon(numero):
    numero=numero-1
    pokemon=open("pokemon.txt","r")
    pokemon_l=list(pokemon)
    for n in range(len(pokemon_l)):
        pokemon_l[n]=pokemon_l[n].split(",")
        for e in range(3):
            pokemon_l[n][e]=pokemon_l[n][e].rstrip()
    return pokemon_l[numero]
def puntos_ataque(nivel,tipo1,tipo2):
    ataque=int(random.randint(0,((nivel/25)*2.6)))
    if tipo1=="agua" and (tipo2=="hierba" or tipo2=="agua"):
        ataque=ataque/2
        print("No es muy efectivo...")
    elif tipo1=="agua" and tipo2=="fuego":
        ataque=ataque*2
        print("Es muy efectivo!")
    elif tipo1=="fuego" and (tipo2=="fuego" or tipo2=="agua"):
        ataque=ataque/2
        print("No es muy efectivo...")
    elif tipo1=="fuego" and tipo2=="hierba":
        ataque=ataque*2
        print("Es muy efectivo!")
    elif tipo1=="electricidad" and (tipo2=="hierba" or tipo2=="electricidad"):
        ataque=ataque/2
        print("No es muy efectivo...")
    elif tipo1=="electricidad" and tipo2=="agua":
        ataque=ataque*2
        print("Es muy efectivo!")
    elif tipo1=="hierba" and (tipo2=="fuego" or tipo2=="hierba"):
        ataque=ataque/2
        print("No es muy efectivo...")
    elif tipo1=="hierba" and tipo2=="agua":
        ataque=ataque*2
        print("Es muy efectivo!")
    return ataque

def definir_nivel():
    nivel=random.randint(5,25)
    return nivel


def heal(hp):
    hp=hp+20
    return hp


class Pokemon:
    def __init__(self,nombre,tipo,ataque,nivel,HP):
        self.nombre=nombre
        self.tipo=tipo
        self.ataque=ataque
        self.nivel=random.randint(5,25)
        self.HP=(self.nivel)*3

    def __repr__(self):
        return self.nombre
    


class Entrenador:
    def __init__(self,nombreentrenador):
        self.nombreentrenador=nombreentrenador
        self.pokemones=[]
        

    def agregar(self,pokemon):
        self.pokemones.append(pokemon)

    def __repr__(self):
        s=""
        for pokemon in self.pokemones:
            s+=pokemon.nombre+" Nivel: "+str(pokemon.nivel)+"   HP: "+str(pokemon.HP)+"\n"
        return s
            
class Batalla:
    def __init__(self,entrenador1,entrenador2):
        self.entrenador1=entrenador1
        self.entrenador2=entrenador2
        self.multiplicador=1
        self.ataque1=random.randint(0,int(((self.entrenador1.pokemones[0].nivel)/5)+2.6))
        self.ataque2=random.randint(0,int(((self.entrenador2.pokemones[0].nivel)/5)+2.6))
        
    
    def atacar(self,entrenador1,entrenador2):
            if self.entrenador1.pokemones[0].tipo=="agua":
                if self.entrenador2.pokemones[0].tipo=="fuego":
                    self.multiplicador=2
                elif self.entrenador2.pokemones[0].tipo=="hierba" or self.entrenador2.pokemones[0].tipo=="agua":
                    self.multiplicador=0.5
            elif self.entrenador1.pokemones[0].tipo=="fuego":
                if self.entrenador2.pokemones[0].tipo=="hierba":
                    self.multiplicador=2
                elif self.entrenador2.pokemones[0].tipo=="agua" or self.entrenador2.pokemones[0].tipo=="fuego":
                    self.multiplicador=0.5
            elif self.entrenador1.pokemones[0].tipo=="electricidad":
                if self.entrenador2.pokemones[0].tipo=="agua":
                    self.multiplicador=2
                elif self.entrenador2.pokemones[0].tipo=="electricidad" or self.entrenador2.pokemones[0].tipo=="hierba":
                    self.multiplicador=0.5
            elif self.entrenador1.pokemones[0].tipo=="hierba":
                  if self.entrenador2.pokemones[0].tipo=="agua":
                      self.multiplicador=2
                  elif self.entrenador2.pokemones[0].tipo=="hierba" or self.entrenador2.pokemones[0].tipo=="fuego":
                      self.multiplicador=0.5
            self.entrenador2.pokemones[0].HP=self.entrenador2.pokemones[0].HP-self.ataque1*self.multiplicador

    def cambiar_pokemon(self,entrenador1,n):
 
        self.entrenador1.pokemones.insert(0,self.entrenador1.pokemones[n])
        self.entrenador1.pokemones.pop(n+1)

    def recuperar(self,entrenador1):
        self.entrenador1.pokemones[0].HP+=20