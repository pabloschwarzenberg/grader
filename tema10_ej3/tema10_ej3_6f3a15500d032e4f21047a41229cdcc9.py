def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))
    def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y obtener el tablero de la sopa de letras
    with open(nombre_archivo, "r") as archivo:
        tablero = [list(linea.strip()) for linea in archivo.readlines()]

    n_filas = len(tablero)
    n_columnas = len(tablero[0])

    resultados = []

    for palabra in palabras:
        # Buscar la palabra en forma horizontal
        for i in range(n_filas):
            for j in range(n_columnas - len(palabra) + 1):
                if tablero[i][j:j + len(palabra)] == list(palabra):
                    resultados.append((palabra, [i, j], "derecha"))

        # Buscar la palabra en forma vertical
        for i in range(n_filas - len(palabra) + 1):
            for j in range(n_columnas):
                columna = [tablero[k][j] for k in range(i, i + len(palabra))]
                if columna == list(palabra):
                    resultados.append((palabra, [i, j], "abajo"))

        # Buscar la palabra en forma diagonal (esquina superior izquierda a esquina inferior derecha)
        for i in range(n_filas - len(palabra) + 1):
            for j in range(n_columnas - len(palabra) + 1):
                diagonal = [tablero[i + k][j + k] for k in range(len(palabra))]
                if diagonal == list(palabra):
                    resultados.append((palabra, [i, j], "diagonal"))

    return resultados

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    palabras = input("Ingrese las palabras separadas por comas: ").split(",")
    resultado = sopaletras(nombre_archivo, palabras)
    print("Resultado:", resultado)

           