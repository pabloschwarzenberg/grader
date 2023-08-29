def cargar_sopa_de_letras(nombre_archivo):
    matriz = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split(',')
            matriz.append(fila)
    return matriz
def buscar_palabra_horizontal(sopa, palabra, fila, columna):
    n = len(palabra)
    m = len(sopa[0])
    if columna + n > m:
        return False
    for i in range(n):
        if sopa[fila][columna+i] != palabra[i]:
            return False
    return True
def buscar_palabra_vertical(sopa, palabra, fila, columna):
    n = len(palabra)
    m = len(sopa)
    if fila + n > m:
        return False
    for i in range(n):
        if sopa[fila+i][columna] != palabra[i]:
            return False
    return True
def buscar_palabra_diagonal(sopa, palabra, fila, columna):
    n = len(palabra)
    m = len(sopa)
    if fila + n > m or columna + n > m:
        return False
    for i in range(n):
        if sopa[fila+i][columna+i] != palabra[i]:
            return False
    return True