raton='O'
gato='X'
underscore_=''
z=[["_","_","_"],["_","_","_"],["_","_","_"]]
def revisar_horizontal(z,fila):
    if z[fila][0]=="X" and z[fila][1]=="X" and z[fila][2]=="X":
        print("Gato win")
        return -1
    elif z[fila][0]=="O" and z[fila][1]=="O" and z[fila][2]=="O":
        print("Ratón win")
        return 1
    else:
        print("NO HAY GANADOR")
        return 0
def revisar_vertical(z,columna):
    if z[0][columna]=="X" and z[1][columna]=="X" and z[2][columna]=="X":
        print("Gato win")
        return -1
    elif z[0][columna]=="O" and z[1][columna]=="O" and z[2][columna]=="O":
        print("Ratón win")
        return 1
    else:
        print("NO HAY GANADOR")
        return 0
def revisar_diagonal_derecha(z):
    if z[0][0]=="X" and z[1][1]=="X" and z[2][2]=="X":
        print("Gato win")
        return -1
    elif z[0][0]=="O" and z[1][1]=="O" and z[2][2]=="O":
        print("Ratón win")
        return 1
    else:
        print("NO HAY GANADOR")
        return 0
def revisar_diagonal_izquierda(z):
    if z[0][2]=="X" and z[1][1]=="X" and z[2][0]=="X":
        print("Gato win")
        return -1
    elif z[0][2]=="O" and z[1][1]=="O" and z[2][0]=="O":
        print("Ratón win")
        return 1
    else:
        print("NO HAY GANADOR")
        return 0