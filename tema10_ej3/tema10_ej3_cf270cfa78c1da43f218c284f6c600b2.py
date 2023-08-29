def sopaletras(nombre_archivo, palabras):
    # Abrir el archivo y leer la sopa de letras
    with open(nombre_archivo, 'r') as archivo:
        sopa = [linea.strip().split() for linea in archivo]

    # Obtener las dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    resultados = []
    
    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        for i in range(filas):
            for j in range(columnas):
                # Buscar en dirección horizontal (derecha)
                if j + len(palabra) <= columnas:
                    if sopa[i][j:j+len(palabra)] == list(palabra):
                        resultados.append((palabra, [i, j], "derecha"))
                
                # Buscar en dirección vertical (abajo)
                if i + len(palabra) <= filas:
                    if [sopa[x][j] for x in range(i, i+len(palabra))] == list(palabra):
                        resultados.append((palabra, [i, j], "abajo"))
                
                # Buscar en dirección diagonal (derecha y abajo)
                if i + len(palabra) <= filas and j + len(palabra) <= columnas:
                    if [sopa[i+x][j+x] for x in range(len(palabra))] == list(palabra):
                        resultados.append((palabra, [i, j], "diagonal"))
                        
                # Buscar en dirección diagonal (izquierda y abajo)
                if i + len(palabra) <= filas and j - len(palabra) >= -1:
                    if [sopa[i+x][j-x] for x in range(len(palabra))] == list(palabra):
                        resultados.append((palabra, [i, j], "diagonal"))

    return resultados


if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultados)

