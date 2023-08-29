def cargar_sopa_de_letras(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split(',')
            sopa.append(fila)
    return sopa

def buscar_horizontal(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n):
        fila = ''.join(sopa[i])
        if palabra in fila:
            columna = fila.index(palabra)
            return (i, columna), "derecha"
    return None

def buscar_vertical(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for j in range(m):
        columna = ''.join(sopa[i][j] for i in range(n))
        if palabra in columna:
            fila = columna.index(palabra)
            return (fila, j), "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n):
        for j in range(m):
            if i + len(palabra) <= n and j + len(palabra) <= m:
                diagonal = ''.join(sopa[i+k][j+k] for k in range(len(palabra)))
                if palabra == diagonal:
                    return (i, j), "diagonal"
    return None

def buscar_palabras(sopa, palabras):
    resultados = []
    for palabra in palabras:
        posicion = buscar_horizontal(sopa, palabra)
        if posicion is None:
            posicion = buscar_vertical(sopa, palabra)
        if posicion is None:
            posicion = buscar_diagonal(sopa, palabra)
        resultados.append((palabra, posicion[0], posicion[1]))
    return resultados

# Ejemplo de uso
nombre_archivo = "sopa.txt"
palabras = ["CASA", "ROSA", "MAR", "SOL"]
sopa = cargar_sopa_de_letras(nombre_archivo)
resultados = buscar_palabras(sopa, palabras)
for resultado in resultados:
    print(resultado)


           