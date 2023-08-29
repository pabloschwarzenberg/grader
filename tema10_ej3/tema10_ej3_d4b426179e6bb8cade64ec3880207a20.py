def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split(",")
            sopa.append(fila)
    return sopa


def buscar_horizontal(sopa, palabra, fila, columna):
    n = len(sopa[0])
    m = len(palabra)
    if columna + m > n:
        return False
    for j in range(m):
        if sopa[fila][columna + j] != palabra[j]:
            return False
    return True


def buscar_vertical(sopa, palabra, fila, columna):
    n = len(sopa)
    m = len(palabra)
    if fila + m > n:
        return False
    for i in range(m):
        if sopa[fila + i][columna] != palabra[i]:
            return False
    return True


def buscar_diagonal(sopa, palabra, fila, columna):
    n = len(sopa)
    m = len(sopa[0])
    if fila + len(palabra) > n or columna + len(palabra) > m:
        return False
    for k in range(len(palabra)):
        if sopa[fila + k][columna + k] != palabra[k]:
            return False
    return True


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        palabra = palabra.lower()
        for i in range(len(sopa)):
            for j in range(len(sopa[0])):
                if buscar_horizontal(sopa, palabra, i, j):
                    resultados.append((palabra, [i, j], "derecha"))
                elif buscar_vertical(sopa, palabra, i, j):
                    resultados.append((palabra, [i, j], "abajo"))
                elif buscar_diagonal(sopa, palabra, i, j):
                    resultados.append((palabra, [i, j], "diagonal"))

    return resultados