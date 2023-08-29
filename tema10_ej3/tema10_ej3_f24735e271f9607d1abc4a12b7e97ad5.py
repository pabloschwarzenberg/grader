def cargar_sopa_de_letras(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for fila in range(n_filas):
        for columna in range(n_columnas - len(palabra) + 1):
            subcadena = "".join(sopa[fila][columna:columna+len(palabra)])
            if subcadena.lower() == palabra.lower():  # Se realiza la comparación ignorando mayúsculas y minúsculas
                return [fila, columna], "derecha"
    return None

def buscar_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas):
            subcadena = "".join(sopa[fila+i][columna] for i in range(len(palabra)))
            if subcadena.lower() == palabra.lower():  # Se realiza la comparación ignorando mayúsculas y minúsculas
                return [fila, columna], "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas - len(palabra) + 1):
            subcadena = "".join(sopa[fila+i][columna+i] for i in range(len(palabra)))
            if subcadena.lower() == palabra.lower():  # Se realiza la comparación ignorando mayúsculas y minúsculas
                return [fila, columna], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa_de_letras(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_horizontal(sopa, palabra)
        if resultado is None:
            resultado = buscar_vertical(sopa, palabra)
        if resultado is None:
            resultado = buscar_diagonal(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))
        else:
            resultados.append((palabra, [], "No encontrada"))
    return resultados

if __name__ == "_main_":
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "cra", "aro"]
    resultado = sopaletras(nombre_archivo, palabras)
    print(resultado)