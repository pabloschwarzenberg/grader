def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, "r") as file:
        tablero = [line.strip().split() for line in file.readlines()]

    # Obtener las dimensiones del tablero
    filas = len(tablero)
    columnas = len(tablero[0])

    # Definir las direcciones en las que se buscarán las palabras
    direcciones = {
        "derecha": (0, 1),
        "abajo": (1, 0),
        "diagonal": (1, 1)
    }

    encontradas = []

    # Función para verificar si una palabra está en el tablero en una dirección específica
    def buscar_palabra(palabra, fila, columna, direccion):
        delta_fila, delta_columna = direccion
        len_palabra = len(palabra)

        # Calcular las coordenadas finales según la dirección
        fin_fila = fila + (len_palabra - 1) * delta_fila
        fin_columna = columna + (len_palabra - 1) * delta_columna

        # Verificar si las coordenadas finales están dentro de los límites del tablero
        if fin_fila >= 0 and fin_fila < filas and fin_columna >= 0 and fin_columna < columnas:
            # Verificar si la palabra está presente en el tablero en la dirección dada
            letras = [tablero[fila + i * delta_fila][columna + i * delta_columna] for i in range(len_palabra)]
            if "".join(letras) == palabra:
                return True

        return False

    # Recorrer el tablero en busca de las palabras en las direcciones
    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                for direccion, delta in direcciones.items():
                    if buscar_palabra(palabra, fila, columna, delta):
                        encontradas.append((palabra, [fila, columna], direccion))

    return encontradas

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "cra", "aro"]
    resultado = sopaletras(nombre_archivo, palabras)
    print(resultado)