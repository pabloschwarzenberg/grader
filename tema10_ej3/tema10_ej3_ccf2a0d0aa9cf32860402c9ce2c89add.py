import os

def cargar_sopa(nombre_archivo):
    ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
    sopa = []
    with open(ruta, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            sopa.append(row)
    return sopa

def buscar_horizontal(sopa, palabra):
    for i in range(len(sopa)):
        row = ''.join(sopa[i])
        if palabra in row:
            col_start = row.index(palabra)
            return [i, col_start], "derecha"
    return None

def buscar_vertical(sopa, palabra):
    for j in range(len(sopa[0])):
        col = ''.join([sopa[i][j] for i in range(len(sopa))])
        if palabra in col:
            row_start = col.index(palabra)
            return [row_start, j], "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n):
        for j in range(m):
            if i + len(palabra) <= n and j + len(palabra) <= m:
                diag = ''.join([sopa[i+k][j+k] for k in range(len(palabra))])
                if palabra in diag:
                    start = [i+k for k in range(len(palabra))]
                    return start, "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    result = []
    for palabra in palabras:
        # Buscar en forma horizontal
        found = buscar_horizontal(sopa, palabra)
        if found:
            result.append((palabra, found[0], found[1]))
            continue

        # Buscar en forma vertical
        found = buscar_vertical(sopa, palabra)
        if found:
            result.append((palabra, found[0], found[1]))
            continue

        # Buscar en forma diagonal
        found = buscar_diagonal(sopa, palabra)
        if found:
            result.append((palabra, found[0], found[1]))

    return result

if __name__ == "__main__":
    archivo = "sopa.txt"
    palabras = ["casa"]

    soluciones = sopaletras(archivo, palabras)
    print(soluciones)
