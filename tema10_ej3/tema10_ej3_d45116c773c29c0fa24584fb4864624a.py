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

    for i in range(n_filas):
        fila = ''.join(sopa[i])
        if palabra in fila:
            columna = fila.index(palabra)
            return [i, columna], "derecha"

    return None

def buscar_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])

    for j in range(n_columnas):
        columna = ''.join(sopa[i][j] for i in range(n_filas))
        if palabra in columna:
            fila = columna.index(palabra)
            return [fila, j], "abajo"

    return None

def buscar_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])

    for i in range(n_filas):
        for j in range(n_columnas):
            if sopa[i][j] == palabra[0]:
                # Verificar diagonal hacia la derecha y hacia abajo
                if i + len(palabra) <= n_filas and j + len(palabra) <= n_columnas:
                    diagonal = ''.join(sopa[i+k][j+k] for k in range(len(palabra)))
                    if diagonal == palabra:
                        return [i, j], "diagonal"

                # Verificar diagonal hacia la izquierda y hacia abajo
                if i + len(palabra) <= n_filas and j - len(palabra) + 1 >= 0:
                    diagonal = ''.join(sopa[i+k][j-k] for k in range(len(palabra)))
                    if diagonal == palabra:
                        return [i, j], "diagonal"

    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        posicion = buscar_horizontal(sopa, palabra)
        if posicion is None:
            posicion = buscar_vertical(sopa, palabra)
        if posicion is None:
            posicion = buscar_diagonal(sopa, palabra)

        if posicion is not None:
            resultados.append((palabra, posicion[0], posicion[1]))

    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa"])
    print(resultados)
