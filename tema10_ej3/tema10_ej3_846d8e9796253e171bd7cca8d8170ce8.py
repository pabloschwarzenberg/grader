def cargar_sopa_de_letras(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        sopa = [list(linea.strip()) for linea in archivo]
    return sopa

def buscar_palabra_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    len_palabra = len(palabra)
    for fila in range(n_filas):
        for columna in range(n_columnas - len_palabra + 1):
            if ''.join(sopa[fila][columna:columna+len_palabra]) == palabra:
                return fila, columna, "derecha"
    return None

def buscar_palabra_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    len_palabra = len(palabra)
    for fila in range(n_filas - len_palabra + 1):
        for columna in range(n_columnas):
            if all(sopa[fila+i][columna] == palabra[i] for i in range(len_palabra)):
                return fila, columna, "abajo"
    return None

def buscar_palabra_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    len_palabra = len(palabra)
    for fila in range(n_filas - len_palabra + 1):
        for columna in range(n_columnas - len_palabra + 1):
            if all(sopa[fila+i][columna+i] == palabra[i] for i in range(len_palabra)):
                return fila, columna, "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa_de_letras(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_palabra_horizontal(sopa, palabra)
        if resultado is None:
            resultado = buscar_palabra_vertical(sopa, palabra)
        if resultado is None:
            resultado = buscar_palabra_diagonal(sopa, palabra)
        resultados.append(resultado)
    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    for resultado in resultados:
        if resultado:
            palabra = resultado[0]
            posicion = resultado[1]
            direccion = resultado[2]
            print(f"Palabra: {palabra}, Posición: {posicion}, Dirección: {direccion}")
        else:
            print("Palabra no encontrada")
