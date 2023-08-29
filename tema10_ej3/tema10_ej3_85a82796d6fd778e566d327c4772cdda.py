def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            sopa.append(linea.strip().split())
    return sopa


def buscar_palabra(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    longitud = len(palabra)

    # Buscar palabra horizontalmente (izquierda a derecha)
    for fila in range(n_filas):
        for columna in range(n_columnas - longitud + 1):
            if sopa[fila][columna:columna + longitud] == list(palabra):
                return [fila, columna], "derecha"

    # Buscar palabra verticalmente (arriba a abajo)
    for fila in range(n_filas - longitud + 1):
        for columna in range(n_columnas):
            columna_actual = [sopa[fila + i][columna] for i in range(longitud)]
            if columna_actual == list(palabra):
                return [fila, columna], "abajo"

    # Buscar palabra diagonalmente (esquina superior izquierda a esquina inferior derecha)
    for fila in range(n_filas - longitud + 1):
        for columna in range(n_columnas - longitud + 1):
            diagonal_actual = [sopa[fila + i][columna + i] for i in range(longitud)]
            if diagonal_actual == list(palabra):
                return [fila, columna], "diagonal"

    return None, ""


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        posicion, direccion = buscar_palabra(sopa, palabra)
        resultados.append((palabra, posicion, direccion))

    return resultados


if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de la sopa de letras: ")
    palabras = input("Ingrese las palabras a buscar en la sopa de letras (separadas por espacios): ").split()

    resultados = sopaletras(nombre_archivo, palabras)

    print("Resultados:")
    for resultado in resultados:
        print(resultado)
