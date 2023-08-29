import time
 
tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
 
def dibujar_tablero(tablero):
    print(" %c | %c | %c " % (tablero[0],tablero[1],tablero[2]))
    print("---+---+---")
    print(" %c | %c | %c " % (tablero[3],tablero[4],tablero[5]))
    print("---+---+---")
    print(" %c | %c | %c " % (tablero[6],tablero[7],tablero[8]))
 
 
 
 
def estado_del_juego(tablero):
    ## Revisar las lineas horizontales
    if (tablero[0] == tablero[1] == tablero[2] != ' '):
        estado_actual = "ganador"
    elif (tablero[3] == tablero[4] == tablero[5] != ' '):
        estado_actual = "ganador"
    elif (tablero[6] == tablero[7] == tablero[8] != ' '):
        estado_actual = "ganador"
 
    ## Revisar las lineas verticales
    elif (tablero[0] == tablero[3] == tablero[6] != ' '):
        estado_actual = "ganador"
    elif (tablero[1] == tablero[4] == tablero[7] != ' '):
        estado_actual = "ganador"
    elif (tablero[2] == tablero[5] == tablero[6] != ' '):
        estado_actual = "ganador"
 
    ## Revisar las lineas diagonales
    elif (tablero[0] == tablero[4] == tablero[8] != ' '):
        estado_actual = "ganador"
    elif (tablero[6] == tablero[4] == tablero[2] != ' '):
        estado_actual = "ganador"
    else:
        estado_actual = "jugando"
 
    return estado_actual
 
## Constantes iniciales
 
jugador_actual = "X"
estado_actual = "jugando"
turno = 1
 
print("Vamos a jugar gato")
print("El tablero tiene la siguiente estructura")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")
print("El el jugador X comienza:")
 
while(True):
 
    print("Es el turno del jugador %s" % jugador_actual)
    poscion = int(input("Eliga donde que posicion quiere ocupar(1-9): ")) - 1
 
    if poscion>=0 or poscion<=9:
 
        if tablero[poscion] != " ":
            print("La poscion %s ya esta ocupada por favor elija otra" % str(poscion))
            continue
        else:
            tablero[poscion] = jugador_actual
            turno = turno + 1
    else:
        print("Posicion no valida")
        continue
 
    dibujar_tablero(tablero)
 
    estado_actual = estado_del_juego(tablero)
 
    if estado_actual == "jugando":
 
        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"
    else:
        print("El juego ha sido ganado por el jugador %s" % jugador_actual)
        break
 
    if turno >= 9:
        print("Ya no existen casillas disponibles esto es un Empate")
        break