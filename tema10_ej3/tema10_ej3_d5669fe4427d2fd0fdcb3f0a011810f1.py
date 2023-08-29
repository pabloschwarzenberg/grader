def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, 'r') as archivo:
        sopa = [linea.strip().split() for linea in archivo]

    # Obtener las dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    resultados = []

    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        # Buscar en dirección horizontal (izquierda a derecha)
        for fila in range(filas):
            for columna in range(columnas - len(palabra) + 1):
                if sopa[fila][columna:columna+len(palabra)] == list(palabra):
                    resultados.append((palabra, [fila, columna], "derecha"))

        # Buscar en dirección diagonal (esquina superior izquierda a esquina inferior derecha)
        for fila in range(filas - len(palabra) + 1):
            for columna in range(columnas - len(palabra) + 1):
                letras = [sopa[fila+i][columna+i] for i in range(len(palabra))]
                if letras == list(palabra):
                    resultados.append((palabra, [fila, columna], "diagonal"))

        # Buscar en dirección vertical (arriba a abajo)
        for fila in range(filas - len(palabra) + 1):
            for columna in range(columnas):
                letras = [sopa[fila+i][columna] for i in range(len(palabra))]
                if letras == list(palabra):
                    resultados.append((palabra, [fila, columna], "abajo"))

    return resultados

if __name__ == "__main__":
    resultado = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultado)
