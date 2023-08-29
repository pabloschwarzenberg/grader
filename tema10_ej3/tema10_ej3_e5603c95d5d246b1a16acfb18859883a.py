def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, 'r') as file:
        sopa = [list(line.strip()) for line in file.readlines()]

    # Tamaño de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    # Direcciones posibles: derecha, abajo, diagonal, izquierda y arriba
    direcciones = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]

    resultados = []

    for palabra in palabras:
        for i in range(filas):
            for j in range(columnas):
                for direccion in direcciones:
                    dx, dy = direccion
                    fin_fila = i + len(palabra) * dx
                    fin_columna = j + len(palabra) * dy

                    # Verificar si la palabra cabe dentro de la sopa de letras
                    if fin_fila < 0 or fin_fila >= filas or fin_columna < 0 or fin_columna >= columnas:
                        continue

                    # Verificar si la palabra está presente en la dirección actual
                    encontrada = True
                    for k in range(len(palabra)):
                        if sopa[i + k * dx][j + k * dy] != palabra[k]:
                            encontrada = False
                            break

                    if encontrada:
                        inicio = [i, j]
                        if direccion == (0, 1):
                            direccion_str = "derecha"
                        elif direccion == (1, 0):
                            direccion_str = "abajo"
                        elif direccion == (1, 1):
                            direccion_str = "diagonal"
                        elif direccion == (0, -1):
                            direccion_str = "izquierda"
                        elif direccion == (-1, 0):
                            direccion_str = "arriba"
                        elif direccion == (-1, -1):
                            direccion_str = "diagonal inversa"
                        elif direccion == (-1, 1):
                            direccion_str = "diagonal inversa"
                        elif direccion == (1, -1):
                            direccion_str = "diagonal inversa"

                        resultados.append((palabra, inicio, direccion_str))

    return resultados


