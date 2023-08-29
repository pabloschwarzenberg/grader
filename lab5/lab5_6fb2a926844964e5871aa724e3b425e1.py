raton='O'
gato='X'
underscore_=''
g=[["_","_","_"],["_","_","_"],["_","_","_"]]
def revisar_horizontal(g,fila):
    if g[fila][0]=="X" and g[fila][1]=="X" and g[fila][2]=="X":
        print("Gato win")
        return -1
    elif g[fila][0]=="O" and g[fila][1]=="O" and g[fila][2]=="O":
        print("Ratón win")
        return 1
    else:
        print("NO HAY GANADOR")
        return 0
def revisar_vertical(g,columna):
    if g[0][columna]=="X" and g[1][columna]=="X" and g[2][columna]=="X":
        print("Gato win")
        return -1
    elif g[0][columna]=="O" and g[1][columna]=="O" and g[2][columna]=="O":
        print("Ratón win")
        return 1
    else:
        print("NO HAY GANADOR")
        return 0
def revisar_diagonal_derecha(g):
    if g[0][0]=="X" and g[1][1]=="X" and g[2][2]=="X":
        print("Gato win")
        return -1
    elif g[0][0]=="O" and g[1][1]=="O" and g[2][2]=="O":
        print("Ratón win")
        return 1
    else:
        print("NO HAY GANADOR")
        return 0
def revisar_diagonal_izquierda(g):
    if g[0][2]=="X" and g[1][1]=="X" and g[2][0]=="X":
        print("Gato win")
        return -1
    elif g[0][2]=="O" and g[1][1]=="O" and g[2][0]=="O":
        print("Ratón win")
        return 1
    else:
        print("NO HAY GANADOR")
        return 0