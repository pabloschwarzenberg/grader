def cargar_sopa_de_letras(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split(',')
            sopa.append(fila)
    return sopa


def buscar_palabra(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])

    # Buscar palabra en horizontal
    for i in range(n):
        fila = ''.join(sopa[i])
        if palabra in fila:
            columna_inicial = fila.index(palabra)
            return [i, columna_inicial], "derecha"

    # Buscar palabra en vertical
    for j in range(m):
        columna = ''.join([sopa[i][j] for i in range(n)])
        if palabra in columna:
            fila_inicial = columna.index(palabra)
            return [fila_inicial, j], "abajo"

    # Buscar palabra en diagonal (esquina superior izquierda a esquina inferior derecha)
    for i in range(n):
        for j in range(m):
            diagonal = ''
            k = 0
            while i + k < n and j + k < m:
                diagonal += sopa[i + k][j + k]
                if palabra in diagonal:
                    pos_inicial = diagonal.index(palabra)
                    return [i + pos_inicial, j + pos_inicial], "diagonal"

    return None


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa_de_letras(nombre_archivo)
    resultados = []

    for palabra in palabras:
        posicion = buscar_palabra(sopa, palabra)
        if posicion:
            resultados.append((palabra, posicion[0], posicion[1]))

    return resultados


if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "hola", "gato", "perro"]
    resultado = sopaletras(nombre_archivo, palabras)
    print(resultado)


           