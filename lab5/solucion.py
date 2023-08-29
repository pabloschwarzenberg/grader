def revisar_horizontal(tablero,fila):
    suma_gato=0
    suma_raton=0
    for i in range(len(tablero[fila])):
        if tablero[fila][i]=="X":
            suma_gato+=1
        elif tablero[fila][i]=="O":
            suma_raton+=1
    if suma_gato==3:
        return -1
    elif suma_raton==3:
        return 1
    else:
        return 0

def revisar_vertical(tablero,columna):
    suma_gato=0
    suma_raton=0
    for i in range(len(tablero)):
        if tablero[i][columna]=="X":
            suma_gato+=1
        elif tablero[i][columna]=="O":
            suma_raton+=1
    if suma_gato==3:
        return -1
    elif suma_raton==3:
        return 1
    else:
        return 0

def revisar_diagonal_derecha(tablero):
    suma_gato=0
    suma_raton=0
    for i in range(len(tablero)):
        if tablero[i][i]=="X":
            suma_gato+=1
        elif tablero[i][i]=="O":
            suma_raton+=1
    if suma_gato==3:
        return -1
    elif suma_raton==3:
        return 1
    else:
        return 0

def revisar_diagonal_izquierda(tablero):
    suma_gato=0
    suma_raton=0
    for i in range(len(tablero)):
        if tablero[i][2-i]=="X":
            suma_gato+=1
        elif tablero[i][2-i]=="O":
            suma_raton+=1
    if suma_gato==3:
        return -1
    elif suma_raton==3:
        return 1
    else:
        return 0

def jugar(tablero,fila,columna,marca):
    if fila>=0 and fila<len(tablero[0]) and columna>=0 and columna<len(tablero):
        tablero[fila][columna]=marca

def convertir_a_string(tablero):
    s=""
    for fila in tablero:
        s=s+" ".join(fila)+"\n"
    return s

if __name__ == "__main__":
    tablero=[["_","_","_"],["_","_","_"],["_","_","_"]]
    jugar(tablero,0,0,"X")
    jugar(tablero,0,1,"X")
    jugar(tablero,0,2,"X")
    print(convertir_a_string(tablero))
    print(revisar_diagonal_derecha(tablero))
    print(revisar_diagonal_izquierda(tablero))
    print(revisar_horizontal(tablero,0))
    print(revisar_vertical(tablero,0))