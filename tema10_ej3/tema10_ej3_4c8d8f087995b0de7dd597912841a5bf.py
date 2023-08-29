def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo]
    return sopa


def buscar_horizontal(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    tam_palabra = len(palabra)

    for i in range(n):
        for j in range(m - tam_palabra + 1):
            if sopa[i][j:j+tam_palabra] == palabra:
                return [i, j], "derecha"
    return None


def buscar_vertical(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    tam_palabra = len(palabra)

    for i in range(n - tam_palabra + 1):
        for j in range(m):
            if all(sopa[i+k][j] == palabra[k] for k in range(tam_palabra)):
                return [i, j], "abajo"
    return None


def buscar_diagonal(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    tam_palabra = len(palabra)

    for i in range(n - tam_palabra + 1):
        for j in range(m - tam_palabra + 1):
            if all(sopa[i+k][j+k] == palabra[k] for k in range(tam_palabra)):
                return [i, j], "diagonal"
    return None


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        resultado = buscar_horizontal(sopa, palabra)
        if resultado is None:
            resultado = buscar_vertical(sopa, palabra)
        if resultado is None:
            resultado = buscar_diagonal(sopa, palabra)
        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))

    return resultados


if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultados)
