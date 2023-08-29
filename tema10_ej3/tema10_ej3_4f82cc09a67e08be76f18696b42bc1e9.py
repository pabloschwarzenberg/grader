def cargar_sopa_de_letras(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            sopa.append(list(linea.strip()))
    return sopa


def buscar_palabra(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])

    # Buscar en horizontal (de izquierda a derecha)
    for fila in range(filas):
        for columna in range(columnas - len(palabra) + 1):
            if sopa[fila][columna:columna + len(palabra)] == palabra:
                return [fila, columna], "derecha"

    # Buscar en vertical (de arriba a abajo)
    for fila in range(filas - len(palabra) + 1):
        for columna in range(columnas):
            columna_palabra = [sopa[i][columna] for i in range(fila, fila + len(palabra))]
            if columna_palabra == list(palabra):
                return [fila, columna], "abajo"

    # Buscar en diagonal (de esquina superior izquierda a esquina inferior derecha)
    for fila in range(filas - len(palabra) + 1):
        for columna in range(columnas - len(palabra) + 1):
            diagonal_palabra = [sopa[fila + i][columna + i] for i in range(len(palabra))]
            if diagonal_palabra == list(palabra):
                return [fila, columna], "diagonal"

    return None


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa_de_letras(nombre_archivo)
    resultados = []
    for palabra in palabras:
        posicion = buscar_palabra(sopa, palabra)
        if posicion:
            resultados.append((palabra, posicion[0], posicion[1]))
    return resultados


if __name__ == "__main__":
    archivo_sopa = "sopa.txt"
    palabras_buscar = ["casa"]
    resultado = sopaletras(archivo_sopa, palabras_buscar)
    print(resultado)
