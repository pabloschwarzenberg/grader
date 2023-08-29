def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras y construir el tablero
    with open(nombre_archivo, 'r') as archivo:
        tablero = [linea.strip().split() for linea in archivo]

    # Obtener dimensiones del tablero
    filas = len(tablero)
    columnas = len(tablero[0])

    resultados = []
    
    # Recorrer cada palabra en la lista de palabras
    for palabra in palabras:
        # Buscar la palabra en el tablero
        for fila in range(filas):
            for columna in range(columnas):
                # Verificar en forma horizontal (derecha)
                if columna + len(palabra) <= columnas:
                    if ''.join(tablero[fila][columna:columna+len(palabra)]) == palabra:
                        resultados.append((palabra, [fila, columna], "derecha"))
                
                # Verificar en forma vertical (abajo)
                if fila + len(palabra) <= filas:
                    if ''.join(tablero[f][columna] for f in range(fila, fila+len(palabra))) == palabra:
                        resultados.append((palabra, [fila, columna], "abajo"))

                # Verificar en forma diagonal (derecha y abajo)
                if columna + len(palabra) <= columnas and fila + len(palabra) <= filas:
                    if ''.join(tablero[fila+i][columna+i] for i in range(len(palabra))) == palabra:
                        resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados
