def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y obtener la sopa de letras como una lista de listas
    with open(nombre_archivo, "r") as file:
        sopa = [list(line.strip()) for line in file.readlines()]

    # Obtener las dimensiones del tablero
    filas = len(sopa)
    columnas = len(sopa[0])

    # Lista para almacenar los resultados
    resultados = []

    # Recorrer cada palabra en la lista de palabras
    for palabra in palabras:
        # Buscar la palabra en la sopa de letras en todas las direcciones
        for i in range(filas):
            for j in range(columnas):
                # Buscar en forma horizontal (de izquierda a derecha)
                if j + len(palabra) <= columnas:
                    if all(sopa[i][j+k] == palabra[k] for k in range(len(palabra))):
                        resultados.append((palabra, [i, j], "derecha"))

                # Buscar en forma vertical (de arriba a abajo)
                if i + len(palabra) <= filas:
                    if all(sopa[i+k][j] == palabra[k] for k in range(len(palabra))):
                        resultados.append((palabra, [i, j], "abajo"))

                # Buscar en forma diagonal (de esquina superior izquierda a esquina inferior derecha)
                if i + len(palabra) <= filas and j + len(palabra) <= columnas:
                    if all(sopa[i+k][j+k] == palabra[k] for k in range(len(palabra))):
                        resultados.append((palabra, [i, j], "diagonal"))

    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)



           