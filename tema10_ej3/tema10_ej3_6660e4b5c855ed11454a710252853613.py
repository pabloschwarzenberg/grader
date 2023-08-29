def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [linea.strip().split() for linea in archivo]
    return sopa


def buscar_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    palabra = palabra.upper() 
    for fila in range(n_filas):
        for columna in range(n_columnas - len(palabra) + 1):
            if sopa[fila][columna:columna + len(palabra)] == list(palabra):
                return [fila, columna], "derecha"
    return None


def buscar_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    palabra = palabra.upper() 
    for columna in range(n_columnas):
        for fila in range(n_filas - len(palabra) + 1):
            if [sopa[fila + i][columna] for i in range(len(palabra))] == list(palabra):
                return [fila, columna], "abajo"
    return None


def buscar_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    palabra = palabra.upper() 
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas - len(palabra) + 1):
            if [sopa[fila + i][columna + i] for i in range(len(palabra))] == list(palabra):
                return [fila, columna], "diagonal"
    return None


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_horizontal(sopa, palabra)
        if resultado is None:
            resultado = buscar_vertical(sopa, palabra)
        if resultado is None:
            resultado = buscar_diagonal(sopa, palabra)
        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))
    return resultados



if _name_ == "_main_":
    archivo = "sopa.txt"
    palabras = []
    añadir_palabra = input("Ingrese una palabra: ")
    palabras.append(añadir_palabra)
    resultado = sopaletras(archivo, palabras)
    print(resultado)
           