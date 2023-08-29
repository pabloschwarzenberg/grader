def buscar_palabra(tablero, palabra, filas, columnas):
    # Buscar palabra en dirección horizontal (izquierda a derecha)
    for i in range(filas):
        for j in range(columnas - len(palabra) + 1):
            if tablero[i][j:j + len(palabra)] == palabra:
                return [i, j], "derecha"

    # Buscar palabra en dirección vertical (arriba a abajo)
    for i in range(filas - len(palabra) + 1):
        for j in range(columnas):
            columna = [tablero[i + k][j] for k in range(len(palabra))]
            if columna == list(palabra):
                return [i, j], "abajo"

    # Buscar palabra en dirección diagonal (esquina superior izquierda a esquina inferior derecha)
    for i in range(filas - len(palabra) + 1):
        for j in range(columnas - len(palabra) + 1):
            diagonal = [tablero[i + k][j + k] for k in range(len(palabra))]
            if diagonal == list(palabra):
                return [i, j], "diagonal"

    # La palabra no fue encontrada
    return None


def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, 'r') as file:
        lines = file.readlines()

    # Obtener las dimensiones del tablero
    filas = len(lines)
    columnas = len(lines[0].strip().split())

    # Crear el tablero a partir del archivo
    tablero = [line.strip().split() for line in lines]

    resultados = []

    # Buscar cada palabra en el tablero
    for palabra in palabras:
        posicion = buscar_palabra(tablero, palabra, filas, columnas)
        if posicion:
            resultados.append((palabra, posicion[0], posicion[1]))

    return resultados


if __name__ == "__main__":
    archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(archivo, palabras)
    for resultado in resultados:
        palabra = resultado[0]
        posicion = resultado[1]
        direccion = resultado[2]
        print((palabra, posicion, direccion))
