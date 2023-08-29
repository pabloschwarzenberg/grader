def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y obtener la sopa de letras
    with open(nombre_archivo, "r") as archivo:
        sopa = [linea.strip().split() for linea in archivo.readlines()]
    
    # Obtener las dimensiones del tablero
    filas = len(sopa)
    columnas = len(sopa[0])
    
    resultados = []
    
    for palabra in palabras:
        # Buscar la palabra en forma horizontal
        for i in range(filas):
            fila = "".join(sopa[i])
            if palabra in fila:
                columna_inicial = fila.index(palabra)
                resultados.append((palabra, [i, columna_inicial], "derecha"))
        
        # Buscar la palabra en forma vertical
        for j in range(columnas):
            columna = "".join(sopa[i][j] for i in range(filas))
            if palabra in columna:
                fila_inicial = columna.index(palabra)
                resultados.append((palabra, [fila_inicial, j], "abajo"))
        
        # Buscar la palabra en forma diagonal (de izquierda a derecha)
        for i in range(filas):
            for j in range(columnas):
                if i + len(palabra) <= filas and j + len(palabra) <= columnas:
                    diagonal = "".join(sopa[i+k][j+k] for k in range(len(palabra)))
                    if palabra == diagonal:
                        resultados.append((palabra, [i, j], "diagonal"))
        
        # Buscar la palabra en forma diagonal (de derecha a izquierda)
        for i in range(filas):
            for j in range(columnas):
                if i + len(palabra) <= filas and j - len(palabra) + 1 >= 0:
                    diagonal = "".join(sopa[i+k][j-k] for k in range(len(palabra)))
                    if palabra == diagonal:
                        resultados.append((palabra, [i, j], "diagonal"))
    
    return resultados

if __name__ == "__main__":
    archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(archivo, palabras)
    print("Resultados:", resultados)
