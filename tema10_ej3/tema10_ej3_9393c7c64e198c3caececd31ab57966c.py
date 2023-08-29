def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    sopa = []
    for linea in archivo:
        fila = linea.strip().split()
        sopa.append(fila)
    archivo.close()

    resultados = []
    for palabra in palabras:
        resultado = buscar_palabra(palabra, sopa)
        resultados.append(resultado)

    return resultados


def buscar_palabra(palabra, sopa):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])

    for i in range(n_filas):
        for j in range(n_columnas):
            if buscar_horizontal(palabra, sopa, i, j):
                return palabra, [i, j], "derecha"
            if buscar_vertical(palabra, sopa, i, j):
                return palabra, [i, j], "abajo"
            if buscar_diagonal(palabra, sopa, i, j):
                return palabra, [i, j], "diagonal"

    return palabra, None, ""


def buscar_horizontal(palabra, sopa, fila, columna):
    n_columnas = len(sopa[0])
    if columna + len(palabra) > n_columnas:
        return False

    for k in range(len(palabra)):
        if sopa[fila][columna + k] != palabra[k]:
            return False

    return True


def buscar_vertical(palabra, sopa, fila, columna):
    n_filas = len(sopa)
    if fila + len(palabra) > n_filas:
        return False

    for k in range(len(palabra)):
        if sopa[fila + k][columna] != palabra[k]:
            return False

    return True


def buscar_diagonal(palabra, sopa, fila, columna):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    if fila + len(palabra) > n_filas or columna + len(palabra) > n_columnas:
        return False

    for k in range(len(palabra)):
        if sopa[fila + k][columna + k] != palabra[k]:
            return False

    return True


if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))
