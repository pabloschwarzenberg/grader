def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y obtener la sopa de letras
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split(',')
            sopa.append(fila)

    # Obtener las dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    resultados = []

    # Función para verificar si una palabra aparece en una dirección específica
    def buscar_palabra(palabra, fila_inicial, columna_inicial, delta_fila, delta_columna):
        fila = fila_inicial
        columna = columna_inicial
        for letra in palabra:
            if fila < 0 or fila >= filas or columna < 0 or columna >= columnas or sopa[fila][columna] != letra:
                return False
            fila += delta_fila
            columna += delta_columna
        return True

    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        palabra_encontrada = False

        # Buscar horizontalmente
        for fila in range(filas):
            for columna in range(columnas - len(palabra) + 1):
                if buscar_palabra(palabra, fila, columna, 0, 1):
                    resultados.append((palabra, [fila, columna], "derecha"))
                    palabra_encontrada = True

        # Buscar verticalmente
        for fila in range(filas - len(palabra) + 1):
            for columna in range(columnas):
                if buscar_palabra(palabra, fila, columna, 1, 0):
                    resultados.append((palabra, [fila, columna], "abajo"))
                    palabra_encontrada = True

        # Buscar en diagonal (esquina superior izquierda a esquina inferior derecha)
        for fila in range(filas - len(palabra) + 1):
            for columna in range(columnas - len(palabra) + 1):
                if buscar_palabra(palabra, fila, columna, 1, 1):
                    resultados.append((palabra, [fila, columna], "diagonal"))
                    palabra_encontrada = True

        if not palabra_encontrada:
            resultados.append((palabra, None, "No encontrada"))

    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)
