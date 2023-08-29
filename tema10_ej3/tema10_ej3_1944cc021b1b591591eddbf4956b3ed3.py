def sopaletras(nombre_archivo, palabras):
    # Leer el archivo con la sopa de letras
    with open(nombre_archivo, "r") as archivo:
        sopa = [linea.strip().split() for linea in archivo]

    # Inicializar la lista de resultados
    resultados = []

    # Obtener dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        # Buscar horizontalmente
        for fila in range(filas):
            for columna in range(columnas - len(palabra)):
                if "".join(sopa[fila][columna:columna+len(palabra)]) == palabra:
                    resultados.append((palabra, [fila, columna], "derecha"))

        # Buscar verticalmente
        for fila in range(filas - len(palabra)):
            for columna in range(columnas):
                if "".join([sopa[fila+i][columna] for i in range(len(palabra))]) == palabra:
                    resultados.append((palabra, [fila, columna], "abajo"))

        # Buscar diagonalmente (de izquierda a derecha)
        for fila in range(filas - len(palabra)):
            for columna in range(columnas - len(palabra)):
                if "".join([sopa[fila+i][columna+i] for i in range(len(palabra))]) == palabra:
                    resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    palabras = input("Ingrese las palabras separadas por comas: ").split(",")

    resultados = sopaletras(nombre_archivo, palabras)
    print("Resultados:")
    for resultado in resultados:
        print(resultado)