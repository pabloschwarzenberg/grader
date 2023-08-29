def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo]
    return sopa

def buscar_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    len_palabra = len(palabra)

    for fila in range(n_filas):
        for columna in range(n_columnas - len_palabra + 1):
            if sopa[fila][columna:columna + len_palabra] == list(palabra):
                return [fila, columna], "derecha"

    return None

def buscar_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    len_palabra = len(palabra)

    for fila in range(n_filas - len_palabra + 1):
        for columna in range(n_columnas):
            if [sopa[fila + i][columna] for i in range(len_palabra)] == list(palabra):
                return [fila, columna], "abajo"

    return None

def buscar_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    len_palabra = len(palabra)

    for fila in range(n_filas - len_palabra + 1):
        for columna in range(n_columnas - len_palabra + 1):
            if [sopa[fila + i][columna + i] for i in range(len_palabra)] == list(palabra):
                return [fila, columna], "diagonal"

    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        resultado = buscar_horizontal(sopa, palabra)
        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))
            continue

        resultado = buscar_vertical(sopa, palabra)
        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))
            continue

        resultado = buscar_diagonal(sopa, palabra)
        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))

    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]

    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)
