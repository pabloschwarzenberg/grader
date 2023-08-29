import numpy as np

def encontrar_palabra(sopa, palabra):
    n, m = sopa.shape

    # Buscar palabra de izquierda a derecha
    for i in range(n):
        for j in range(m - len(palabra) + 1):
            if all(sopa[i, j+k] == palabra[k] for k in range(len(palabra))):
                return [i, j], "derecha"

    # Buscar palabra de arriba a abajo
    for i in range(n - len(palabra) + 1):
        for j in range(m):
            if all(sopa[i+k, j] == palabra[k] for k in range(len(palabra))):
                return [i, j], "abajo"

    # Buscar palabra en diagonal de izquierda arriba a derecha abajo
    for i in range(n - len(palabra) + 1):
        for j in range(m - len(palabra) + 1):
            if all(sopa[i+k, j+k] == palabra[k] for k in range(len(palabra))):
                return [i, j], "diagonal"

    # Buscar palabra en diagonal de izquierda abajo a derecha arriba
    for i in range(len(palabra) - 1, n):
        for j in range(m - len(palabra) + 1):
            if all(sopa[i-k, j+k] == palabra[k] for k in range(len(palabra))):
                return [i, j], "diagonal"

    return None

def sopaletras(nombre_archivo, palabras):
    # Leer archivo de sopa de letras
    sopa = np.genfromtxt(nombre_archivo, dtype=str, delimiter=' ')

    resultados = []
    for palabra in palabras:
        inicio, direccion = encontrar_palabra(sopa, palabra)
        if inicio:
            resultados.append((palabra, inicio, direccion))

    return resultados

if __name__ == "__main__":
    resultado = sopaletras("sopa.txt", ["casa"])
    print(resultado)
