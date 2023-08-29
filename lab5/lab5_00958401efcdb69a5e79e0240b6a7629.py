tablero=[["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]]

def mostrar_tablero(tablero):
    j=""
    j=" ".join(tablero[0])+"\n"
    j=" ".join(tablero[1])+"\n"
    j=" ".join(tablero[2])+"\n"
    print (j) 

def revisar_horizontal(tablero,fila):
    if tablero[fila][0]=='X' and tablero[fila][1]=='X' and tablero[fila][2]=='X':
        print('win cat')
        return-1
    elif  tablero[fila][0]=='O' and tablero[fila][1]=='O' and tablero[fila][2]=='O':
        print('win mouse')
        return 1
    else:
        return 0

def revisar_vertical(tablero,columna):
     if tablero[0][columna]=='X' and tablero[1][columna]=='X' and tablero[2][columna]=='X':
        print('win cat')
        return-1
     elif tablero[0][columna]=='O' and tablero[1][columna]=='O' and tablero[2][columna]=='O':
        print('win mouse')
        return 1
     else:
        return 0
def revisar_diagonal_derecha(tablero):
    if tablero[0][0]=='X' and tablero[1][1]=='X' and tablero[2][2]=='X':
        print('win cat')
        return-1
    elif  tablero[0][0]=='O' and tablero[1][1]=='O' and tablero[2][2]=='O':
        print('win mouse')
        return 1
    else:
        return 0

def revisar_diagonal_izquierda(tablero):
    if tablero[0][2]=='X' and tablero[1][1]=='X' and tablero[2][0]=='X':
        print('win cat')
        return-1
    elif  tablero[0][2]=='O' and tablero[1][1]=='O' and tablero[2][0]=='O':
        print('win mouse')
        return 1
    else:
        return 0
