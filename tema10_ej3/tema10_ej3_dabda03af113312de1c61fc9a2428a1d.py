def cargar_tablero(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        tablero = [list(linea.strip()) for linea in archivo]
    return tablero


def buscar_horizontal(palabra, tablero):
    n = len(tablero)
    m = len(tablero[0])

    for fila in range(n):
        for col in range(m - len(palabra) + 1):
            if tablero[fila][col : col + len(palabra)] == palabra:
                return fila, col, "derecha"

    return None


def buscar_vertical(palabra, tablero):
    n = len(tablero)
    m = len(tablero[0])

    for col in range(m):
        for fila in range(n - len(palabra) + 1):
            if all(tablero[fila + i][col] == palabra[i] for i in range(len(palabra))):
                return fila, col, "abajo"

    return None


def buscar_diagonal(palabra, tablero):
    n = len(tablero)
    m = len(tablero[0])

    for fila in range(n - len(palabra) + 1):
        for col in range(m - len(palabra) + 1):
            if all(tablero[fila + i][col + i] == palabra[i] for i in range(len(palabra))):
                return fila, col, "diagonal"

    return None


def sopaletras(nombre_archivo, palabras):
    tablero = cargar_tablero(nombre_archivo)
    resultados = []

    for palabra in palabras:
        resultado = buscar_horizontal(palabra, tablero)
        if resultado is None:
            resultado = buscar_vertical(palabra, tablero)
        if resultado is None:
            resultado = buscar_diagonal(palabra, tablero)

        if resultado is not None:
            resultados.append((palabra, [resultado[0], resultado[1]], resultado[2]))

    return resultados


if __name__ == "__main__":
    archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(archivo, palabras)
    print(resultados)
