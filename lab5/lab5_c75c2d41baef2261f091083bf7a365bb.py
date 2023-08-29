def revisar_horizontal(tablero,fila):
    if tablero[fila][0]=="X" and tablero[fila][1]=="X" and tablero[fila][2]=="X":
        h=-1

    elif tablero[fila][0]=="O" and tablero[fila][1]=="O" and tablero[fila][2]=="O":
        h=1
        
    else:
        h=0
    return h

def revisar_vertical(tablero,columna):
    if tablero[0][columna]=="X" and tablero[1][columna]=="X" and tablero[2][columna]=="X":
        v=-1

    elif tablero[0][columna]=="O" and tablero[1][columna]=="O" and tablero[2][columna]=="O":
        v=1
   

    else:
        v=0
    return v

def revisar_diagonal_derecha(tablero):
    if tablero[0][0]=="X" and tablero[1][1]=="X" and tablero[2][2]=="X":
        d1=-1
        
    elif tablero[0][0]=="O" and tablero[1][1]=="O" and tablero[2][2]=="O":
        d1=1
        
    else:
        d1=0

    return d1

def revisar_diagonal_izquierda(tablero):
    if tablero[2][0]=="X" and tablero[1][1]=="X" and tablero[0][2]=="X":
        d2=-1    

    elif tablero[0][2]=="O" and tablero[1][1]=="O" and tablero[2][0]=="O":
        d2=1

    else:
        d2=0
    return d2