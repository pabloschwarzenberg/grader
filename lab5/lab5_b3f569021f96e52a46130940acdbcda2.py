def revisar_horizontal(tablero,fila):
    if tablero[fila][0]=="X" and tablero[fila][1]=="X" and tablero[fila][2]=="X":
        H=-1

    elif tablero[fila][0]=="O" and tablero[fila][1]=="O" and tablero[fila][2]=="O":
        H=1
        
    else:
        H=0
    return H

def revisar_vertical(tablero,columna):
    if tablero[0][columna]=="X" and tablero[1][columna]=="X" and tablero[2][columna]=="X":
        V=-1

    elif tablero[0][columna]=="O" and tablero[1][columna]=="O" and tablero[2][columna]=="O":
        V=1
   

    else:
        V=0
    return V

def revisar_diagonal_derecha(tablero):
    if tablero[0][0]=="X" and tablero[1][1]=="X" and tablero[2][2]=="X":
        Diag1=-1
        
    elif tablero[0][0]=="O" and tablero[1][1]=="O" and tablero[2][2]=="O":
        Diag1=1
        
    else:
        Diag1=0

    return Diag1

def revisar_diagonal_izquierda(tablero):
    if tablero[2][0]=="X" and tablero[1][1]=="X" and tablero[0][2]=="X":
        Diag2=-1    

    elif tablero[0][2]=="O" and tablero[1][1]=="O" and tablero[2][0]=="O":
        Diag2=1

    else:
        Diag2=0
    return Diag2



      