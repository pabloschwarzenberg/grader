def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.readlines()

    contenido = [linea.strip() for linea in contenido]
    filas = len(contenido)
    columnas = len(contenido[0])

    resultados = []

    # Función auxiliar para verificar si una palabra está en una posición determinada
    def verificar_palabra(palabra, fila, col, direccion):
        longitud = len(palabra)
        if direccion == "derecha":
            if col + longitud > columnas:
                return False
            for i in range(longitud):
                if contenido[fila][col + i] != palabra[i]:
                    return False
        elif direccion == "abajo":
            if fila + longitud > filas:
                return False
            for i in range(longitud):
                if contenido[fila + i][col] != palabra[i]:
                    return False
        elif direccion == "diagonal":
            if col + longitud > columnas or fila + longitud > filas:
                return False
            for i in range(longitud):
                if contenido[fila + i][col + i] != palabra[i]:
                    return False
        return True

    # Búsqueda de palabras en el tablero
    for palabra in palabras:
        encontrada = False
        direccion = ""

        # Buscar en forma horizontal
        for fila in range(filas):
            for col in range(columnas - len(palabra) + 1):
                if verificar_palabra(palabra, fila, col, "derecha"):
                    resultados.append((palabra, [fila, col], "derecha"))
                    encontrada = True
                    break
            if encontrada:
                break

        # Buscar en forma vertical
        if not encontrada:
            for col in range(columnas):
                for fila in range(filas - len(palabra) + 1):
                    if verificar_palabra(palabra, fila, col, "abajo"):
                        resultados.append((palabra, [fila, col], "abajo"))
                        encontrada = True
                        break
                if encontrada:
                    break

        # Buscar en forma diagonal
        if not encontrada:
            for fila in range(filas - len(palabra) + 1):
                for col in range(columnas - len(palabra) + 1):
                    if verificar_palabra(palabra, fila, col, "diagonal"):
                        resultados.append((palabra, [fila, col], "diagonal"))
                        encontrada = True
                        break
                if encontrada:
                    break

    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    for resultado in resultados:
        print(resultado)
