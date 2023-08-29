def buscar_palabra_horizontal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    largo_palabra = len(palabra)

    for fila in range(filas):
        for columna in range(columnas - largo_palabra + 1):
            if sopa[fila][columna:columna + largo_palabra] == palabra:
                return [fila, columna], "derecha"
    return None

def buscar_palabra_vertical(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    largo_palabra = len(palabra)

    for fila in range(filas - largo_palabra + 1):
        for columna in range(columnas):
            palabra_vertical = ''.join(sopa[fila + i][columna] for i in range(largo_palabra))
            if palabra_vertical == palabra:
                return [fila, columna], "abajo"
    return None

def buscar_palabra_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    largo_palabra = len(palabra)

    for fila in range(filas - largo_palabra + 1):
        for columna in range(columnas - largo_palabra + 1):
            palabra_diagonal = ''.join(sopa[fila + i][columna + i] for i in range(largo_palabra))
            if palabra_diagonal == palabra:
                return [fila, columna], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    # Cargar la sopa de letras desde el archivo
    with open(nombre_archivo, 'r') as archivo:
        sopa = [linea.strip().split() for linea in archivo]

    resultados = []
    for palabra in palabras:
        resultado_horizontal = buscar_palabra_horizontal(sopa, palabra)
        if resultado_horizontal:
            resultados.append((palabra, resultado_horizontal[0], resultado_horizontal[1]))

        resultado_vertical = buscar_palabra_vertical(sopa, palabra)
        if resultado_vertical:
            resultados.append((palabra, resultado_vertical[0], resultado_vertical[1]))

        resultado_diagonal = buscar_palabra_diagonal(sopa, palabra)
        if resultado_diagonal:
            resultados.append((palabra, resultado_diagonal[0], resultado_diagonal[1]))

    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    archivo_sopa = "sopa.txt"
    palabras_buscar = ["casa", "cra", "aro"]
    resultados = sopaletras(archivo_sopa, palabras_buscar)
    print(resultados)
