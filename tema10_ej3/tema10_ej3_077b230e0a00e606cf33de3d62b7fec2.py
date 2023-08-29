def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras y obtener el tablero
    with open(nombre_archivo, 'r') as archivo:
        tablero = [linea.strip().split() for linea in archivo]

    n_filas = len(tablero)
    n_columnas = len(tablero[0])

    resultados = []

    # Buscar las palabras en el tablero
    for palabra in palabras:
        encontrada = False
        direccion = ""
        fila_inicial = -1
        columna_inicial = -1

        # Buscar en forma horizontal
        for i in range(n_filas):
            fila = tablero[i]
            fila_str = ''.join(fila)
            if palabra in fila_str:
                columna_inicial = fila_str.index(palabra)
                fila_inicial = i
                direccion = "derecha"
                encontrada = True
                break

        if not encontrada:
            # Buscar en forma vertical
            for j in range(n_columnas):
                columna = [fila[j] for fila in tablero]
                columna_str = ''.join(columna)
                if palabra in columna_str:
                    fila_inicial = columna_str.index(palabra)
                    columna_inicial = j
                    direccion = "abajo"
                    encontrada = True
                    break

        if not encontrada:
            # Buscar en forma diagonal de izquierda a derecha
            for i in range(n_filas):
                for j in range(n_columnas):
                    diagonal = []
                    fila = i
                    columna = j
                    while fila < n_filas and columna < n_columnas:
                        diagonal.append(tablero[fila][columna])
                        fila += 1
                        columna += 1
                    diagonal_str = ''.join(diagonal)
                    if palabra in diagonal_str:
                        fila_inicial = diagonal_str.index(palabra) + i
                        columna_inicial = diagonal_str.index(palabra) + j
                        direccion = "diagonal"
                        encontrada = True
                        break

        if encontrada:
            resultados.append((palabra, [fila_inicial, columna_inicial], direccion))

    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)
