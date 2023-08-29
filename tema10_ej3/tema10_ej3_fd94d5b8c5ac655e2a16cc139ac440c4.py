def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras y crear el tablero
    with open(nombre_archivo, 'r') as archivo:
        tablero = [linea.strip().split() for linea in archivo]

    # Obtener las dimensiones del tablero
    filas = len(tablero)
    columnas = len(tablero[0])

    resultados = []

    for palabra in palabras:
        palabra = palabra.lower()
        encontrada = False

        # Buscar la palabra en forma horizontal (de izquierda a derecha)
        for fila in range(filas):
            for columna in range(columnas - len(palabra) + 1):
                subcadena = ''.join(tablero[fila][columna:columna+len(palabra)])
                if subcadena.lower() == palabra:
                    resultados.append((palabra, [fila, columna], 'derecha'))
                    encontrada = True
                    break
            if encontrada:
                break

        # Buscar la palabra en forma vertical (de arriba a abajo)
        if not encontrada:
            for columna in range(columnas):
                for fila in range(filas - len(palabra) + 1):
                    subcadena = ''.join(tablero[fila+i][columna] for i in range(len(palabra)))
                    if subcadena.lower() == palabra:
                        resultados.append((palabra, [fila, columna], 'abajo'))
                        encontrada = True
                        break
                if encontrada:
                    break

        # Buscar la palabra en forma diagonal (de esquina superior izquierda a esquina inferior derecha)
        if not encontrada:
            for fila in range(filas - len(palabra) + 1):
                for columna in range(columnas - len(palabra) + 1):
                    subcadena = ''.join(tablero[fila+i][columna+i] for i in range(len(palabra)))
                    if subcadena.lower() == palabra:
                        resultados.append((palabra, [fila, columna], 'diagonal'))
                        encontrada = True
                        break
                if encontrada:
                    break

    return resultados


if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de la sopa de letras: ")
    palabras = input("Ingrese las palabras a buscar en la sopa de letras (separadas por comas): ").split(',')

    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)


           