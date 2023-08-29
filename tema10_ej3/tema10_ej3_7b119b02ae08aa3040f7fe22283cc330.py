def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    sopa = []
    for linea in archivo:
        fila = linea.strip().split()
        sopa.append(fila)
    archivo.close()

    resultados = []
    filas = len(sopa)
    columnas = len(sopa[0])

    for palabra in palabras:
        encontrada = False
        for i in range(filas):
            for j in range(columnas):
                if buscar_palabra(sopa, palabra, i, j):
                    direccion = determinar_direccion(i, j, len(palabra), filas, columnas)
                    resultados.append((palabra, [i, j], direccion))
                    encontrada = True
                    break
            if encontrada:
                break

    return resultados


def buscar_palabra(sopa, palabra, inicio_fila, inicio_columna):
    filas = len(sopa)
    columnas = len(sopa[0])
    largo = len(palabra)

    # Buscar horizontalmente
    if inicio_columna + largo <= columnas:
        encontrada = True
        for j in range(largo):
            if sopa[inicio_fila][inicio_columna + j] != palabra[j]:
                encontrada = False
                break
        if encontrada:
            return True

    # Buscar verticalmente
    if inicio_fila + largo <= filas:
        encontrada = True
        for i in range(largo):
            if sopa[inicio_fila + i][inicio_columna] != palabra[i]:
                encontrada = False
                break
        if encontrada:
            return True

    # Buscar diagonalmente
    if inicio_fila + largo <= filas and inicio_columna + largo <= columnas:
        encontrada = True
        for k in range(largo):
            if sopa[inicio_fila + k][inicio_columna + k] != palabra[k]:
                encontrada = False
                break
        if encontrada:
            return True

    return False


def determinar_direccion(fila, columna, largo, filas, columnas):
    if largo <= columnas - columna:
        direccion = "derecha"
    elif largo <= filas - fila:
        direccion = "abajo"
    else:
        direccion = "diagonal"
    return direccion


if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["cra"])
    print(resultados)

    resultados = sopaletras("sopa.txt", ["aro"])
    print(resultados)

    resultados = sopaletras("sopa.txt", ["casa"])
    print(resultados)

    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultados)


           