def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    sopa = [linea.strip().split() for linea in archivo]
    archivo.close()

    filas = len(sopa)
    columnas = len(sopa[0])

    resultados = []
    
    for palabra in palabras:
        encontrada = False
        for fila in range(filas):
            for columna in range(columnas):
                if buscar_horizontal(sopa, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "derecha"))
                    encontrada = True
                elif buscar_vertical(sopa, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "abajo"))
                    encontrada = True
                elif buscar_diagonal(sopa, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "diagonal"))
                    encontrada = True
                if encontrada:
                    break
            if encontrada:
                break

    return resultados


def buscar_horizontal(sopa, palabra, fila, columna):
    longitud = len(palabra)
    if columna + longitud > len(sopa[fila]):
        return False
    for i in range(longitud):
        if sopa[fila][columna + i] != palabra[i]:
            return False
    return True


def buscar_vertical(sopa, palabra, fila, columna):
    longitud = len(palabra)
    if fila + longitud > len(sopa):
        return False
    for i in range(longitud):
        if sopa[fila + i][columna] != palabra[i]:
            return False
    return True


def buscar_diagonal(sopa, palabra, fila, columna):
    longitud = len(palabra)
    if fila + longitud > len(sopa) or columna + longitud > len(sopa[fila]):
        return False
    for i in range(longitud):
        if sopa[fila + i][columna + i] != palabra[i]:
            return False
    return True


if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    for resultado in resultados:
        print(resultado)