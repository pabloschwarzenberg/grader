def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, "r") as archivo:
        sopa = [linea.strip().split() for linea in archivo]

    filas = len(sopa)
    columnas = len(sopa[0])

    resultados = []

    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        palabra = palabra.lower()
        for fila in range(filas):
            for columna in range(columnas):
                # Buscar palabra en dirección horizontal (derecha)
                if columna + len(palabra) <= columnas:
                    palabra_encontrada = "".join(sopa[fila][columna:columna + len(palabra)])
                    if palabra_encontrada.lower() == palabra:
                        resultados.append((palabra, [fila, columna], "derecha"))

                # Buscar palabra en dirección vertical (abajo)
                if fila + len(palabra) <= filas:
                    palabra_encontrada = "".join(sopa[i][columna] for i in range(fila, fila + len(palabra)))
                    if palabra_encontrada.lower() == palabra:
                        resultados.append((palabra, [fila, columna], "abajo"))

                # Buscar palabra en dirección diagonal (derecha-abajo)
                if fila + len(palabra) <= filas and columna + len(palabra) <= columnas:
                    palabra_encontrada = "".join(sopa[fila + i][columna + i] for i in range(len(palabra)))
                    if palabra_encontrada.lower() == palabra:
                        resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados


if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))
