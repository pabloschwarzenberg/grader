def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa


def buscar_palabra_horizontal(sopa, palabra):
    for i in range(len(sopa)):
        fila = "".join(sopa[i])
        if palabra in fila:
            columna_inicio = fila.index(palabra)
            return [i, columna_inicio], "derecha"
    return None


def buscar_palabra_vertical(sopa, palabra):
    for j in range(len(sopa[0])):
        columna = "".join([fila[j] for fila in sopa])
        if palabra in columna:
            fila_inicio = columna.index(palabra)
            return [fila_inicio, j], "abajo"
    return None


def buscar_palabra_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for i in range(filas):
        for j in range(columnas):
            k = 0
            while i + k < filas and j + k < columnas and sopa[i + k][j + k] == palabra[k]:
                k += 1
                if k == len(palabra):
                    return [i, j], "diagonal"
    return None


def buscar_palabra(sopa, palabra):
   pos, direccion = buscar_palabra_horizontal(sopa, palabra)
    if pos:
        return pos, direccion

    pos, direccion = buscar_palabra_vertical(sopa, palabra)
    if pos:
        return pos, direccion

    pos, direccion = buscar_palabra_diagonal(sopa, palabra)
    if pos:
        return pos, direccion

    return None


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        pos, direccion = buscar_palabra(sopa, palabra)
        if pos:
            resultados.append((palabra, pos, direccion))
    return resultados


if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)
