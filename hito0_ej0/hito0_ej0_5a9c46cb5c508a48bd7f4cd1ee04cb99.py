from random import randint
from time import sleep
class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.nivel = randint(5,25)
        self.tipo = tipo
        self.hp = self.nivel * 3
        self.contador = 2
        self.ataque = ''

    def definir_ataque(self):
        if self.tipo == 'fuego':
            self.ataque = 'Brasas'
        elif self.tipo == 'agua':
            self.ataque = 'Burbujas'
        elif self.tipo == 'hierba':
            self.ataque = 'Hojas Navaja'
        elif self.tipo == 'electrico':
            self.ataque = 'Impactrueno'

    def __str__(self):
        string = str(self.nombre).capitalize() + '\nTipo: ' + str(self.tipo).capitalize() +'\nNivel: ' + str(self.nivel) + '\nVida: ' + str(self.hp) + '\n'
        return string
    
class Batalla:
    def __init__(self, contrincante1, contrincante2):
        self.contrincantes = [contrincante1,contrincante2]
        self.pokemon = [[],[]]
        self.pelea = []
        self.ataque1 = []
        self.ataque2 = []

    def agregar_pelea(self):
        for i in range(2):
            self.pelea.append(self.pokemon[i][0])

    def agregar_pokemon_batalla(self):
        for i in range(6):
            self.pokemon[0].append(self.contrincantes[0].pokemones[i])
        for i in range(6):
            self.pokemon[1].append(self.contrincantes[1].pokemones[i])

    def atacar(self, contrincante):
        if contrincante == 0:
            p1 = self.pelea[0]
            p2 = self.pelea[1]
            ataque = randint(0,int(((p1.nivel/25)*26)))
            print(p1.nombre.capitalize()+' ataca a '+p2.nombre.capitalize()+' con '+p1.ataque+'!\n')
            sleep(2)
            if p1.tipo == 'agua':
                if p2.tipo == 'fuego':
                    p2.hp = p2.hp - 2*ataque
                    print('Es super efectivo!\n')
                    sleep(2)
                elif p2.tipo == 'hierba':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'agua':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'electrico':
                    p2.hp = p2.hp - ataque
            elif p1.tipo == 'fuego':
                if p2.tipo == 'fuego':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'hierba':
                    p2.hp = p2.hp - 2*ataque
                    print('Es super efectivo!\n')
                    sleep(2)
                elif p2.tipo == 'agua':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'electrico':
                    p2.hp = p2.hp - ataque
            elif p1.tipo == 'electrico':
                if p2.tipo == 'fuego':
                    p2.hp = p2.hp - ataque
                elif p2.tipo == 'hierba':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'agua':
                    p2.hp = p2.hp - 2*ataque
                    print('Es super efectivo!\n')
                    sleep(2)
                elif p2.tipo == 'electrico':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
            elif p1.tipo == 'hierba':
                if p2.tipo == 'fuego':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'hierba':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'agua':
                    p2.hp = p2.hp - 2*ataque
                    print('Es super efectivo!\n')
                    sleep(2)
                elif p2.tipo == 'electrico':
                    p2.hp = p2.hp - ataque
        if contrincante == 1:
            p1 = self.pelea[1]
            p2 = self.pelea[0]
            ataque = randint(0,int(((p1.nivel/25)*26)))
            print(p1.nombre.capitalize()+' ataca a '+p2.nombre.capitalize()+' con '+p1.ataque+'!\n')
            sleep(2)
            if p1.tipo == 'agua':
                if p2.tipo == 'fuego':
                    p2.hp = p2.hp - 2*ataque
                    print('Es super efectivo!\n')
                    sleep(2)
                elif p2.tipo == 'hierba':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'agua':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'electrico':
                    p2.hp = p2.hp - ataque
            elif p1.tipo == 'fuego':
                if p2.tipo == 'fuego':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'hierba':
                    p2.hp = p2.hp - 2*ataque
                    print('Es super efectivo!\n')
                    sleep(2)
                elif p2.tipo == 'agua':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'electrico':
                    p2.hp = p2.hp - ataque
            elif p1.tipo == 'electrico':
                if p2.tipo == 'fuego':
                    p2.hp = p2.hp - ataque
                elif p2.tipo == 'hierba':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'agua':
                    p2.hp = p2.hp - 2*ataque
                    print('Es super efectivo!\n')
                    sleep(2)
                elif p2.tipo == 'electrico':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
            elif p1.tipo == 'hierba':
                if p2.tipo == 'fuego':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'hierba':
                    p2.hp = p2.hp - ataque/2
                    print('No es muy efectivo...\n')
                    sleep(2)
                elif p2.tipo == 'agua':
                    p2.hp = p2.hp - 2*ataque
                    print('Es super efectivo!\n')
                    sleep(2)
                elif p2.tipo == 'electrico':
                    p2.hp = p2.hp - ataque
    
    def cambiar_pokemon(self, contrincante, num_pokemon):
        if self.pokemon[contrincante][num_pokemon - 1].hp <= 0:
            print('Este pokemon no esta apto para combatir\n')
            sleep(2)
            cambio = False
        else:
            self.pelea[contrincante] = self.pokemon[contrincante][num_pokemon - 1]
            cambio = True
        return cambio

    def recuperar_pokemon(self, contrincante, num_pokemon):
        if self.pokemon[contrincante][num_pokemon - 1].contador <= 0:
            print('No puedes recuperar mas a este pokemon\n')
            sleep(2)
            recuperar = False
        elif self.pokemon[contrincante][num_pokemon - 1].hp <= 0:
            print('No puedes recuperar a un pokemon caido\n')
            sleep(2)
            recuperar = False
        elif self.pokemon[contrincante][num_pokemon - 1].hp + 20 > self.pokemon[contrincante][num_pokemon - 1].nivel * 3:
            self.pokemon[contrincante][num_pokemon - 1].hp = self.pokemon[contrincante][num_pokemon -1].nivel * 3
            self.pokemon[contrincante][num_pokemon - 1].contador -= 1
            recuperar = True
        else:
            self.pokemon[contrincante][num_pokemon - 1].hp += 20
            self.pokemon[contrincante][num_pokemon - 1].contador -= 1
            recuperar = True
        return recuperar

    def revisar_ganador(self, contrincante):
        game = True
        if contrincante == 0:
            otro = 1
        else:
            otro = 0
        derrotados = []
        for i in self.pokemon[contrincante]:
            if i.hp <= 0:
                derrotados += [0]
        if len(derrotados) > 5:
            game = False
            print('Los pokemones de '+self.contrincantes[contrincante].nombre+' han sido derrotados.\nEl entrenador ganador es '+self.contrincantes[otro].nombre+'!')
        return game
        
