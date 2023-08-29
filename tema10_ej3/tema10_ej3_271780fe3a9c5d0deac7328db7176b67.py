def sopaletras(nombre_archivo, palabras):
    matriz = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            matriz.append(fila)

    filas = len(matriz)
    columnas = len(matriz[0])

    resultados = []

    def buscar_palabra(palabra, fila_inicial, columna_inicial, direccion_fila, direccion_columna):
        fila_actual = fila_inicial
        columna_actual = columna_inicial

        for letra in palabra:
            if fila_actual < 0 or fila_actual >= filas or columna_actual < 0 or columna_actual >= columnas or matriz[fila_actual][columna_actual].lower() != letra:
                return False
            fila_actual += direccion_fila
            columna_actual += direccion_columna

        return True

    def determinar_direccion(fila_inicial, columna_inicial, fila_final, columna_final):
        if fila_inicial == fila_final:
            return "derecha"
        elif columna_inicial == columna_final:
            return "abajo"
        else:
            return "diagonal"

    for palabra in palabras:
        palabra = palabra.lower()  
        for fila in range(filas):
            for col in range(columnas):
                if buscar_palabra(palabra, fila, col, 0, 1):  
                    direccion = determinar_direccion(fila, col, fila, col + len(palabra) - 1)
                    resultados.append((palabra, [fila, col], direccion))

                if buscar_palabra(palabra, fila, col, 1, 0):  
                    direccion = determinar_direccion(fila, col, fila + len(palabra) - 1, col)
                    resultados.append((palabra, [fila, col], direccion))

                if buscar_palabra(palabra, fila, col, 1, 1):  
                    direccion = determinar_direccion(fila, col, fila + len(palabra) - 1, col + len(palabra) - 1)
                    resultados.append((palabra, [fila, col], direccion))

    return resultados

if __name__ == "__main__":
    resultado = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultado)