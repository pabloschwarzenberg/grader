def revisar_horizontal(tablero,fila):
    return 0

def revisar_vertical(tablero,columna):
    return 0

def revisar_diagonal_derecha(tablero):
    return 0

def revisar_diagonal_izquierda(tablero):
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