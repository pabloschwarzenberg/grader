def leer_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa


def buscar_horizontal(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n):
        for j in range(m - len(palabra) + 1):
            if sopa[i][j:j+len(palabra)] == palabra:
                return i, j, "derecha"
    return palabra


def buscar_vertical(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n - len(palabra) + 1):
        for j in range(m):
            columna = [sopa[k][j] for k in range(i, i+len(palabra))]
            if columna == palabra:
                return i, j, "abajo"
    return palabra


def buscar_diagonal(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n - len(palabra) + 1):
        for j in range(m - len(palabra) + 1):
            diagonal = [sopa[i+k][j+k] for k in range(len(palabra))]
            if diagonal == palabra:
                return i, j, "diagonal"
    return palabra


def sopaletras(nombre_archivo, palabras):
    sopa = leer_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_horizontal(sopa, palabra)
        if resultado is None:
            resultado = buscar_vertical(sopa, palabra)
        if resultado is None:
            resultado = buscar_diagonal(sopa, palabra)
        if resultado is not None:
            resultados.append((palabra, [resultado[0], resultado[1]], resultado[2]))
    return resultados



if __name__ == "__main__":
    archivo_sopa = "sopa.txt"
    palabras_buscar = ["casa"]
    resultado = sopaletras(archivo_sopa, palabras_buscar)
    print(resultado)