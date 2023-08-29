"""def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    archivo.close()
    
    resultados = []
    
    for palabra in palabras:
        letras = list(palabra)
        resultados.append((palabra, [0, 0], "diagonal"))
    
    return resultados"""
def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, "r") as archivo:
        tablero = [list(linea.strip()) for linea in archivo]

    filas = len(tablero)
    columnas = len(tablero[0])

    resultados = []

    for palabra in palabras:
        letras = list(palabra)

        # Buscar en horizontal (izquierda a derecha)
        for fila in range(filas):
            for columna in range(columnas - len(letras) + 1):
                secuencia_letras = tablero[fila][columna:columna + len(letras)]
                if secuencia_letras == letras:
                    resultados.append((palabra, [fila, columna], "derecha"))
                    break
        
        # Buscar en vertical (arriba a abajo)
        if resultados:
            continue  # Si ya se encontró la palabra, pasar a la siguiente

        for columna in range(columnas):
            for fila in range(filas - len(letras) + 1):
                secuencia_letras = [tablero[fila + i][columna] for i in range(len(letras))]
                if secuencia_letras == letras:
                    resultados.append((palabra, [fila, columna], "abajo"))
                    break
        
        # Buscar en diagonal (esquina superior izquierda a esquina inferior derecha)
        if resultados:
            continue  # Si ya se encontró la palabra, pasar a la siguiente

        for fila in range(filas - len(letras) + 1):
            for columna in range(columnas - len(letras) + 1):
                secuencia_letras = [tablero[fila + i][columna + i] for i in range(len(letras))]
                if secuencia_letras == letras:
                    resultados.append((palabra, [fila, columna], "diagonal"))
                    break

    return resultados


if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))
