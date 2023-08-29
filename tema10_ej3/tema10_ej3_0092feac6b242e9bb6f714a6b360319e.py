def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    tablero = [linea.strip().split() for linea in archivo]
    archivo.close()

    resultados = []

    for palabra in palabras:
        for fila in range(len(tablero)):
            for columna in range(len(tablero[0])):
                if palabra_horizontal(tablero, fila, columna, palabra):
                    resultados.append((palabra, [fila, columna], "derecha"))
                if palabra_vertical(tablero, fila, columna, palabra):
                    resultados.append((palabra, [fila, columna], "abajo"))
                if palabra_diagonal(tablero, fila, columna, palabra):
                    resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados

def palabra_horizontal(tablero, fila, columna, palabra):
    if columna + len(palabra) > len(tablero[0]):
        return False
    for i in range(len(palabra)):
        if tablero[fila][columna + i] != palabra[i]:
            return False
    return True

def palabra_vertical(tablero, fila, columna, palabra):
    if fila + len(palabra) > len(tablero):
        return False
    for i in range(len(palabra)):
        if tablero[fila + i][columna] != palabra[i]:
            return False
    return True

def palabra_diagonal(tablero, fila, columna, palabra):
    if fila + len(palabra) > len(tablero) or columna + len(palabra) > len(tablero[0]):
        return False
    for i in range(len(palabra)):
        if tablero[fila + i][columna + i] != palabra[i]:
            return False
    return True

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["cra"])
    print(resultados)

    resultados = sopaletras("sopa.txt", ["aro"])
    print(resultados)

    resultados = sopaletras("sopa.txt", ["casa"])
    print(resultados)

    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultados)


           