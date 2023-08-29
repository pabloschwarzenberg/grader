def sopaletras(nombre_archivo, palabras):
    tablero = cargar_tablero(nombre_archivo)
    resultados = []

    for palabra in palabras:
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                if palabra_en_horizontal(tablero, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "derecha"))
                if palabra_en_vertical(tablero, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "abajo"))
                if palabra_en_diagonal(tablero, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados


def cargar_tablero(nombre_archivo):
    tablero = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            tablero.append(fila)
    return tablero


def palabra_en_horizontal(tablero, palabra, fila, columna):
    if columna + len(palabra) > len(tablero[fila]):
        return False

    for i in range(len(palabra)):
        if tablero[fila][columna + i] != palabra[i]:
            return False

    return True


def palabra_en_vertical(tablero, palabra, fila, columna):
    if fila + len(palabra) > len(tablero):
        return False

    for i in range(len(palabra)):
        if tablero[fila + i][columna] != palabra[i]:
            return False

    return True


def palabra_en_diagonal(tablero, palabra, fila, columna):
    if fila + len(palabra) > len(tablero) or columna + len(palabra) > len(tablero[fila]):
        return False

    for i in range(len(palabra)):
        if tablero[fila + i][columna + i] != palabra[i]:
            return False

    return True


if __name__ == "__main__":
    archivo = input("Ingrese el nombre del archivo: ")
    palabras = input("Ingrese las palabras a buscar (separadas por comas): ").split(",")

    resultados = sopaletras(archivo, palabras)
    print(resultados)


           