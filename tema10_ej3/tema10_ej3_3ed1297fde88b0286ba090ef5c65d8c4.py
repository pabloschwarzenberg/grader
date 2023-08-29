def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    sopa = [linea.strip().split() for linea in archivo]
    archivo.close()
    
    resultados = []
    filas = len(sopa)
    columnas = len(sopa[0])
    
    # Buscar en horizontal (izquierda a derecha)
    for palabra in palabras:
        for i in range(filas):
            fila = "".join(sopa[i])
            if palabra in fila:
                columna_inicial = fila.index(palabra)
                resultados.append((palabra, [i, columna_inicial], "derecha"))
    
    # Buscar en vertical (arriba a abajo)
    for palabra in palabras:
        for j in range(columnas):
            columna = "".join(sopa[i][j] for i in range(filas))
            if palabra in columna:
                fila_inicial = columna.index(palabra)
                resultados.append((palabra, [fila_inicial, j], "abajo"))
    
    # Buscar en diagonal (esquina superior izquierda a esquina inferior derecha)
    for palabra in palabras:
        for i in range(filas):
            for j in range(columnas):
                diagonal = ""
                k = 0
                while i + k < filas and j + k < columnas:
                    diagonal += sopa[i + k][j + k]
                    if palabra in diagonal:
                        fila_inicial = i + k - diagonal.index(palabra)
                        columna_inicial = j + k - diagonal.index(palabra)
                        resultados.append((palabra, [fila_inicial, columna_inicial], "diagonal"))
                    k += 1
    
    return resultados

if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))
