A=[["_","_","_"],
   ["_","_","_"],
   ["_","_","_"]]
def revisar_horizontal(A,fila):
    if A[fila][0]=="X" and A[fila][1]=="X" and A[fila][2]=="X":
        print("winGATO")
        return -1
    elif A[fila][0]=="O" and A[fila][1]=="O" and A[fila][2]=="O":
        print("win RATON")
        return 1
    else:
        return 0
def revisar_vertical(A,columna):
    if A[0][columna]=="X" and A[1][columna]=="X" and A[2][columna]=="X":
        print("EL GANADOR ES GATO")
        return -1
    elif A[0][columna]=="O" and A[1][columna]=="O" and A[2][columna]=="O":
        print("EL GANADOR ES RATON")
        return 1
    else:
        return 0
def revisar_diagonal_derecha(A):
    if A[0][0]=="X" and  A[1][1]=="X" and A[2][2]=="X":
        print ("winGATO")
        return -1
    elif A[0][0]=="O" and  A[1][1]=="O" and A[2][2]=="O":
        print("winRATON")
        return 1
    else:
        return 0
def revisar_diagonal_izquierda(A):
    if A[2][0]=="X" and  A[1][1]=="X" and A[0][2]=="X":
        print ("win GATO")
        return -1
    elif A[2][0]=="O" and  A[1][1]=="O" and A[0][2]=="O":
        print("win  RATON")
        return 1
    else:
        return 0
