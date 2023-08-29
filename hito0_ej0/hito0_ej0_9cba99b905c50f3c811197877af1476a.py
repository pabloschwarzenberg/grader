import random


class Pokemon:
    def __init__(self, nombrepkmn, tipo):
        self.nombre = nombrepkmn
        self.tipo = tipo
        self.nivel = random.randint(5, 26)
        self.hp = self.nivel * 3
        self.ataque_tipo = self.tipo
        self.ataque_nombre = self.nombre
        self.recuperadas = 0
        self.hp_inicial = self.nivel * 3

    def __str__(self):
        return self.nombre.capitalize() + ", Nivel = " + str(self.nivel) + ", HP = " + str(self.hp)


class Entrenador:
    def __init__(self, nombre, lista_pokemon):
        self.nombre = nombre
        self.lista_pokemon = lista_pokemon
        self.equipo = []
        self.equipo_str = ""
        lista = []
        for i in range(len(self.lista_pokemon)):
            lista.append(self.lista_pokemon[i])
        for i in range(6):
            n = random.randint(0, 15 - i)
            pokemon = lista.pop(n)
            self.equipo.append(pokemon)

    def __str__(self):
        for i in self.equipo:
            self.equipo_str = self.equipo_str + " / " + str(i)
        return str(self.nombre) + " Equipo -> " + str(self.equipo_str)

    def mostrar_pokemones(self):
        for i in self.equipo:
            self.equipo_str = self.equipo_str + str(i).capitalize() + " / "
        print(self.equipo_str)


