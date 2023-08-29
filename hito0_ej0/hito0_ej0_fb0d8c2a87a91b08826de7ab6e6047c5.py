import random
class Pokemon:
    def __init__(self,nombre,tipo,nivel,hp,ataques):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.hp = hp
        self. ataques = ataques
class MiEquipo:
    def __init__(self):
        self.equipo = []

    def agregar_pokemon(self,pokemon):
        self.equipo.append(pokemon)

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print("""Nombre: {0}
                     Tipo: {1}
                     Nivel: {2}
                     HP: {3}
                     Ataques: {4}""".format(pokemon.nombre,pokemon.tipo,pokemon.nivel,pokemon.hp,pokemon.ataques))



class batalla:
    def __init__(self,entrenador1,entrenador2):
        self.pokemon1 = entrenador1.pokemon
        self.pokemon2 = entrenador2.pokemon

    def atacar(self,ataque):
        ataque1 = random.randint(0,((pokemon1.nivel/25)*(2.6))//1)
        ataque2 = random.randint(0, ((pokemon2.nivel / 25) * (2.6))//1)
        if pokemon1.tipo == "agua" and (pokemon2.tipo == "hierba" or pokemon2.tipo == "agua"):
            ataque1 = ataque/2
            ataque2 = ataque2/2
        elif  pokemon1.tipo == "fuego" and (pokemon2.tipo == "fuego" or pokemon2.tipo == "agua"):
            ataque1 = ataque1/2
            ataque2 = ataque2/2
        elif pokemon1.tipo == "electricidad" and (pokemon2.tipo == "hierba" or pokemon2.tipo == "electricidad"):
            ataque1 = ataque1 / 2
            ataque2 = ataque2 / 2
        elif pokemon1.tipo == "hierba" and (pokemon2.tipo == "hierba" or pokemon2.tipo == "fuego"):
            ataque1 = ataque1 / 2
            ataque2 = ataque2 / 2
