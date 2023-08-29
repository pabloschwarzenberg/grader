def buscar_horizontal(palabra, tablero):
    n_filas = len(tablero)
    n_columnas = len(tablero[0])
    for fila in range(n_filas):
        for columna in range(n_columnas - len(palabra) + 1):
            if tablero[fila][columna:columna+len(palabra)] == palabra:
                return fila, columna, "derecha"
    return None

def buscar_vertical(palabra, tablero):
    n_filas = len(tablero)
    n_columnas = len(tablero[0])
    for columna in range(n_columnas):
        for fila in range(n_filas - len(palabra) + 1):
            letras = [tablero[fila+i][columna] for i in range(len(palabra))]
            if letras == list(palabra):
                return fila, columna, "abajo"
    return None

def buscar_diagonal(palabra, tablero):
    n_filas = len(tablero)
    n_columnas = len(tablero[0])
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas - len(palabra) + 1):
            letras = [tablero[fila+i][columna+i] for i in range(len(palabra))]
            if letras == list(palabra):
                return fila, columna, "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y construir el tablero
    with open(nombre_archivo, 'r') as archivo:
        tablero = [list(linea.strip()) for linea in archivo.readlines()]

    resultados = []
    for palabra in palabras:
        resultado = buscar_horizontal(palabra, tablero)
        if resultado:
            resultados.append((palabra, [resultado[0], resultado[1]], resultado[2]))
            continue

        resultado = buscar_vertical(palabra, tablero)
        if resultado:
            resultados.append((palabra, [resultado[0], resultado[1]], resultado[2]))
            continue

        resultado = buscar_diagonal(palabra, tablero)
        if resultado:
            resultados.append((palabra, [resultado[0], resultado[1]], resultado[2]))

    return resultados


if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)


