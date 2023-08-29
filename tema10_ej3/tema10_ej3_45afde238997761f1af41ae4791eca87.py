def buscar_palabra(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])

    for fila in range(n):
        for columna in range(m):
            # Buscar en horizontal
            if ''.join(sopa[fila][columna:columna + len(palabra)]) == palabra:
                return [fila, columna], "derecha"
            # Buscar en vertical
            if fila + len(palabra) <= n and ''.join(sopa[fila + k][columna] for k in range(len(palabra))) == palabra:
                return [fila, columna], "abajo"
            # Buscar en diagonal hacia abajo
            if fila + len(palabra) <= n and columna + len(palabra) <= m and ''.join(sopa[fila + k][columna + k] for k in range(len(palabra))) == palabra:
                return [fila, columna], "diagonal"
            # Buscar en diagonal hacia arriba
            if fila - len(palabra) >= -1 and columna + len(palabra) <= m and ''.join(sopa[fila - k][columna + k] for k in range(len(palabra))) == palabra:
                return [fila, columna], "diagonal"

    return None

def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo]

    resultados = []

    for palabra in palabras:
        palabra = palabra.lower()
        posicion = buscar_palabra(sopa, palabra)
        if posicion:
            resultados.append((palabra, [posicion[0][0], posicion[0][1]], posicion[1]))

    return resultados
