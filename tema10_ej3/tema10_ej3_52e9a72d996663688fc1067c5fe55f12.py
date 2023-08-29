def buscar_horizontal(tablero, palabra, fila, columna):
    largo_palabra = len(palabra)
    largo_tablero = len(tablero[0])
    if columna + largo_palabra > largo_tablero:
        return False
    for i in range(largo_palabra):
        if tablero[fila][columna+i] != palabra[i]:
            return False
    return True


def buscar_vertical(tablero, palabra, fila, columna):
    largo_palabra = len(palabra)
    largo_tablero = len(tablero)
    if fila + largo_palabra > largo_tablero:
        return False
    for i in range(largo_palabra):
        if tablero[fila+i][columna] != palabra[i]:
            return False
    return True


def buscar_diagonal(tablero, palabra, fila, columna):
    largo_palabra = len(palabra)
    largo_tablero = len(tablero)
    if fila + largo_palabra > largo_tablero or columna + largo_palabra > largo_tablero:
        return False
    for i in range(largo_palabra):
        if tablero[fila+i][columna+i] != palabra[i]:
            return False
    return True


def sopaletras(nombre_archivo, palabras):
    tablero = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            tablero.append(fila)

    resultados = []
    filas = len(tablero)
    columnas = len(tablero[0])
    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                if buscar_horizontal(tablero, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "derecha"))
                if buscar_vertical(tablero, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "abajo"))
                if buscar_diagonal(tablero, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados


if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa"])
    print(resultados)
