def sopaletras(nombre_archivo, palabras):
    # Abrir el archivo y leer el contenido
    with open(nombre_archivo, "r") as archivo:
        tablero = [linea.strip().split() for linea in archivo]

    # Obtener las dimensiones del tablero
    filas = len(tablero)
    columnas = len(tablero[0])

    resultados = []

    # Función auxiliar para verificar si una palabra se encuentra en una posición específica
    def buscar_palabra(palabra, fila, columna, direccion):
        longitud = len(palabra)

        # Verificar si la palabra excede los límites del tablero en la dirección dada
        if (
            (direccion == "derecha" and columna + longitud > columnas) or
            (direccion == "abajo" and fila + longitud > filas) or
            (direccion == "diagonal" and (columna + longitud > columnas or fila + longitud > filas))
        ):
            return False

        # Verificar si las letras en el tablero coinciden con la palabra en la dirección dada
        for i in range(longitud):
            if (
                (direccion == "derecha" and tablero[fila][columna + i] != palabra[i]) or
                (direccion == "abajo" and tablero[fila + i][columna] != palabra[i]) or
                (direccion == "diagonal" and tablero[fila + i][columna + i] != palabra[i])
            ):
                return False

        return True

    # Buscar las palabras en el tablero
    for palabra in palabras:
        encontrada = False

        # Recorrer el tablero y buscar la palabra en todas las direcciones posibles
        for i in range(filas):
            for j in range(columnas):
                if buscar_palabra(palabra, i, j, "derecha"):
                    resultados.append((palabra, [i, j], "derecha"))
                    encontrada = True
                elif buscar_palabra(palabra, i, j, "abajo"):
                    resultados.append((palabra, [i, j], "abajo"))
                    encontrada = True
                elif buscar_palabra(palabra, i, j, "diagonal"):
                    resultados.append((palabra, [i, j], "diagonal"))
                    encontrada = True

        # Si la palabra no se encontró, agregar una tupla vacía a los resultados
        if not encontrada:
            resultados.append((palabra, [], ""))

    return resultados


if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))

           