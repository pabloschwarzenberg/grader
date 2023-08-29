T=[["_","_","_"],
   ["_","_","_"],
   ["_","_","_"]]
def revisar_horizontal(T,fila):
    if T[fila][0]=='X' and T[fila][1]=='X' and T[fila][2]=='X':
        print('win cat')
        return -1
    elif T[fila][0]=='O' and T[fila][1]=='O' and T[fila][2]=='O':
        print ('win mouse')
        return 1
    else :
        return 0
def revisar_vertical(T,columna):
    if T[0][columna]=='X' and T[1][columna]=='X' and T[2][columna]=='X':
        print('win cat')
        return -1
    elif T[0][columna]=='O' and T[1][columna]=='O' and T[2][columna]=='O':
        print ('win mouse')
        return 1
    else :
        return 0
def revisar_diagonal_derecha(T):
    if T[0][0]=='X' and T[1][1]=='X' and T[2][2]=='X':
        print('win cat')
        return -1
    elif T[0][0]=='O' and T[1][1]=='O' and T[2][2]=='O':
        print('win mouse')
        return 1
    else:
        return 0
def revisar_diagonal_izquierda(T):
    if T[0][2]=='X' and T[1][1]=='X' and T[2][0]=='X':
        print('win cat')
        return -1
    elif T[0][2]=='O' and T[1][1]=='O' and T[2][0]=='O':
        print('win mouse')
        return 1
    else:
        return 0