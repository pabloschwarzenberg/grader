def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            sopa.append(linea.strip().split())
    return sopa

def buscar_palabra(sopa, palabra, fila, columna, direccion):
    filas = len(sopa)
    columnas = len(sopa[0])
    longitud = len(palabra)
    
    if direccion == "derecha":
        if columna + longitud > columnas:
            return False
        for i in range(longitud):
            if sopa[fila][columna+i] != palabra[i]:
                return False
    elif direccion == "abajo":
        if fila + longitud > filas:
            return False
        for i in range(longitud):
            if sopa[fila+i][columna] != palabra[i]:
                return False
    elif direccion == "diagonal":
        if fila + longitud > filas or columna + longitud > columnas:
            return False
        for i in range(longitud):
            if sopa[fila+i][columna+i] != palabra[i]:
                return False
    else:
        return False
    
    return True

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    
    for palabra in palabras:
        filas = len(sopa)
        columnas = len(sopa[0])
        longitud = len(palabra)
        
        for i in range(filas):
            for j in range(columnas):
                if buscar_palabra(sopa, palabra, i, j, "derecha"):
                    resultados.append((palabra, [i, j], "derecha"))
                if buscar_palabra(sopa, palabra, i, j, "abajo"):
                    resultados.append((palabra, [i, j], "abajo"))
                if buscar_palabra(sopa, palabra, i, j, "diagonal"):
                    resultados.append((palabra, [i, j], "diagonal"))
    
    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultado = sopaletras(nombre_archivo, palabras)
    print(resultado)
