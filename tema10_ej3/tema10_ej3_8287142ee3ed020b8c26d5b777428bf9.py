def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras y construir el tablero
    with open(nombre_archivo, "r") as file:
        tablero = [list(line.strip()) for line in file]

    # Obtener dimensiones del tablero
    filas = len(tablero)
    columnas = len(tablero[0])

    # Definir las direcciones para buscar las palabras
    direcciones = {
        'derecha': (0, 1),
        'abajo': (1, 0),
        'diagonal': (1, 1) }

    # Función auxiliar para verificar si una palabra está dentro de los límites del tablero
    def dentro_limites(fila, columna):
        return 0 <= fila < filas and 0 <= columna < columnas

    # Función auxiliar para buscar una palabra en una dirección específica
    def buscar_palabra(palabra, fila, columna, direccion):
        direccion_fila, direccion_columna = direccion
        longitud_palabra = len(palabra)

        # Calcular la posición final de la palabra en la dirección dada
        fila_final = fila + (longitud_palabra - 1) * direccion_fila
        columna_final = columna + (longitud_palabra - 1) * direccion_columna

        # Verificar si la palabra está dentro de los límites del tablero
        if not dentro_limites(fila_final, columna_final):
            return False

        # Verificar si la palabra coincide en la dirección dada
        for i in range(longitud_palabra):
            fila_actual = fila + i * direccion_fila
            columna_actual = columna + i * direccion_columna
            if tablero[fila_actual][columna_actual] != palabra[i]:
                return False

        return True

    resultados = []

    # Buscar cada palabra en el tablero en todas las direcciones posibles
    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                for direccion, (direccion_fila, direccion_columna) in direcciones.items():
                    if buscar_palabra(palabra, fila, columna, (direccion_fila, direccion_columna)):
                        resultados.append((palabra, [fila, columna], direccion))

    return resultados

if __name__ == "__main__":
    resultado = sopaletras('sopa.txt', ['casa'])
    for palabra, posicion, direccion in resultado:
        print(f:{"Palabra: {palabra}, Posición: {posicion}, Dirección: {direccion}"})
