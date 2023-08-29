def buscar_horizontal(tablero, palabra, fila, columna):
    if len(palabra) > len(tablero[fila]) - columna:
        return False
    for i in range(len(palabra)):
        if tablero[fila][columna+i] != palabra[i]:
            return False
    return True

def buscar_vertical(tablero, palabra, fila, columna):
    if len(palabra) > len(tablero) - fila:
        return False
    for i in range(len(palabra)):
        if tablero[fila+i][columna] != palabra[i]:
            return False
    return True

def buscar_diagonal(tablero, palabra, fila, columna):
    if len(palabra) > len(tablero) - fila or len(palabra) > len(tablero[fila]) - columna:
        return False
    for i in range(len(palabra)):
        if tablero[fila+i][columna+i] != palabra[i]:
            return False
    return True

def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    tablero = [linea.strip().split() for linea in archivo]
    archivo.close()

    resultados = []
    for palabra in palabras:
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                if buscar_horizontal(tablero, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "derecha"))
                if buscar_vertical(tablero, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "abajo"))
                if buscar_diagonal(tablero, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "diagonal"))
    return resultados

if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
