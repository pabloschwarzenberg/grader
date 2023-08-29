def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, "r") as archivo:
        sopa = [line.strip().split() for line in archivo]

    # Definir las direcciones posibles
    direcciones = [(0, 1), (1, 0), (1, 1)]

    resultados = []
    filas = len(sopa)
    columnas = len(sopa[0])

    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        for i in range(filas):
            for j in range(columnas):
                for direccion in direcciones:
                    dx, dy = direccion
                    palabra_encontrada = True

                    for k in range(len(palabra)):
                        if (i + k * dx >= filas or j + k * dy >= columnas or
                                sopa[i + k * dx][j + k * dy] != palabra[k]):
                            palabra_encontrada = False
                            break

                    if palabra_encontrada:
                        direccion_str = "derecha" if direccion == (0, 1) else "abajo" if direccion == (1, 0) else "diagonal"
                        resultados.append((palabra, [i, j], direccion_str))
                        break  # Salir del bucle de dirección si se encuentra la palabra

    return resultados
