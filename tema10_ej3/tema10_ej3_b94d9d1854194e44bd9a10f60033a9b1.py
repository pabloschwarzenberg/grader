def cargar_sopa_de_letras(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            sopa.append(linea.strip().split())
    return sopa


def buscar_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for fila in range(n_filas):
        for columna in range(n_columnas - len(palabra) + 1):
            if sopa[fila][columna:columna+len(palabra)] == palabra:
                return fila, columna, 'derecha'
    return None


def buscar_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas):
            if all(sopa[fila+i][columna] == palabra[i] for i in range(len(palabra))):
                return fila, columna, 'abajo'
    return None


def buscar_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas - len(palabra) + 1):
            if all(sopa[fila+i][columna+i] == palabra[i] for i in range(len(palabra))):
                return fila, columna, 'diagonal'
    return None


def buscar_palabra_en_sopa(sopa, palabra):
    resultado = []
    resultado_horizontal = buscar_horizontal(sopa, palabra)
    if resultado_horizontal:
        resultado.append((palabra, [resultado_horizontal[0], resultado_horizontal[1]], resultado_horizontal[2]))

    resultado_vertical = buscar_vertical(sopa, palabra)
    if resultado_vertical:
        resultado.append((palabra, [resultado_vertical[0], resultado_vertical[1]], resultado_vertical[2]))

    resultado_diagonal = buscar_diagonal(sopa, palabra)
    if resultado_diagonal:
        resultado.append((palabra, [resultado_diagonal[0], resultado_diagonal[1]], resultado_diagonal[2]))

    return resultado


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa_de_letras(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultados.extend(buscar_palabra_en_sopa(sopa, palabra))
    return resultados


if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa"])
    print(resultados)