class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pokemones = []

    def pokemon_entrenador(self, pokemonos):
        pokemonos = pokemonos.lower()
        pokemonos = pokemonos.strip()
        pokemonos = pokemonos.split(',')
        x = 0
        while x <= 5:
            u = 0
            while u < len(lista_pokemones):
                if pokemonos[x] == lista_pokemones[u].nombre:
                    self.pokemones.append(lista_pokemones[u])
                u += 1
            x += 1

##########################
                    
def random_pokemon():
    with open('pokemon.csv', 'r') as pokemones:
        for linea in pokemones:
            linea = linea.strip()
            linea = linea.split(',')
            pokemon = Pokemon(linea[0], linea[1])
            pokemon.definir_ataque()
            lista_pokemones.append(pokemon)

###########################

entrenador1 = Entrenador(input('Entrenador 1, por favor ingrese su nombre:\n>>>'))
entrenador2 = Entrenador(input('Entrenador 2, por favor ingrese su nombre:\n>>>'))
lista_pokemones = []
random_pokemon()
string_pokemon = ''
for pokemon in lista_pokemones:
    string_pokemon += str(pokemon)+'\n'
print('Pueden elegir 6 pokemones de esta lista:\n\n'+string_pokemon)
sleep(1)
entrenador1.pokemon_entrenador(input('Pokemones de '+entrenador1.nombre+' separados por coma(,)\n>>>'))
entrenador2.pokemon_entrenador(input('Pokemones de '+entrenador2.nombre+' separados por coma(,)\n>>>'))
batalla = Batalla(entrenador1,entrenador2)
batalla.agregar_pokemon_batalla()
batalla.agregar_pelea()
print('+-+-+-+-+-+-+-+-+| '+entrenador1.nombre+' v/s '+entrenador2.nombre+' |+-+-+-+-+-+-+-+-+\n')
sleep(2)
game = True
while game:
    print(str(batalla.pelea[0])+'\nv/s\n\n'+str(batalla.pelea[1]))
    sleep(3)
    contrincante = 0    
    while contrincante == 0:
        atacar0 = 0
        cambiar0 = 0
        print(entrenador1.nombre+', puedes atacar, recuperar a tus pokemon, cambiar tu pokemon por otro no caido, o revisar tus pokemon (Atacar, Recuperar, Cambiar, Revisar).')
        decision = input('>>>')
        decision = decision.strip()
        decision = decision.lower()
        if decision == 'atacar':
            atacar0 = 1
            contrincante = 1
        elif decision == 'recuperar':
            batalla.recuperar_pokemon(contrincante, int(input('Que pokemon quieres recuperar? (del 1 al 6):\n>>>')))
            contrincante = 1
        elif decision == 'cambiar':
            batalla.cambiar_pokemon(contrincante, int(input('Por que pokemon quieres cambiar a tu pokemon actual? (del 1 al 6):\n>>>')))
            cambiar0 = 1
            contrincante = 1
        elif decision == 'revisar':
            for i in batalla.pokemon[contrincante]:
                print(i)
                sleep(2)
    while contrincante == 1:
        atacar1 = 0
        cambiar1 = 0
        print(entrenador2.nombre+', puedes atacar, recuperar a tus pokemon, cambiar tu pokemon por otro no caido, o revisar tus pokemon (Atacar, Recuperar, Cambiar, Revisar).')
        decision = input('>>>')
        decision = decision.strip()
        decision = decision.lower()
        if decision == 'atacar':
            atacar1 = 1
            contrincante = 0
        elif decision == 'recuperar':
            batalla.recuperar_pokemon(contrincante, int(input('Que pokemon quieres recuperar? (del 1 al 6):\n>>>')))
            contrincante = 0
        elif decision == 'cambiar':
            batalla.cambiar_pokemon(contrincante, int(input('Por que pokemon quieres cambiar a tu pokemon actual? (del 1 al 6):\n>>>')))
            cambiar1 = 1
            contrincante = 0
        elif decision == 'revisar':
            for i in batalla.pokemon[contrincante]:
                print(i)
                sleep(2)
    if cambiar0 == 1:
        print(batalla.contrincantes[0].nombre+' ha cambiado su pokemon por '+batalla.pelea[0].nombre.capitalize()+'\n')
        sleep(2)
    if cambiar1 == 1:
        print(batalla.contrincantes[1].nombre+' ha cambiado su pokemon por '+batalla.pelea[1].nombre.capitalize()+'\n')
        sleep(2)
    if atacar0 == 1 and atacar1 == 1:
        if batalla.pelea[0].nivel >= batalla.pelea[1].nivel:
            batalla.atacar(0)
            game = batalla.revisar_ganador(1)
            if batalla.pelea[1].hp > 0:
                batalla.atacar(1)
                game = batalla.revisar_ganador(0)
        if batalla.pelea[0].nivel < batalla.pelea[1].nivel:
            batalla.atacar(1)
            game = batalla.revisar_ganador(0)
            if batalla.pelea[0].hp > 0:
                batalla.atacar(0)
                game = batalla.revisar_ganador(1)
        if batalla.pelea[0].hp <= 0:
            cambio = True
            while cambio:
                cambio = not batalla.cambiar_pokemon(0, int(input('Oh no! el '+batalla.pelea[0].nombre.capitalize()+' de '+batalla.contrincantes[0].nombre+' ha sido derrotado.\nElige otro pokemon (del 1 al 6):\n>>>')))
                print('\n')
                sleep(2)
        if batalla.pelea[1].hp <= 0:
            cambio = True
            while cambio:
                cambio = batalla.cambiar_pokemon(1, int(input('Oh no! el '+batalla.pelea[1].nombre.capitalize()+' de '+batalla.contrincantes[1].nombre+' ha sido derrotado.\nElige otro pokemon (del 1 al 6):\n>>>')))
                print('\n')
                sleep(2)
    elif atacar0 == 1 and atacar1 == 0:
        batalla.atacar(0)
        game = batalla.revisar_ganador(1)
        if batalla.pelea[1].hp <= 0:
            cambio = True
            while cambio:  
                cambio = not batalla.cambiar_pokemon(1, int(input('Oh no! el '+batalla.pelea[1].nombre.capitalize()+' de '+batalla.contrincantes[1].nombre+' ha sido derrotado.\nElige otro pokemon (del 1 al 6):\n>>>')))
                print('\n')
                sleep(2)
    elif atacar0 == 0 and atacar1 == 1:
        batalla.atacar(1)
        game = batalla.revisar_ganador(0)
        if batalla.pelea[0].hp <= 0:
            cambio = True
            while cambio:
                cambio = not batalla.cambiar_pokemon(0, int(input('Oh no! el '+batalla.pelea[0].nombre.capitalize()+' de '+batalla.contrincantes[0].nombre+' ha sido derrotado.\nElige otro pokemon (del 1 al 6):\n>>>')))
                print('\n')
                sleep(2)
    
