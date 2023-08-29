def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            sopa.append(list(linea.strip()))
    return sopa


def buscar_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    longitud_palabra = len(palabra)
    for i in range(n_filas):
        for j in range(n_columnas - longitud_palabra + 1):
            if sopa[i][j:j + longitud_palabra] == palabra:
                return [i, j], "derecha"
    return None


def buscar_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    longitud_palabra = len(palabra)
    for i in range(n_filas - longitud_palabra + 1):
        for j in range(n_columnas):
            columna = [sopa[i + k][j] for k in range(longitud_palabra)]
            if columna == palabra:
                return [i, j], "abajo"
    return None


def buscar_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    longitud_palabra = len(palabra)
    for i in range(n_filas - longitud_palabra + 1):
        for j in range(n_columnas - longitud_palabra + 1):
            diagonal = [sopa[i + k][j + k] for k in range(longitud_palabra)]
            if diagonal == palabra:
                return [i, j], "diagonal"

            diagonal_inversa = [sopa[i + k][j + longitud_palabra - k - 1] for k in range(longitud_palabra)]
            if diagonal_inversa == palabra:
                return [i, j + longitud_palabra - 1], "diagonal"
    return None


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_horizontal(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))
            continue

        resultado = buscar_vertical(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))
            continue

        resultado = buscar_diagonal(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))

    return resultados


if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    for resultado in resultados:
        print(resultado)
