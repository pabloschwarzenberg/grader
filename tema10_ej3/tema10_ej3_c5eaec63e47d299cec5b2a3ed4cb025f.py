def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo]
    return sopa

def buscar_horizontal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for fila in range(filas):
        for col in range(columnas - len(palabra) + 1):
            if sopa[fila][col:col + len(palabra)] == palabra:
                return [fila, col], "derecha"
    return None

def buscar_vertical(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for col in range(columnas):
        for fila in range(filas - len(palabra) + 1):
            if [sopa[fila + i][col] for i in range(len(palabra))] == list(palabra):
                return [fila, col], "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for fila in range(filas - len(palabra) + 1):
        for col in range(columnas - len(palabra) + 1):
            if [sopa[fila + i][col + i] for i in range(len(palabra))] == list(palabra):
                return [fila, col], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_horizontal(sopa, palabra)
        if resultado is None:
            resultado = buscar_vertical(sopa, palabra)
        if resultado is None:
            resultado = buscar_diagonal(sopa, palabra)
        resultados.append((palabra, resultado[0], resultado[1]) if resultado else (palabra, None, None))
    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa"])
    print(resultados)
