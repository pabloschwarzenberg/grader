def cargar_sopa(nombre_archivo):
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
    return None

def buscar_vertical(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n - len(palabra) + 1):
        for j in range(m):
            if all(sopa[i+k][j] == palabra[k] for k in range(len(palabra))):
                return i, j, "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n - len(palabra) + 1):
        for j in range(m - len(palabra) + 1):
            if all(sopa[i+k][j+k] == palabra[k] for k in range(len(palabra))):
                return i, j, "diagonal"
    for i in range(n - len(palabra) + 1):
        for j in range(len(palabra) - 1, m):
            if all(sopa[i+k][j-k] == palabra[k] for k in range(len(palabra))):
                return i, j, "diagonal"
    return None

def buscar_palabra(sopa, palabra):
    resultado = []
    resultado_horizontal = buscar_horizontal(sopa, palabra)
    resultado_vertical = buscar_vertical(sopa, palabra)
    resultado_diagonal = buscar_diagonal(sopa, palabra)
    if resultado_horizontal:
        resultado.append((palabra, [resultado_horizontal[0], resultado_horizontal[1]], resultado_horizontal[2]))
    if resultado_vertical:
        resultado.append((palabra, [resultado_vertical[0], resultado_vertical[1]], resultado_vertical[2]))
    if resultado_diagonal:
        resultado.append((palabra, [resultado_diagonal[0], resultado_diagonal[1]], resultado_diagonal[2]))
    return resultado

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado_palabra = buscar_palabra(sopa, palabra)
        resultados.extend(resultado_palabra)
    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "cra", "aro"]
    print(sopaletras(nombre_archivo, palabras))