class Batalla:
    def __init__(self, entrenador1, entrenador2):
        self.nombre_entrenador1 = entrenador1.nombre
        self.nombre_entrenador2 = entrenador2.nombre
        self.pokemones_jugador1 = entrenador1.equipo
        self.pokemones_jugador2 = entrenador2.equipo
        self.pokemon_jugador1 = self.pokemones_jugador1[0]
        self.pokemon_jugador2 = self.pokemones_jugador2[0]
        self.quien_parte = 0
        self.valor_de_ataque_1 = 0
        self.valor_de_ataque_2 = 0
    def __cambiar_pokemon__(self, numero_entrenador):
        contador = 0
        if self.pokemon_jugador1.hp == 0:
            print('Este pokemon ya no tiene vida. Por favor elige otro')
        if numero_entrenador == 1:
            print("Tus pokemones son:")
            for i in entrenador1.equipo:
                print('Pokemon {}'.format(contador) + i.nombre.capitalize() + ', Nivel: {}'.format(i.nivel) +
                      ', HP: {}'.format(i.hp))
                contador += 1
            self.cambio_jugador1 = int(input("Seleccione el numero de pokemon que va a usar:"))
            self.pokemon_cambiado = self.pokemon_jugador1.nombre
            self.pokemon_jugador1 = entrenador1.equipo[self.cambio_jugador1]
            while self.pokemon_jugador1.hp == 0:
                print('Este pokemon ya no tiene vida. Por favor elige otro')
                print("Tus pokemones son:")
                for i in entrenador1.equipo:
                    print('Pokemon {}'.format(contador) + i.nombre.capitalize() + ', Nivel: {}'.format(i.nivel) +
                          ', HP: {}'.format(i.hp))
                    contador += 1
                self.cambio_jugador1 = int(input("Seleccione el numero de pokemon que va a usar:"))
                self.pokemon_cambiado = self.pokemon_jugador1.nombre
                self.pokemon_jugador1 = entrenador1.equipo[self.cambio_jugador1]
            print("El pokemon que vas a usar es:", self.pokemon_jugador1)
        else:
            if self.pokemon_jugador2.hp == 0:
                print('Este pokemon ya no tiene vida. Por favor elige otro')
            print("tus pokemones son:")
            for i in entrenador2.equipo:
                print('Pokemon {}'.format(contador) + ', ' + i.nombre.capitalize() + ', Nivel: {}'.format(i.nivel) +
                      ', HP: {}'.format(i.hp))
                contador += 1
            self.cambio_jugador2 = int(input("Seleccione el numero de pokemon que va a usar:"))
            self.pokemon_cambiado = self.pokemon_jugador2.nombre
            self.pokemon_jugador2 = entrenador2.equipo[self.cambio_jugador2]
            while self.pokemon_jugador2.hp == 0:
                print('Este pokemon ya no tiene vida. Por favor elige otro')
                print("tus pokemones son:")
                for i in entrenador2.equipo:
                    print('Pokemon {}'.format(contador) + ', ' + i.nombre.capitalize() + ', Nivel: {}'.format(i.nivel) +
                          ', HP: {}'.format(i.hp))
                    contador += 1
                self.cambio_jugador2 = int(input("Seleccione el numero de pokemon que va a usar:"))
                self.pokemon_cambiado = self.pokemon_jugador2.nombre
                self.pokemon_jugador2 = entrenador2.equipo[self.cambio_jugador2]
            print("El pokemon que vas a usar es:", self.pokemon_jugador2)
    def check(self):
        if self.pokemon_jugador1.hp == 0:
            self.__cambiar_pokemon__(1)
        if self.pokemon_jugador2.hp == 0:
            self.__cambiar_pokemon__(2)


    def __atacar__(self, pokemon1, pokemon2):
        self.check()
        # pokemon1 = self.pokemon_jugador1
        limite1 = int((pokemon1.nivel / 25) * 2.6)
        limite2 = int((pokemon2.nivel / 25) * 2.6)
        ataque_pokemon1 = random.randint(0, limite1)
        ataque_pokemon2 = random.randint(0, limite2)
        multiplicador = {'agua,fuego': 2, 'agua,hierba': 0.5, 'agua,agua': 0.5,
                         'agua,electrico': 1, 'fuego,fuego': 0.5, 'fuego,hierba': 2,
                         'fuego,agua': 0.5, 'fuego,electrico': 1, 'electrico,fuego': 1,
                         'electrico,hierba': 0.5, 'electrico,agua': 2,
                         'electrico,electrico': 0.5, 'hierba,fuego': 0.5, 'hierba,hierba': 0.5,
                         'hierba,agua': 2, 'hierba,electrico': 1}
        if pokemon1.nivel >= pokemon2.nivel:
            print("-" * 70)
            print('Este turno lo comienza {}.'.format(self.nombre_entrenador1))
            self.quien_parte = 1
        else:
            print("-" * 70)
            print('Este turno lo comienza {}.'.format(self.nombre_entrenador2))
            self.quien_parte = 2
        evaluador1 = pokemon1.tipo + ',' + pokemon2.tipo
        evaluador2 = pokemon2.tipo + ',' + pokemon1.tipo
        self.valor_de_ataque_1 = int(multiplicador[evaluador1] * ataque_pokemon1)
        self.valor_de_ataque_2 = int(multiplicador[evaluador2] * ataque_pokemon2)
        self.check()

    def __recuperar__(self, pokemon):
        self.check()
        if pokemon.recuperadas < 2:
            if pokemon.hp + 20 > pokemon.hp_inicial:
                pokemon.hp = pokemon.hp_inicial
            else:
                pokemon.hp = pokemon.hp + 20
            pokemon.recuperadas += 1
        else:
            print("No se puede recuperar")
        self.check()




print('Bienvendios al juego de pokemon!')
print('Vamos a cargar la lista de pokemones disponibles')
for i in range(5):
    print('.')

archivo_datos = open("pokemon.csv")
lis_archivo = []
for linea in archivo_datos:
    if "\n" in linea:
        linea = linea[:-1]
    lis_archivo.append(linea)

for i in range(len(lis_archivo)):
    lis_archivo[i] = lis_archivo[i].split(",")

lista_pokemon = []

for i in range(len(lis_archivo)):
    p = [Pokemon(lis_archivo[i][0], lis_archivo[i][1])]
    lista_pokemon.append(p)

for i in range(len(lista_pokemon)):
    lista_pokemon.append(lista_pokemon[i].pop(0))
lista_pokemon = lista_pokemon[int(((len(lista_pokemon) / 2))):]
print('=' * 150)
for i in lista_pokemon:
    if lista_pokemon.index(i) == len(lista_pokemon) - 1:
        print(i.nombre.capitalize(), end='.\n')
    else:
        print(i.nombre.capitalize(), end=', ')
print('=' * 150)
agregar = input('Deseas agregar otro pokemón?\n'
                '1. Si\n'
                '2. No\n'
                'Opción: ')
