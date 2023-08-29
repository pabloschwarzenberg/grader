def leer_sopa_de_letras(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            sopa.append(list(linea.strip()))
    return sopa

def buscar_horizontal(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n):
        for j in range(m - len(palabra) + 1):
            if sopa[i][j:j+len(palabra)] == palabra:
                return [i, j], "derecha"
    return None

def buscar_vertical(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n - len(palabra) + 1):
        for j in range(m):
            if all(sopa[i+k][j] == palabra[k] for k in range(len(palabra))):
                return [i, j], "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n - len(palabra) + 1):
        for j in range(m - len(palabra) + 1):
            if all(sopa[i+k][j+k] == palabra[k] for k in range(len(palabra))):
                return [i, j], "diagonal"
            if all(sopa[i+k][j-k] == palabra[k] for k in range(len(palabra))):
                return [i, j], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = leer_sopa_de_letras(nombre_archivo)
    resultados = []
    for palabra in palabras:
        encontrado = buscar_horizontal(sopa, palabra)
        if encontrado is None:
            encontrado = buscar_vertical(sopa, palabra)
        if encontrado is None:
            encontrado = buscar_diagonal(sopa, palabra)
        if encontrado is not None:
            resultados.append((palabra, encontrado[0], encontrado[1]))
    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultados)
