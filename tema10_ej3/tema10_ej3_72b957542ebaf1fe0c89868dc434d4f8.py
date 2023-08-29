def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    sopa = archivo.read().splitlines()
    archivo.close()

    resultados = []

    filas = len(sopa)
    columnas = len(sopa[0])

    # Buscar palabras horizontalmente
    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas - len(palabra) + 1):
                if sopa[fila][columna:columna + len(palabra)] == palabra:
                    resultados.append((palabra, [fila, columna], "derecha"))

    # Buscar palabras verticalmente
    for palabra in palabras:
        for columna in range(columnas):
            for fila in range(filas - len(palabra) + 1):
                vertical = ''.join([sopa[fila + i][columna] for i in range(len(palabra))])
                if vertical == palabra:
                    resultados.append((palabra, [fila, columna], "abajo"))

    # Buscar palabras diagonalmente
    for palabra in palabras:
        for fila in range(filas - len(palabra) + 1):
            for columna in range(columnas - len(palabra) + 1):
                diagonal = ''.join([sopa[fila + i][columna + i] for i in range(len(palabra))])
                if diagonal == palabra:
                    resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados

if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["casa"]))
