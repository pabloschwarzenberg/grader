def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y obtener la sopa de letras
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)

    # Obtener dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    # Lista para almacenar los resultados
    resultados = []

    # Función para verificar si una palabra se encuentra en la sopa de letras en una dirección específica
    def buscar_palabra(palabra, fila, columna, direccion):
        longitud = len(palabra)

        # Verificar límites según la dirección
        if direccion == 'derecha' and columna + longitud > columnas:
            return False
        elif direccion == 'abajo' and fila + longitud > filas:
            return False
        elif direccion == 'diagonal' and (fila + longitud > filas or columna + longitud > columnas):
            return False

        # Verificar si la palabra coincide en la dirección específica
        for i in range(longitud):
            if direccion == 'derecha' and sopa[fila][columna + i] != palabra[i]:
                return False
            elif direccion == 'abajo' and sopa[fila + i][columna] != palabra[i]:
                return False
            elif direccion == 'diagonal' and sopa[fila + i][columna + i] != palabra[i]:
                return False

        return True

    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        palabra_encontrada = False

        # Buscar en forma horizontal (de izquierda a derecha)
        for i in range(filas):
            for j in range(columnas):
                if buscar_palabra(palabra, i, j, 'derecha'):
                    resultados.append((palabra, [i, j], 'derecha'))
                    palabra_encontrada = True
                    break
            if palabra_encontrada:
                break

        # Buscar en forma vertical (de arriba a abajo)
        if not palabra_encontrada:
            for i in range(filas):
                for j in range(columnas):
                    if buscar_palabra(palabra, i, j, 'abajo'):
                        resultados.append((palabra, [i, j], 'abajo'))
                        palabra_encontrada = True
                        break
                if palabra_encontrada:
                    break

        # Buscar en forma diagonal (de esquina superior izquierda a esquina inferior derecha)
        if not palabra_encontrada:
            for i in range(filas):
                for j in range(columnas):
                    if buscar_palabra(palabra, i, j, 'diagonal'):
                        resultados.append((palabra, [i, j], 'diagonal'))
                        palabra_encontrada = True
                        break
                if palabra_encontrada:
                    break

    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultado = sopaletras(nombre_archivo, palabras)
    print(resultado)
