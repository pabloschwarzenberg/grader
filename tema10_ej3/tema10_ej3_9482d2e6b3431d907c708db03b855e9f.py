def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, "r") as archivo:
        tablero = [linea.strip().split() for linea in archivo]
    
    # Obtener las dimensiones del tablero
    filas = len(tablero)
    columnas = len(tablero[0])
    
    resultados = []
    
    # Buscar las palabras en el tablero
    for palabra in palabras:
        for i in range(filas):
            for j in range(columnas):
                # Buscar palabra en forma horizontal (de izquierda a derecha)
                if j + len(palabra) <= columnas:
                    if "".join(tablero[i][j:j+len(palabra)]) == palabra:
                        resultados.append((palabra, [i, j], "derecha"))
                
                # Buscar palabra en forma vertical (de arriba a abajo)
                if i + len(palabra) <= filas:
                    if "".join(tablero[k][j] for k in range(i, i+len(palabra))) == palabra:
                        resultados.append((palabra, [i, j], "abajo"))
                
                # Buscar palabra en forma diagonal (de esquina superior izquierda a esquina inferior derecha)
                if i + len(palabra) <= filas and j + len(palabra) <= columnas:
                    if "".join(tablero[i+k][j+k] for k in range(len(palabra))) == palabra:
                        resultados.append((palabra, [i, j], "diagonal"))
    
    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "cra", "aro"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)
