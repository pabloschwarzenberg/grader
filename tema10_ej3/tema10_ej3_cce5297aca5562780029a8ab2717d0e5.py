def cargar_sopa(nombre_archivo):
    # Lee el archivo de la sopa de letras y devuelve el tablero como una matriz
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo]
    return sopa

def buscar_horizontal(sopa, palabra):
    # Busca la palabra en dirección horizontal (de izquierda a derecha)
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    longitud_palabra = len(palabra)

    for i in range(n_filas):
        for j in range(n_columnas - longitud_palabra + 1):
            if sopa[i][j:j+longitud_palabra] == list(palabra):
                return [i, j], "derecha"
    return None

def buscar_vertical(sopa, palabra):
    # Busca la palabra en dirección vertical (de arriba a abajo)
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    longitud_palabra = len(palabra)

    for i in range(n_filas - longitud_palabra + 1):
        for j in range(n_columnas):
            if all(sopa[i+k][j] == palabra[k] for k in range(longitud_palabra)):
                return [i, j], "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    # Busca la palabra en dirección diagonal (de esquina superior izquierda a esquina inferior derecha)
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    longitud_palabra = len(palabra)

    for i in range(n_filas - longitud_palabra + 1):
        for j in range(n_columnas - longitud_palabra + 1):
            if all(sopa[i+k][j+k] == palabra[k] for k in range(longitud_palabra)):
                return [i, j], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        posicion = buscar_horizontal(sopa, palabra)
        if posicion:
            resultados.append((palabra, posicion[0], posicion[1]))
            continue

        posicion = buscar_vertical(sopa, palabra)
        if posicion:
            resultados.append((palabra, posicion[0], posicion[1]))
            continue

        posicion = buscar_diagonal(sopa, palabra)
        if posicion:
            resultados.append((palabra, posicion[0], posicion[1]))

    return resultados
