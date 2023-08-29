def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        tablero = [linea.strip().split() for linea in lineas]

    tablero = [[letra.lower() for letra in fila] for fila in tablero]

    filas = len(tablero)
    columnas = len(tablero[0])

    resultados = []

    def buscar_palabra(palabra, fila, columna, direccion):
        longitud = len(palabra)

        if (direccion == "derecha" and columna + longitud <= columnas) or \
           (direccion == "abajo" and fila + longitud <= filas) or \
           (direccion == "diagonal" and fila + longitud <= filas and columna + longitud <= columnas):

            for i in range(longitud):
                letra_tablero = tablero[fila][columna + i] if direccion == "derecha" else \
                                tablero[fila + i][columna] if direccion == "abajo" else \
                                tablero[fila + i][columna + i]
                if letra_tablero != palabra[i].lower():
                    return False

            return True

        return False

    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                if buscar_palabra(palabra, fila, columna, "derecha"):
                    resultados.append((palabra, [fila, columna], "derecha"))
                if buscar_palabra(palabra, fila, columna, "abajo"):
                    resultados.append((palabra, [fila, columna], "abajo"))
                if buscar_palabra(palabra, fila, columna, "diagonal"):
                    resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados

if __name__ == "__main__":
    nombre_archivo = input("Ingresa el nombre del archivo de la sopa de letras: ")
    palabras = ["casa", "cra", "aro"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)
