def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    
    for palabra in palabras:
        for i in range(len(sopa)):
            for j in range(len(sopa[0])):
                if sopa[i][j] == palabra[0]:
                    for direccion in ["derecha", "abajo", "diagonal"]:
                        if buscar_palabra(sopa, palabra, i, j, direccion):
                            resultados.append((palabra, [i, j], direccion))
    
    return resultados

def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_palabra(sopa, palabra, fila, columna, direccion):
    n = len(sopa)
    m = len(sopa[0])
    longitud = len(palabra)
    
    if direccion == "derecha":
        if columna + longitud > m:
            return False
        for i in range(longitud):
            if sopa[fila][columna + i] != palabra[i]:
                return False
        return True
    elif direccion == "abajo":
        if fila + longitud > n:
            return False
        for i in range(longitud):
            if sopa[fila + i][columna] != palabra[i]:
                return False
        return True
    elif direccion == "diagonal":
        if fila + longitud > n or columna + longitud > m:
            return False
        for i in range(longitud):
            if sopa[fila + i][columna + i] != palabra[i]:
                return False
        return True
    else:
        return False
