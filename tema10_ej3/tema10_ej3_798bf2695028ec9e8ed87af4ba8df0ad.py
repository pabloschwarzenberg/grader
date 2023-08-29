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
    longitud_palabra = len(palabra)
    for i in range(filas):
        for j in range(columnas - longitud_palabra + 1):
            if sopa[i][j:j + longitud_palabra] == palabra:
                return [i, j], "derecha"
    return None

def buscar_vertical(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    longitud_palabra = len(palabra)
    for i in range(filas - longitud_palabra + 1):
        for j in range(columnas):
            if all(sopa[i + k][j] == palabra[k] for k in range(longitud_palabra)):
                return [i, j], "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    longitud_palabra = len(palabra)
    for i in range(filas - longitud_palabra + 1):
        for j in range(columnas - longitud_palabra + 1):
            if all(sopa[i + k][j + k] == palabra[k] for k in range(longitud_palabra)):
                return [i, j], "diagonal"
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
        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))
    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)
