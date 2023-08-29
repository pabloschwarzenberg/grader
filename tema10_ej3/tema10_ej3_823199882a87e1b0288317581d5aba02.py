def buscar_horizontal(tablero, palabra):
    for i in range(len(tablero)):
        fila = "".join(tablero[i])
        if palabra in fila:
            columna = fila.index(palabra)
            return [i, columna], "derecha"
    return None

def buscar_vertical(tablero, palabra):
    for j in range(len(tablero[0])):
        columna = [tablero[i][j] for i in range(len(tablero))]
        columna = "".join(columna)
        if palabra in columna:
            fila = columna.index(palabra)
            return [fila, j], "abajo"
    return None

def buscar_diagonal(tablero, palabra):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            diagonal = ""
            k = 0
            while i + k < len(tablero) and j + k < len(tablero[0]):
                diagonal += tablero[i + k][j + k]
                if palabra in diagonal:
                    indice = diagonal.index(palabra)
                    return [i + indice, j + indice], "diagonal"
                k += 1
    return None

def sopaletras(nombre_archivo, palabras):
    tablero = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            tablero.append(fila)    

    resultados = []
    for palabra in palabras:
        resultado = None
        resultado = buscar_horizontal(tablero, palabra.upper())
        if resultado is None:
            resultado = buscar_vertical(tablero, palabra.upper())
        if resultado is None:
            resultado = buscar_diagonal(tablero, palabra.upper())
        resultados.append((palabra, resultado[0], resultado[1]) if resultado else (palabra, [], ""))

    return resultados

if __name__ == "__main__":
    archivo = input("Ingrese el nombre del archivo: ")
    palabras = input("Ingrese las palabras separadas por comas: ").split(",")
    resultado = sopaletras(archivo, palabras)
    print("Resultados:")
    for res in resultado:
        print(res)

           
