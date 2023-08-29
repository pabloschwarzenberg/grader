def cargar_sopa_de_letras(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_horizontal(sopa, palabra, fila, columna):
    largo_palabra = len(palabra)
    largo_sopa = len(sopa[0])
    if columna + largo_palabra > largo_sopa:
        return False
    for i in range(largo_palabra):
        if sopa[fila][columna + i] != palabra[i]:
            return False
    return True

def buscar_vertical(sopa, palabra, fila, columna):
    largo_palabra = len(palabra)
    largo_sopa = len(sopa)
    if fila + largo_palabra > largo_sopa:
        return False
    for i in range(largo_palabra):
        if sopa[fila + i][columna] != palabra[i]:
            return False
    return True

def buscar_diagonal(sopa, palabra, fila, columna):
    largo_palabra = len(palabra)
    largo_sopa = len(sopa)
    largo_fila = len(sopa[0])
    if fila + largo_palabra > largo_sopa or columna + largo_palabra > largo_fila:
        return False
    for i in range(largo_palabra):
        if sopa[fila + i][columna + i] != palabra[i]:
            return False
    return True

def buscar_palabra(sopa, palabra):
    largo_sopa = len(sopa)
    largo_fila = len(sopa[0])
    for fila in range(largo_sopa):
        for columna in range(largo_fila):
            if buscar_horizontal(sopa, palabra, fila, columna):
                return [fila, columna], "derecha"
            elif buscar_vertical(sopa, palabra, fila, columna):
                return [fila, columna], "abajo"
            elif buscar_diagonal(sopa, palabra, fila, columna):
                return [fila, columna], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa_de_letras(nombre_archivo)
    resultados = []
    for palabra in palabras:
        posicion = buscar_palabra(sopa, palabra)
        if posicion is not None:
            resultados.append((palabra, posicion[0], posicion[1]))
    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "hombre", "arboles"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)
