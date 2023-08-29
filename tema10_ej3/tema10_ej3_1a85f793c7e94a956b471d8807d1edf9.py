def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras y almacenar las letras en una matriz
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo]

    # Definir las direcciones posibles: derecha, abajo, diagonal (derecha abajo)
    direcciones = [(1, 0), (0, 1), (1, 1)]

    # Obtener dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    # Función para verificar si una palabra se puede formar desde una posición en una dirección
    def verificar_palabra(palabra, fila, columna, direccion):
        for letra in palabra:
            # Verificar si la posición está dentro de los límites de la matriz
            if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
                return False

            # Verificar si la letra coincide con la posición actual en la matriz
            if sopa[fila][columna] != letra:
                return False

            # Moverse a la siguiente posición en la dirección especificada
            fila += direccion[0]
            columna += direccion[1]

        return True

    # Lista para almacenar las palabras encontradas
    palabras_encontradas = []

    # Buscar cada palabra en la sopa de letras
    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                for direccion in direcciones:
                    # Verificar si la palabra se puede formar desde la posición actual en la dirección especificada
                    if verificar_palabra(palabra, fila, columna, direccion):
                        # Almacenar la palabra encontrada junto con su posición inicial y dirección
                        palabras_encontradas.append((palabra, [fila, columna], direccion))

    return palabras_encontradas

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)
