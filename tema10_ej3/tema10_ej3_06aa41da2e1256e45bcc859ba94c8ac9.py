def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = [c for c in linea.strip()]
            sopa.append(fila)
    return sopa

def buscar_palabra_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    n = len(palabra)

    for i in range(n_filas):
        for j in range(n_columnas - n + 1):
            if sopa[i][j:j+n] == palabra:
                return i, j, "derecha"

    return None

def buscar_palabra_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    n = len(palabra)

    for i in range(n_filas - n + 1):
        for j in range(n_columnas):
            if all(sopa[i+k][j] == palabra[k] for k in range(n)):
                return i, j, "abajo"

    return None

def buscar_palabra_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    n = len(palabra)

    for i in range(n_filas - n + 1):
        for j in range(n_columnas - n + 1):
            if all(sopa[i+k][j+k] == palabra[k] for k in range(n)):
                return i, j, "diagonal"

    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        posicion = buscar_palabra_horizontal(sopa, palabra)
        if not posicion:
            posicion = buscar_palabra_vertical(sopa, palabra)
        if not posicion:
            posicion = buscar_palabra_diagonal(sopa, palabra)

        if posicion:
            resultados.append((palabra, [posicion[0], posicion[1]], posicion[2]))

    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)

    for resultado in resultados:
        print(resultado)
