def buscar_horizontal(tablero, palabra):
    for fila in range(len(tablero)):
        for col in range(len(tablero[0]) - len(palabra) + 1):
            if tablero[fila][col:col+len(palabra)] == palabra:
                return (fila, col), "derecha"
    return None

def buscar_vertical(tablero, palabra):
    for fila in range(len(tablero) - len(palabra) + 1):
        for col in range(len(tablero[0])):
            if all(tablero[fila+i][col] == palabra[i] for i in range(len(palabra))):
                return (fila, col), "abajo"
    return None

def buscar_diagonal(tablero, palabra):
    for fila in range(len(tablero) - len(palabra) + 1):
        for col in range(len(tablero[0]) - len(palabra) + 1):
            if all(tablero[fila+i][col+i] == palabra[i] for i in range(len(palabra))):
                return (fila, col), "diagonal"
    return None

def sopa_letras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, 'r') as archivo:
        tablero = [linea.strip().split() for linea in archivo]

    resultados = []
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir la palabra a minúsculas para buscar sin distinción de mayúsculas

        resultado = buscar_horizontal(tablero, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))
            continue

        resultado = buscar_vertical(tablero, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))
            continue

        resultado = buscar_diagonal(tablero, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))

    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "cra", "aro"]

    resultados = sopa_letras(nombre_archivo, palabras)
    print(resultados)
