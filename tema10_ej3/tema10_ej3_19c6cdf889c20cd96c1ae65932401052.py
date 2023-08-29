def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

def cargar_tablero(nombre_archivo):
    tablero = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split(",")
            tablero.append(fila)
    return tablero

def buscar_horizontal(tablero, palabra):
    for i in range(len(tablero)):
        fila = "".join(tablero[i])
        if palabra in fila:
            columna = fila.index(palabra)
            return i, columna
    return None

def buscar_vertical(tablero, palabra):
    filas = len(tablero)
    columnas = len(tablero[0])
    for j in range(columnas):
        columna = "".join(tablero[i][j] for i in range(filas))
        if palabra in columna:
            fila = columna.index(palabra)
            return fila, j
    return None

def buscar_diagonal(tablero, palabra):
    filas = len(tablero)
    columnas = len(tablero[0])
    for i in range(filas):
        for j in range(columnas):
            diagonal = []
            k, l = i, j
            while k < filas and l < columnas:
                diagonal.append(tablero[k][l])
                k += 1
                l += 1
            diagonal_str = "".join(diagonal)
            if palabra in diagonal_str:
                fila = diagonal_str.index(palabra) + i
                columna = diagonal_str.index(palabra) + j
                return fila, columna
    return None

def sopaletras(nombre_archivo, palabras):
    tablero = cargar_tablero(nombre_archivo)
    resultados = []

    for palabra in palabras:
        resultado = {}
        resultado["palabra"] = palabra

        # Buscar en dirección horizontal
        pos_horizontal = buscar_horizontal(tablero, palabra)
        if pos_horizontal:
            resultado["posicion"] = list(pos_horizontal)
            resultado["direccion"] = "derecha"
            resultados.append(resultado)
            continue

        # Buscar en dirección vertical
        pos_vertical = buscar_vertical(tablero, palabra)
        if pos_vertical:
            resultado["posicion"] = list(pos_vertical)
            resultado["direccion"] = "abajo"
            resultados.append(resultado)
            continue

        # Buscar en dirección diagonal
        pos_diagonal = buscar_diagonal(tablero, palabra)
        if pos_diagonal:
            resultado["posicion"] = list(pos_diagonal)
            resultado["direccion"] = "diagonal"
            resultados.append(resultado)
            continue

    return resultados


if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    for resultado in resultados:
        print(resultado)
        
#FIN