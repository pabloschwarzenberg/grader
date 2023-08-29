def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras y obtener las letras del tablero
    with open(nombre_archivo, "r") as archivo:
        tablero = [linea.strip().split() for linea in archivo.readlines()]

    # Obtener las dimensiones del tablero
    filas = len(tablero)
    columnas = len(tablero[0])

    # Lista para almacenar los resultados
    resultados = []

    # Función para verificar si una palabra se encuentra en el tablero en una dirección dada
    def buscar_palabra(palabra, fila_inicio, col_inicio, fila_dir, col_dir):
        # Verificar que la palabra encaje dentro del tablero
        if fila_inicio + fila_dir * (len(palabra) - 1) >= filas or col_inicio + col_dir * (len(palabra) - 1) >= columnas:
            return False

        # Verificar si la palabra coincide en la dirección dada
        for i in range(len(palabra)):
            fila_actual = fila_inicio + fila_dir * i
            col_actual = col_inicio + col_dir * i
            if tablero[fila_actual][col_actual] != palabra[i]:
                return False

        return True

    # Buscar las palabras en el tablero
    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                # Verificar dirección horizontal (derecha)
                if buscar_palabra(palabra, fila, columna, 0, 1):
                    resultados.append((palabra, [fila, columna], "derecha"))

                # Verificar dirección vertical (abajo)
                if buscar_palabra(palabra, fila, columna, 1, 0):
                    resultados.append((palabra, [fila, columna], "abajo"))

                # Verificar dirección diagonal (derecha-abajo)
                if buscar_palabra(palabra, fila, columna, 1, 1):
                    resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]

    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)