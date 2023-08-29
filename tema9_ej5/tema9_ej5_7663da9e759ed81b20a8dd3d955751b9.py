#(forgive my bad english)
#This code will work properly on python, copy this and enjoy.
#Este juego funciona correctamente en la consola de python, copia y disfruta.
import random

def imprimir(matriz):
    for i in range(4):
        print (' '*22),
        for j in range(4):
            print (matriz[i][j]),
        print ('\n')

def ganador(jugador):
    gana = None
    if gato[1][1]==gato[2][2]==gato[3][3]!='.':
        gana = 'Ganador'
    elif gato[1][3]==gato[2][2]==gato[3][1]!='.':
        gana = 'Ganador'
    for i in range(1,4):
        if gato[i][1]==gato[i][2]==gato[i][3]!='.':
            gana = 'Ganador'
        elif gato[1][i]==gato[2][i]==gato[3][i]!='.':
            gana = 'Ganador'
    if gana == 'Ganador':
        print ('<' + '='*48 + '>')
        print ('> Ha ganado {} <'.format(jugador)).center(50,'=')
        print ('<' + '='*48 + '>\n\n')
        return 'WINNER'

def entradaJugador(jugador,z):
    while True:
        x=None
        y=None
        entrada_jugador = str(input('En que posicion desea marcar?\n'+
                                    '(Ingrese la letra seguido del numero)\n'))
        for caracter in entrada_jugador:
            if caracter in 'abc':
                x = 'abc'.index(caracter) + 1
                letra = caracter.upper()
            elif caracter in '123':
                y=int(caracter)
        if gato[y][x]=='.':
            gato[y][x]=z
            print ('%s ha marcado en %s%d'%(jugador.capitalize(), letra, y))
            imprimir(gato)
            break

def jugada(x,y,z,jugador):
    if gato [y][x]=='.':
        gato[y][x]=z
        if x==1:
            letra='A'
        elif x==2:
            letra='B'
        elif x==3:
            letra='C'
        print ('%s ha marcado en %s%d'%(jugador.capitalize(), letra, y))
        imprimir(gato)

while True:
    gato = [[' ','A','B','C'],['1','.','.','.'],['2','.','.','.'],['3','.','.','.']]
    print (('> bienvenido al juego del gato <'.title()).center(50,'=') + '\n')
    opcion = str(input('Ingrese la opcion de juego:'+
                       '\n 1.- Player vs CPU'+
                       '\n 2.- Player vs Player'+
                       '\n 3.- Salir de la partida\n'))
    imprimir(gato)
    if opcion == '1':
        quien_parte = random.randrange(1)
        if quien_parte==1:
            juega = 'el jugador'
        else:
            juega = 'el contrincante'
        print ('Estas jugando contra la maquina, comienza %s'%(juega))
        while True:
            if juega=='el contrincante':
                x = random.randrange(1,4)
                y = random.randrange(1,4)
                jugada(x,y,'O',juega)
                if ganador(juega) == 'WINNER':
                    break
                juega='el jugador'
            elif juega=='el jugador':
                entradaJugador(juega,'X')
                if ganador(juega) == 'WINNER':
                    break
                juega='el contrincante'
    elif opcion == '2':
        juega = 'el jugador 1'
        while True:
            print ('Turno para %s'%(juega))
            if juega=='el jugador 1':
                entradaJugador(juega,'X')
                if ganador(juega) == 'WINNER':
                    break
                juega='el jugador 2'
            elif juega=='el jugador 2':
                entradaJugador(juega,'O')
                if ganador(juega) == 'WINNER':
                    break
                juega='el jugador 1'
    elif opcion == '3':
        print ('Gracias por jugar! nos vemos en otra partida!')
        break
    else:
        print ('ERROR! Inserte una opcion valida')