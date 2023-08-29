def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        sopa = [list(linea.strip()) for linea in archivo]
    return sopa


def buscar_horizontal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for i in range(filas):
        for j in range(columnas - len(palabra) + 1):
            if sopa[i][j:j + len(palabra)] == palabra:
                return [i, j], "derecha"
    return None


def buscar_vertical(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for i in range(filas - len(palabra) + 1):
        for j in range(columnas):
            if all(sopa[i + k][j] == palabra[k] for k in range(len(palabra))):
                return [i, j], "abajo"
    return None


def buscar_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for i in range(filas - len(palabra) + 1):
        for j in range(columnas - len(palabra) + 1):
            if all(sopa[i + k][j + k] == palabra[k] for k in range(len(palabra))):
                return [i, j], "diagonal"
    return None


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        posicion = buscar_horizontal(sopa, palabra)
        if posicion is None:
            posicion = buscar_vertical(sopa, palabra)
        if posicion is None:
            posicion = buscar_diagonal(sopa, palabra)
        if posicion is not None:
            resultados.append((palabra, posicion[0], posicion[1]))
    return resultados