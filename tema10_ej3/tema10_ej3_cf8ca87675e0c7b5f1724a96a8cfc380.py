def cargar_tablero(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
    
    tablero = [linea.strip().split() for linea in lineas]
    return tablero

def buscar_palabra(tablero, palabra, direccion):
    n = len(tablero)
    m = len(tablero[0])
    palabra = palabra.upper()
    
    if direccion == "derecha":
        for i in range(n):
            fila = "".join(tablero[i])
            if palabra in fila:
                columna = fila.index(palabra)
                return [i, columna]
    
    if direccion == "abajo":
        for j in range(m):
            columna = "".join(tablero[i][j] for i in range(n))
            if palabra in columna:
                fila = columna.index(palabra)
                return [fila, j]
    
    if direccion == "diagonal":
        for i in range(n):
            for j in range(m):
                diagonal = ""
                k = 0
                while i + k < n and j + k < m:
                    diagonal += tablero[i + k][j + k]
                    if palabra in diagonal:
                        indice = diagonal.index(palabra)
                        return [i + indice, j + indice]
                    k += 1
    
    return None

def sopaletras(nombre_archivo, palabras):
    tablero = cargar_tablero(nombre_archivo)
    resultados = []
    
    for palabra in palabras:
        palabra = palabra.upper()
        encontrado = False
        
        for direccion in ["derecha", "abajo", "diagonal"]:
            posicion = buscar_palabra(tablero, palabra, direccion)
            if posicion is not None:
                resultados.append((palabra.lower(), posicion, direccion))
                encontrado = True
                break
        
        if not encontrado:
            resultados.append((palabra.lower(), None, None))
    
    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "cra", "aro"]
    resultados = sopaletras(nombre_archivo, palabras)
    
    for resultado in resultados:
        print(resultado)
