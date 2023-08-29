def obtener_sopa_letras(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    print(sopa)
    return sopa


def buscar_palabra_horizontal(sopa, buscar, palabra):
    for i in range(len(sopa)):
        fila = ''.join(sopa[i])
        if buscar in fila:
            columna = fila.index(buscar)
            return [i, columna], "derecha"
    return None


def buscar_palabra_vertical(sopa, buscar, palabra):
    for j in range(len(sopa[0])):
        columna = ''.join(sopa[i][j] for i in range(len(sopa)))
        if buscar in columna:
            fila = columna.index(buscar)
            return [fila, j], "abajo"
    return None


def buscar_palabra_diagonal(sopa, buscar, palabra):
    n = len(sopa)
    m = len(sopa[0])

    for i in range(n):
        for j in range(m):
            k = 0
            while i + k < n and j + k < m and sopa[i + k][j + k] == buscar[k]:
                k += 1
                if k == len(buscar):
                    return [i, j], "diagonal"
    return None


def sopaletras(nombre_archivo, palabras):
    sopa = obtener_sopa_letras(nombre_archivo)
    resultados = []

    for palabra in palabras:
        buscar = palabra.upper()
        resultado = buscar_palabra_horizontal(sopa, buscar, palabra)
        if resultado is None:
            resultado = buscar_palabra_vertical(sopa, buscar, palabra)
        if resultado is None:
            resultado = buscar_palabra_diagonal(sopa, buscar, palabra)

        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))

    return resultados


if __name__ == "__main__":
    archivo_sopa = "sopa.txt"
    palabras_buscar = ["casa"]
    resultados = sopaletras(archivo_sopa, palabras_buscar)
    print(resultados)