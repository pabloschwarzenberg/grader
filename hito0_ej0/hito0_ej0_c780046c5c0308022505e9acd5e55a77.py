import random


class pokemon:
    def __init__(self, nombre, tipo, ataque):
        nivel = random.randint(5, 26)
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.ataque = ataque + ' del tipo ' + tipo
        self.hp = nivel * 3

    def __str__(self):
        pokemon = self.nombre +" de nivel "+ str(self.nivel) +" con HP: "+ str(self.hp) +", de tipo "+ self.tipo +" ;Tiene el ataque: "+ self.ataque
        return


class Entrenador:
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo

    def mostrar_equipo(self,equipo):
        self.equipo = equipo
        pass
    def __str__(self):
        entrenador = "El entrenador "+ self.nombre +" tiene en su equipo a:"
        for i in equipo:
            print (i)

        return entrenador
#equipo es una lista de pokemones con sus atributos

lista_pokemon = []
archivo_datos = open('pokemon.csv', 'r')

for linea in archivo_datos:
    print(type(linea))
    linea = linea.strip()
    linea = linea.split(',')

    lista_pokemon.append(linea)

    print(linea)

print(lista_pokemon)

archivo_datos.close()

print("Qué pokemon deseas escojer")
contador = 1
for i in lista_pokemon:
    contador = str(contador)
    print(contador + ")" + i[0])
    contador = int(contador)
    contador += 1

lista_equipo = []
cont = 6
while cont > 0:
    eleccion = int(input("Ingrese número del Pokémon a elegir:"))
    lista_equipo.append(lista_pokemon[eleccion-1])
    cont = cont - 1

pokemon1 = pokemon(lista_equipo[0][0],lista_equipo[0][1],lista_equipo[0][2])
pokemon2 = pokemon(lista_equipo[1][0],lista_equipo[1][1],lista_equipo[1][2])
pokemon3 = pokemon(lista_equipo[2][0],lista_equipo[2][1],lista_equipo[2][2])
pokemon4 = pokemon(lista_equipo[3][0],lista_equipo[3][1],lista_equipo[3][2])
pokemon5 = pokemon(lista_equipo[4][0],lista_equipo[4][1],lista_equipo[4][2])
pokemon6 = pokemon(lista_equipo[5][0],lista_equipo[5][1],lista_equipo[5][2])
equipo = [pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6]
      