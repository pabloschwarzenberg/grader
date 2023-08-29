def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    
    for fila in range(n_filas):
        for columna in range(n_columnas - len(palabra) + 1):
            if all(sopa[fila][columna+i] == palabra[i] for i in range(len(palabra))):
                return [fila, columna], "derecha"
    return None

def buscar_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas):
            if all(sopa[fila+i][columna] == palabra[i] for i in range(len(palabra))):
                return [fila, columna], "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas - len(palabra) + 1):
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
        
        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))
    
    return resultados
