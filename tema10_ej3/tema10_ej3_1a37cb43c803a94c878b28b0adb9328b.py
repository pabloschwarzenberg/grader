def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa


def buscar_palabra_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for i in range(n_filas):
        fila = ''.join(sopa[i])
        if palabra in fila:
            columna = fila.index(palabra)
            return [i, columna]
    return None


def buscar_palabra_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for j in range(n_columnas):
        columna = ''.join(sopa[i][j] for i in range(n_filas))
        if palabra in columna:
            fila = columna.index(palabra)
            return [fila, j]
    return None


def buscar_palabra_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for i in range(n_filas):
        for j in range(n_columnas):
            diagonal = ''
            k = 0
            while i + k < n_filas and j + k < n_columnas:
                diagonal += sopa[i + k][j + k]
                k += 1
            if palabra in diagonal:
                pos = diagonal.index(palabra)
                return [i + pos, j + pos]
    return None


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        direccion = buscar_palabra_horizontal(sopa, palabra)
        if direccion:
            resultados.append((palabra, direccion, "derecha"))
            continue
        direccion = buscar_palabra_vertical(sopa, palabra)
        if direccion:
            resultados.append((palabra, direccion, "abajo"))
            continue
        direccion = buscar_palabra_diagonal(sopa, palabra)
        if direccion:
            resultados.append((palabra, direccion, "diagonal"))
            continue
    return resultados


if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultados)
