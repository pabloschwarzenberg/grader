def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y obtener la sopa de letras
    with open(nombre_archivo, 'r') as archivo:
        sopa = [linea.strip().split() for linea in archivo]
    
    filas = len(sopa)
    columnas = len(sopa[0])
    
    resultados = []
    
    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        # Buscar horizontalmente
        for fila in range(filas):
            for col in range(columnas - len(palabra) + 1):
                if sopa[fila][col:col+len(palabra)] == list(palabra):
                    resultados.append((palabra, [fila, col], "derecha"))
        
        # Buscar verticalmente
        for fila in range(filas - len(palabra) + 1):
            for col in range(columnas):
                letras = [sopa[fila+i][col] for i in range(len(palabra))]
                if letras == list(palabra):
                    resultados.append((palabra, [fila, col], "abajo"))
        
        # Buscar en diagonal (de izquierda a derecha)
        for fila in range(filas - len(palabra) + 1):
            for col in range(columnas - len(palabra) + 1):
                letras = [sopa[fila+i][col+i] for i in range(len(palabra))]
                if letras == list(palabra):
                    resultados.append((palabra, [fila, col], "diagonal"))
        
        # Buscar en diagonal (de derecha a izquierda)
        for fila in range(filas - len(palabra) + 1):
            for col in range(len(palabra) - 1, columnas):
                letras = [sopa[fila+i][col-i] for i in range(len(palabra))]
                if letras == list(palabra):
                    resultados.append((palabra, [fila, col], "diagonal"))
    
    return resultados


if __name__ == "__main__":
    resultado = sopaletras("sopa.txt", ["casa"])
    print(resultado)
