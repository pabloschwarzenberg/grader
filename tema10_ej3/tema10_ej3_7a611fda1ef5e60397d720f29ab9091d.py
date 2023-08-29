def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y crear la matriz de la sopa de letras
    with open(nombre_archivo, 'r') as archivo:
        matriz = [list(linea.strip().lower()) for linea in archivo.readlines()]

    # Definir las direcciones de búsqueda
    direcciones = {
        'derecha': (0, 1),
        'abajo': (1, 0),
        'diagonal': (1, 1)
    }

    # Obtener las dimensiones de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])

    # Función auxiliar para verificar si una posición está dentro de los límites de la matriz
    def dentro_limites(fila, columna):
        return 0 <= fila < filas and 0 <= columna < columnas

    # Función auxiliar para buscar una palabra en una dirección específica
    def buscar_palabra(palabra, fila, columna, direccion):
        delta_fila, delta_columna = direcciones[direccion]
        longitud = len(palabra)

        for i in range(longitud):
            nueva_fila = fila + i * delta_fila
            nueva_columna = columna + i * delta_columna

            if not dentro_limites(nueva_fila, nueva_columna) or matriz[nueva_fila][nueva_columna] != palabra[i]:
                return False

        return True

    resultados = []

    # Iterar sobre las palabras y buscarlas en la matriz
    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                for direccion in direcciones:
                    if buscar_palabra(palabra, fila, columna, direccion):
                        resultados.append((palabra, [fila, columna], direccion))

    return resultados