while agregar == '1':
    nombre_agregar = input('Ingrese el nombre del pokemon: ')
    tipo_agregar = input('Ingrese el tipo del pokemon: ')
    lista_pokemon.append(Pokemon(nombre_agregar, tipo_agregar))
    print('=' * 70)
    print('Pokemon ' + nombre_agregar.capitalize() + ', Tipo: ' + tipo_agregar + '.\nPokemon agregado.')
    print('=' * 70)
    agregar = input('Deseas agregar otro pokemón?\n'
                    '1. Si\n'
                    '2. No\n'
                    'Opción:')
print('Perfecto. Continuemos')
entrenador1 = Entrenador(input('Ingrese el nombre del entrenador 1: '), lista_pokemon)
print('Entrenador {} enlistado.'.format(entrenador1.nombre))
print('Tus pokemones son:')
entrenador1.mostrar_pokemones()
entrenador2 = Entrenador(input('Ingrese nombre del entrenador 2: '), lista_pokemon)
entrenador2.mostrar_pokemones()
print("-" * 70)
print('Estamos listos. Comenienza la batalla!')
print("-" * 70)
batalla = Batalla(entrenador1, entrenador2)
nombre_entrenador1 = entrenador1.nombre
nombre_entrenador2 = entrenador2.nombre
nombre_pokemon1 = str(batalla.pokemon_jugador1.nombre)
nombre_pokemon2 = str(batalla.pokemon_jugador2.nombre)
while not (all(i.hp == 0 for i in batalla.pokemones_jugador1) or all(i.hp == 0 for i in batalla.pokemones_jugador2)):
    input('Presione cualquier tecla para continuar....')
    batalla.__atacar__(batalla.pokemon_jugador1, batalla.pokemon_jugador2)
    print('Entrenador {} juega con el pokemon {} y Entrenador {} juega con {}'.format(nombre_entrenador1,
                                                                                       nombre_pokemon1,
                                                                                       nombre_entrenador2,
                                                                                       nombre_pokemon2))
    if batalla.quien_parte == 1:
        actividad1 = input('Entrenador {}, que desea hacer?\n'
                      '1. Atacar\n'
                      '2. Recuperar\n'
                      '3. Cambiar Pokemon\n'.format(nombre_entrenador1))
        if actividad1 == '1':
            actividad2 = input('Entrenador {}, que desea hacer?\n'
                          '1. Atacar\n'
                          '2. Recuperar\n'
                          '3. Cambiar Pokemon\n'.format(nombre_entrenador2))
            if actividad2 == '1':
                print('Entrenador {} ataca con {} pegándole con una cantidad {}'.format(nombre_entrenador1,
                                                                                          batalla.pokemon_jugador1,
                                                                                          batalla.valor_de_ataque_1))
                batalla.pokemon_jugador2.hp += -1 * (batalla.valor_de_ataque_1)
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador2,
                    batalla.pokemon_jugador2,
                    batalla.valor_de_ataque_2))
                batalla.pokemon_jugador1.hp += -1 * (batalla.valor_de_ataque_2)
            elif actividad2 == '2':
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador1,
                    nombre_pokemon1,
                    batalla.valor_de_ataque_1))
                if batalla.pokemon_jugador2.recuperadas < 2:
                    mostrar = True
                else:
                    mostrar = False
                batalla.__recuperar__(batalla.pokemon_jugador2)
                if mostrar:
                    print('Entrenador {} aumenta la vida de {} a {} '.format(nombre_entrenador2,
                                                                             nombre_pokemon2,
                                                                             batalla.pokemon_jugador2.hp))

            elif actividad2 == '3':
                batalla.__cambiar_pokemon__(2)
                print('Entrenador {} cambia su pokemon del {}  a {}'.format(nombre_entrenador2,
                                                                              batalla.pokemon_cambiado,
                                                                              nombre_pokemon2))
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador1,
                    nombre_pokemon1,
                    batalla.valor_de_ataque_1))
                batalla.pokemon_jugador2.hp += -1 * (batalla.valor_de_ataque_1)
        elif actividad1 == '2':
            if batalla.pokemon_jugador1.recuperadas < 2:
                mostrar = True
            else:
                mostrar = False
            batalla.__recuperar__(batalla.pokemon_jugador1)
            if mostrar:
                print('Entrenador {} aumenta la vida de {} a {} '.format(nombre_entrenador1,nombre_pokemon1,
                                                                           batalla.pokemon_jugador1.hp
                                                                           ))
            actividad2 = input('Entrenador {}, que desea hacer?\n'
                          '1. Atacar\n'
                          '2. Recuperar\n'
                          '3. Cambiar Pokemon\n'.format(nombre_entrenador2))

            if actividad2 == '1':
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador2,
                    nombre_pokemon2,
                    batalla.valor_de_ataque_2))
                batalla.pokemon_jugador1.hp += -1 * (batalla.valor_de_ataque_2)

            elif actividad2 == '2':
                if batalla.pokemon_jugador2.recuperadas < 2:
                    mostrar = True
                else:
                    mostrar = False
                batalla.__recuperar__(batalla.pokemon_jugador2)
                if mostrar:
                    print('Entrenador {} aumenta la vida de {} a {} '.format(nombre_entrenador2, nombre_pokemon2,
                                                                               batalla.pokemon_jugador2.hp))
            elif actividad2 == '3':
                batalla.__cambiar_pokemon__(2)
                print('Entrenador {} cambia su pokemon del {}  a {}'.format(nombre_entrenador2,
                                                                              batalla.pokemon_cambiado,
                                                                              nombre_pokemon2))


        elif actividad1 == '3':
            batalla.__cambiar_pokemon__(1)
            print('Entrenador {} cambia su pokemon del {}  a {}'.format(nombre_entrenador1,
                                                                          batalla.pokemon_cambiado,
                                                                          nombre_pokemon1))
            actividad2 = input('Entrenador {}, que desea hacer?\n'
                          '1. Atacar\n'
                          '2. Recuperar\n'
                          '3. Cambiar Pokemon\n'.format(nombre_entrenador2))
            if actividad2 == '1':
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador2,
                    nombre_pokemon2,
                    batalla.valor_de_ataque_2))
                batalla.pokemon_jugador1.hp += -1 * (batalla.valor_de_ataque_2)
            elif actividad2 == '2':
                if batalla.pokemon_jugador2.recuperadas < 2:
                    mostrar = True
                else:
                    mostrar = False

                batalla.__recuperar__(batalla.pokemon_jugador2)
                if mostrar:
                    print('Entrenador {} aumenta la vida de {} a {} '.format(nombre_entrenador2,nombre_pokemon2,
                                                                               batalla.pokemon_jugador2.hp
                                                                               ))
            elif actividad2 == '3':
                batalla.__cambiar_pokemon__(2)
                print('Entrenador {} cambia su pokemon del {}  a {}'.format(nombre_entrenador2,
                                                                              batalla.pokemon_cambiado,
                                                                              nombre_pokemon2))
    if batalla.quien_parte == 2:
        actividad1 = input('Entrenador {}, que desea hacer?\n'
                      '1. Atacar\n'
                      '2. Recuperar\n'
                      '3. Cambiar Pokemon\n'.format(nombre_entrenador2))
        if actividad1 == '1':
            actividad2 = input('Entrenador {}, que desea hacer?\n'
                          '1. Atacar\n'
                          '2. Recuperar\n'
                          '3. Cambiar Pokemon\n'.format(nombre_entrenador2))
            if actividad2 == '1':
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador2,
                    batalla.pokemon_jugador2,
                    batalla.valor_de_ataque_2))
                batalla.pokemon_jugador1.hp += -1 * (batalla.valor_de_ataque_2)
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador1,
                    nombre_pokemon1,
                    batalla.valor_de_ataque_1))
                batalla.pokemon_jugador2.hp += -1 * (batalla.valor_de_ataque_1)
            elif actividad2 == '2':
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador2,
                    nombre_pokemon2,
                    batalla.valor_de_ataque_2))
                if batalla.pokemon_jugador1.recuperadas < 2:
                    mostrar = True
                else:
                    mostrar = False
                batalla.__recuperar__(batalla.pokemon_jugador1)
                if mostrar:
                    print('Entrenador {} aumenta la vida de {} a {} '.format(nombre_entrenador1,nombre_pokemon1,
                                                                               batalla.pokemon_jugador1.hp))
            elif actividad2 == '3':
                batalla.__cambiar_pokemon__(1)
                print('Entrenador {} cambia su pokemon del {}  a {}'.format(nombre_entrenador1,
                                                                              batalla.pokemon_cambiado,
                                                                              nombre_pokemon1))
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador2,
                    batalla.pokemon_jugador2,
                    batalla.valor_de_ataque_2))
                batalla.pokemon_jugador1.hp += -1 * (batalla.valor_de_ataque_2)
        elif actividad1 == '2':
            if batalla.pokemon_jugador2.recuperadas < 2:
                mostrar = True
            else:
                mostrar = False
            batalla.__recuperar__(batalla.pokemon_jugador2)
            if mostrar:
                print('Entrenador {} aumenta la vida de {} a {} '.format(nombre_entrenador1,
                                                                           batalla.pokemon_jugador1.hp,
                                                                           nombre_pokemon1))
            actividad2 = input('Entrenador {}, que desea hacer?\n'
                          '1. Atacar\n'
                          '2. Recuperar\n'
                          '3. Cambiar Pokemon\n'.format(nombre_entrenador2))

            if actividad2 == '1':
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador1,
                    nombre_pokemon1,
                    batalla.valor_de_ataque_1))
                batalla.pokemon_jugador2.hp += -1 * (batalla.valor_de_ataque_1)

            elif actividad2 == '2':
                if batalla.pokemon_jugador1.recuperadas < 2:
                    mostrar = True
                else:
                    mostrar = False
                batalla.__recuperar__(batalla.pokemon_jugador1)
                if mostrar:
                    print('Entrenador {} aumenta la vida de {} a {} '.format(nombre_entrenador1,nombre_pokemon1,
                                                                               batalla.pokemon_jugador1.hp))
            elif actividad2 == '3':
                batalla.__cambiar_pokemon__(1)
                print('Entrenador {} cambia su pokemon del {}  a {}'.format(nombre_entrenador1,
                                                                              batalla.pokemon_cambiado,
                                                                              nombre_pokemon1))
        elif actividad1 == '3':
            batalla.__cambiar_pokemon__(2)
            print('Entrenador {} cambia su pokemon del {}  al {}'.format(nombre_entrenador2,
                                                                          batalla.pokemon_cambiado,
                                                                          batalla.pokemon_jugador2))
            actividad2 = input('Entrenador {}, que desea hacer?\n'
                          '1. Atacar\n'
                          '2. Recuperar\n'
                          '3. Cambiar Pokemon\n'.format(nombre_entrenador1))
            if actividad2 == '1':
                print('Entrenador {} ataca con {} pegándole al otro pokemon con una cantidad {}'.format(
                    nombre_entrenador1,
                    nombre_pokemon1,
                    batalla.valor_de_ataque_1))
                batalla.pokemon_jugador2.hp += -1 * (batalla.valor_de_ataque_1)
            elif actividad2 == '2':
                if batalla.pokemon_jugador1.recuperadas < 2:
                    mostrar = True
                else:
                    mostrar = False
                batalla.__recuperar__(batalla.pokemon_jugador1)
                if mostrar:
                    print('Entrenador {} aumenta la vida de {} a {} '.format(nombre_entrenador1,nombre_pokemon1,
                                                                               batalla.pokemon_jugador1.hp))
            elif actividad2 == '3':
                batalla.__cambiar_pokemon__(1)
                print('Entrenador {} cambia su pokemon del {}  a {}'.format(nombre_entrenador1,
                                                                              batalla.pokemon_cambiado,
                                                                              nombre_pokemon1))
ganador = ''
if all(i.hp == 0 for i in batalla.pokemones_jugador1) and not(all(i.hp == 0 for i in batalla.pokemones_jugador2)):
    ganador = 'el ganador es el entrenador {}'.format(nombre_entrenador1)
elif not(all(i.hp == 0 for i in batalla.pokemones_jugador1)) and all(i.hp == 0 for i in batalla.pokemones_jugador2):
    ganador = 'el ganador es el entrenador {}'.format(nombre_entrenador2)
elif all(i.hp == 0 for i in batalla.pokemones_jugador1) and all(i.hp == 0 for i in batalla.pokemones_jugador2):
    ganador = 'Se ha generado un empate'
else:
    print('ERROR')
print('Juego Terminado!.' + ganador)