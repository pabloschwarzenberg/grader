def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split(',')
            sopa.append(fila)
    return sopa

def buscar_palabra(sopa, palabra, fila, columna, direccion):
    n = len(sopa)
    m = len(sopa[0])
    longitud = len(palabra)

    # Verificar si la posición inicial es válida
    if fila < 0 or fila >= n or columna < 0 or columna >= m:
        return False

    # Verificar si la palabra cabe en la dirección indicada
    if (direccion == "derecha" and columna + longitud > m) or \
       (direccion == "abajo" and fila + longitud > n) or \
       (direccion == "diagonal" and (fila + longitud > n or columna + longitud > m)):
        return False

    # Verificar si la palabra coincide en la dirección indicada
    for i in range(longitud):
        if direccion == "derecha" and sopa[fila][columna + i] != palabra[i]:
            return False
        elif direccion == "abajo" and sopa[fila + i][columna] != palabra[i]:
            return False
        elif direccion == "diagonal" and sopa[fila + i][columna + i] != palabra[i]:
            return False

    return True
def sopaletras(nombre_archivo,palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        n = len(sopa)
        m = len(sopa[0])
        longitud = len(palabra)

        for fila in range(n):
            for columna in range(m):
                # Verificar en todas las direcciones
                if buscar_palabra(sopa, palabra, fila, columna, "derecha"):
                    resultados.append((palabra, [fila, columna], "derecha"))
                if buscar_palabra(sopa, palabra, fila, columna, "abajo"):
                    resultados.append((palabra, [fila, columna], "abajo"))
                if buscar_palabra(sopa, palabra, fila, columna, "diagonal"):
                    resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           