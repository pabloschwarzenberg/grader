def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
    tablero = [list(linea.strip()) for linea in lineas]
    return tablero

def buscar_horizontal(tablero, palabra):
    for fila in range(len(tablero)):
        fila_str = "".join(tablero[fila])
        if palabra in fila_str:
            columna = fila_str.index(palabra)
            return [fila, columna], "derecha"
    return None

def buscar_vertical(tablero, palabra):
    for columna in range(len(tablero[0])):
        columna_str = "".join(tablero[fila][columna] for fila in range(len(tablero)))
        if palabra in columna_str:
            fila = columna_str.index(palabra)
            return [fila, columna], "abajo"
    return None

def buscar_diagonal(tablero, palabra):
    N = len(tablero)
    M = len(tablero[0])
    for fila in range(N):
        for columna in range(M):
            diagonal = ""
            i, j = fila, columna
            while i < N and j < M:
                diagonal += tablero[i][j]
                i += 1
                j += 1
            if palabra in diagonal:
                inicio_fila = diagonal.index(palabra)
                inicio_columna = columna + inicio_fila
                return [fila + inicio_fila, columna + inicio_fila], "diagonal"

            diagonal = ""
            i, j = fila, columna
            while i < N and j >= 0:
                diagonal += tablero[i][j]
                i += 1
                j -= 1
            if palabra in diagonal:
                inicio_fila = diagonal.index(palabra)
                inicio_columna = columna - inicio_fila
                return [fila + inicio_fila, columna - inicio_fila], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    tablero = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
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
            continue

    return resultados

if __name__ == "__main__":
    archivo_sopa = "sopa.txt"
    palabras_buscar = ["casa", "cra", "aro"]
    resultado = sopaletras(archivo_sopa, palabras_buscar)
    print(resultado)
