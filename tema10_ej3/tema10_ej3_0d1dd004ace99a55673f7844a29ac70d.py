def cargar_tablero(nombre_archivo):
    tablero = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            tablero.append(fila)
    return tablero

def buscar_horizontal(tablero, palabra):
    for fila in range(len(tablero)):
        for col in range(len(tablero[fila]) - len(palabra) + 1):
            if all(tablero[fila][col+i] == palabra[i] for i in range(len(palabra))):
                return [fila, col], "derecha"
    return None

def buscar_vertical(tablero, palabra):
    for fila in range(len(tablero) - len(palabra) + 1):
        for col in range(len(tablero[fila])):
            if all(tablero[fila+i][col] == palabra[i] for i in range(len(palabra))):
                return [fila, col], "abajo"
    return None

def buscar_diagonal(tablero, palabra):
    for fila in range(len(tablero) - len(palabra) + 1):
        for col in range(len(tablero[fila]) - len(palabra) + 1):
            if all(tablero[fila+i][col+i] == palabra[i] for i in range(len(palabra))):
                return [fila, col], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    tablero = cargar_tablero(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_horizontal(tablero, palabra)
        if resultado is None:
            resultado = buscar_vertical(tablero, palabra)
        if resultado is None:
            resultado = buscar_diagonal(tablero, palabra)
        resultados.append((palabra, resultado[0], resultado[1]) if resultado else (palabra, [], "No encontrada"))
    return resultados

# Ejemplo de uso con ruta completa del archivo
resultado = sopaletras("/ruta/completa/sopa.txt", ["casa"])
print(resultado)
