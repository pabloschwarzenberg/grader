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
            fila = linea.strip().split()
            tablero.append(fila)
    return tablero

def buscar_horizontal(tablero, palabra):
    for i, fila in enumerate(tablero):
        for j in range(len(fila) - len(palabra) + 1):
            if palabra == "".join(fila[j:j+len(palabra)]):
                return [i, j], "derecha"
    return None

def buscar_vertical(tablero, palabra):
    m = len(tablero)
    n = len(tablero[0])
    for i in range(m - len(palabra) + 1):
        for j in range(n):
            if all(palabra[k] == tablero[i+k][j] for k in range(len(palabra))):
                return [i, j], "abajo"
    return None

def buscar_diagonal(tablero, palabra):
    m = len(tablero)
    n = len(tablero[0])
    for i in range(m - len(palabra) + 1):
        for j in range(n - len(palabra) + 1):
            if all(palabra[k] == tablero[i+k][j+k] for k in range(len(palabra))):
                return [i, j], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    tablero = cargar_tablero(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_horizontal(tablero, palabra)
        if not resultado:
            resultado = buscar_vertical(tablero, palabra)
        if not resultado:
            resultado = buscar_diagonal(tablero, palabra)
        resultados.append((palabra, resultado[0], resultado[1]) if resultado else (palabra, [], ""))
    return resultados


if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))
           