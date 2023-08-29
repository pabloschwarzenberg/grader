def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, 'r') as archivo:
        sopa = [linea.strip().split() for linea in archivo]

    n = len(sopa)  # Número de filas
    m = len(sopa[0])  # Número de columnas

    resultados = []

    # Función auxiliar para verificar si una palabra se encuentra en una dirección específica
    def buscar_palabra(palabra, fila, columna, delta_fila, delta_columna, direccion):
        for letra in palabra:
            if (fila < 0 or fila >= n or columna < 0 or columna >= m or sopa[fila][columna] != letra):
                return False
            fila += delta_fila
            columna += delta_columna
        resultados.append((palabra, [fila-delta_fila, columna-delta_columna], direccion))
        return True

    # Función principal para buscar las palabras en la sopa de letras
    for palabra in palabras:
        for fila in range(n):
            for columna in range(m):
                if buscar_palabra(palabra, fila, columna, 0, 1, "derecha"):
                    continue
                if buscar_palabra(palabra, fila, columna, 1, 0, "abajo"):
                    continue
                if buscar_palabra(palabra, fila, columna, 1, 1, "diagonal"):
                    continue

    return resultados
    
    def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo]
    return sopa


def buscar_horizontal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for i in range(filas):
        for j in range(columnas - len(palabra) + 1):
            if sopa[i][j:j + len(palabra)] == palabra:
                return [i, j], "derecha"
    return None


def buscar_vertical(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for i in range(filas - len(palabra) + 1):
        for j in range(columnas):
            if all(sopa[i + k][j] == palabra[k] for k in range(len(palabra))):
                return [i, j], "abajo"
    return None


def buscar_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for i in range(filas - len(palabra) + 1):
        for j in range(columnas - len(palabra) + 1):
            if all(sopa[i + k][j + k] == palabra[k] for k in range(len(palabra))):
                return [i, j], "diagonal"
    return None


def buscar_palabras(sopa, palabras):
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


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = buscar_palabras(sopa, palabras)
    return resultados



    


           