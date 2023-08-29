def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            sopa.append(linea.strip().split())
    return sopa


def buscar_horizontal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    palabra_len = len(palabra)

    for fila in range(filas):
        for col in range(columnas - palabra_len + 1):
            if sopa[fila][col:col + palabra_len] == palabra:
                return [fila, col], "derecha"
    return None


def buscar_vertical(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    palabra_len = len(palabra)

    for fila in range(filas - palabra_len + 1):
        for col in range(columnas):
            if all(sopa[fila + i][col] == palabra[i] for i in range(palabra_len)):
                return [fila, col], "abajo"
    return None


def buscar_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    palabra_len = len(palabra)

    for fila in range(filas - palabra_len + 1):
        for col in range(columnas - palabra_len + 1):
            if all(sopa[fila + i][col + i] == palabra[i] for i in range(palabra_len)):
                return [fila, col], "diagonal"
    return None


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        resultado = buscar_horizontal(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))
            continue

        resultado = buscar_vertical(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))
            continue

        resultado = buscar_diagonal(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))

    return resultados


if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultado = sopaletras(nombre_archivo, palabras)
    print(resultado)
