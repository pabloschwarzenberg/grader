def buscar_horizontal(tablero, palabra):
    n = len(tablero)
    m = len(tablero[0])
    resultados = []
    for i in range(n):
        fila = ''.join(tablero[i])
        if palabra in fila:
            indice = fila.index(palabra)
            resultados.append(([i, indice], "derecha"))
    return resultados

def buscar_vertical(tablero, palabra):
    n = len(tablero)
    m = len(tablero[0])
    resultados = []
    for j in range(m):
        columna = ''.join(tablero[i][j] for i in range(n))
        if palabra in columna:
            indice = columna.index(palabra)
            resultados.append(([indice, j], "abajo"))
    return resultados

def buscar_diagonal(tablero, palabra):
    n = len(tablero)
    m = len(tablero[0])
    resultados = []
    for i in range(n - len(palabra) + 1):
        for j in range(m - len(palabra) + 1):
            diagonal = ''.join(tablero[i+k][j+k] for k in range(len(palabra)))
            if diagonal == palabra:
                resultados.append(([i, j], "diagonal"))
    return resultados

def buscar_palabra(tablero, palabra):
    resultados = buscar_horizontal(tablero, palabra)
    if resultados:
        return resultados
    resultados = buscar_vertical(tablero, palabra)
    if resultados:
        return resultados
    resultados = buscar_diagonal(tablero, palabra)
    if resultados:
        return resultados
    return None

def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, "r") as archivo:
        tablero = [linea.strip().split() for linea in archivo]

    resultados = []
    for palabra in palabras:
        resultado = buscar_palabra(tablero, palabra)
        if resultado:
            resultados.append((palabra, resultado[0][0], resultado[0][1]))

    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultados)