def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_horizontal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for fila in range(filas):
        for columna in range(columnas - len(palabra) + 1):
            if sopa[fila][columna:columna+len(palabra)] == list(palabra):
                return [fila, columna], "derecha"
    return None

def buscar_vertical(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for fila in range(filas - len(palabra) + 1):
        for columna in range(columnas):
            if all(sopa[fila+i][columna] == palabra[i] for i in range(len(palabra))):
                return [fila, columna], "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for fila in range(filas - len(palabra) + 1):
        for columna in range(columnas - len(palabra) + 1):
            if all(sopa[fila+i][columna+i] == palabra[i] for i in range(len(palabra))):
                return [fila, columna], "diagonal"
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
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultados)
