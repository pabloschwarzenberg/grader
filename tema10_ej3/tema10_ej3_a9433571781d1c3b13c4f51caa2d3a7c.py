def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, 'r') as archivo:
        sopa = [linea.strip().split() for linea in archivo]

    # Obtener dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    resultados = []

    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        encontrada = False

        # Buscar en forma horizontal (de izquierda a derecha)
        for i in range(filas):
            fila = ''.join(sopa[i])
            if palabra in fila:
                columna_inicial = fila.index(palabra)
                resultados.append((palabra, [i, columna_inicial], "derecha"))
                encontrada = True
                break

        # Buscar en forma vertical (de arriba a abajo)
        if not encontrada:
            for j in range(columnas):
                columna = ''.join([sopa[i][j] for i in range(filas)])
                if palabra in columna:
                    fila_inicial = columna.index(palabra)
                    resultados.append((palabra, [fila_inicial, j], "abajo"))
                    encontrada = True
                    break

        # Buscar en forma diagonal (de esquina superior izquierda a esquina inferior derecha)
        if not encontrada:
            for i in range(filas):
                for j in range(columnas):
                    if i + len(palabra) <= filas and j + len(palabra) <= columnas:
                        diagonal = ''.join([sopa[i+k][j+k] for k in range(len(palabra))])
                        if palabra in diagonal:
                            fila_inicial = i + diagonal.index(palabra)
                            columna_inicial = j + diagonal.index(palabra)
                            resultados.append((palabra, [fila_inicial, columna_inicial], "diagonal"))
                            encontrada = True
                            break
                if encontrada:
                    break

    return resultados