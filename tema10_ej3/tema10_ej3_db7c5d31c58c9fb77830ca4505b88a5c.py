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
        for j in range(n_columnas - len(palabra) + 1):
            if sopa[i][j:j+len(palabra)] == palabra:
                return [i, j], "derecha"
    return None

def buscar_palabra_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for i in range(n_filas - len(palabra) + 1):
        for j in range(n_columnas):
            columna = [sopa[k][j] for k in range(i, i+len(palabra))]
            if columna == palabra:
                return [i, j], "abajo"
    return None

def buscar_palabra_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for i in range(n_filas - len(palabra) + 1):
        for j in range(n_columnas - len(palabra) + 1):
            diagonal = [sopa[i+k][j+k] for k in range(len(palabra))]
            if diagonal == palabra:
                return [i, j], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_palabra_horizontal(sopa, palabra)
        if resultado is None:
            resultado = buscar_palabra_diagonal(sopa, palabra)
        if resultado is None:
            resultado = buscar_palabra_vertical(sopa, palabra)
        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))
    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    for resultado in resultados:
        print(resultado)
