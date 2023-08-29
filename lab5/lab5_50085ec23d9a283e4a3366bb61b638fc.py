print('Juego del Gato :3')
print('Ratón = O ; Gato = X')
Tablero=[['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]
def revisar_horizontal(Tablero,fila):
    if Tablero[fila][0]=='X' and Tablero[fila][1]=='X' and Tablero[fila][2]=='X':
        return -1
    elif Tablero[fila][0]=='O' and Tablero[fila][1]=='O' and Tablero[fila][2]=='O':
        return 1
    else:
        return 0
 
def revisar_vertical(Tablero,columna):
    if Tablero[0][columna]=='X' and Tablero[1][columna]=='X' and Tablero[2][columna]=='X':
        return -1
    elif Tablero[0][columna]=='O' and Tablero[1][columna]=='O' and Tablero[2][columna]=='O':
        return 1
    else:
        return 0

def revisar_diagonal_derecha(Tablero):
    if Tablero[0][0]=='X' and Tablero[1][1]=='X' and Tablero[2][2]=='X':
        return -1
    elif Tablero[0][0]=='O' and Tablero[1][1]=='O' and Tablero[2][2]=='O':
        return 1
    else:
        return 0

def revisar_diagonal_izquierda(Tablero):
    if Tablero[0][2]=='X' and Tablero[1][1]=='X' and Tablero[2][0]=='X':
        return -1
    elif Tablero[0][2]=='O' and Tablero[1][1]=='O' and Tablero[2][0]=='O':
        return 1
    else:
        return 0