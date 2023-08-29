def buscar_palabra(tablero, palabra, fila, columna, direccion):
    longitud = len(palabra)

    # Verificar límites del tablero según la dirección
    if direccion == "derecha":
        if columna + longitud > len(tablero[0]):
            return False
    elif direccion == "abajo":
        if fila + longitud > len(tablero):
            return False
    elif direccion == "diagonal":
        if fila + longitud > len(tablero) or columna + longitud > len(tablero[0]):
            return False

    # Verificar si la palabra coincide con el tablero
    for i in range(longitud):
        if direccion == "derecha":
            if tablero[fila][columna + i] != palabra[i]:
                return False
        elif direccion == "abajo":
            if tablero[fila + i][columna] != palabra[i]:
                return False
        elif direccion == "diagonal":
            if tablero[fila + i][columna + i] != palabra[i]:
                return False

    return True

def sopaletras(nombre_archivo, palabras):
    tablero = []
    resultado = []

    # Leer el archivo y cargar la sopa de letras
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            tablero.append(fila)

    filas = len(tablero)
    columnas = len(tablero[0])

    # Buscar palabras en el tablero
    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                # Buscar palabra en diferentes direcciones
                if buscar_palabra(tablero, palabra, fila, columna, "derecha"):
                    resultado.append((palabra, [fila, columna], "derecha"))
                if buscar_palabra(tablero, palabra, fila, columna, "abajo"):
                    resultado.append((palabra, [fila, columna], "abajo"))
                if buscar_palabra(tablero, palabra, fila, columna, "diagonal"):
                    resultado.append((palabra, [fila, columna], "diagonal"))

    return resultado

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultado = sopaletras(nombre_archivo, palabras)
    print(resultado)
