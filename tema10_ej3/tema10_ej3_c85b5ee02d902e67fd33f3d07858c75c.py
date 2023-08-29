def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo]
    return sopa

def buscar_palabra(sopa, palabra, fila, columna, direccion):
    num_filas = len(sopa)
    num_columnas = len(sopa[0])
    longitud = len(palabra)

    for i in range(longitud):
        if fila >= num_filas or columna >= num_columnas or sopa[fila][columna] != palabra[i]:
            return False

        if direccion == 'derecha':
            columna += 1
        elif direccion == 'abajo':
            fila += 1
        elif direccion == 'diagonal':
            fila += 1
            columna += 1

    return True

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    num_filas = len(sopa)
    num_columnas = len(sopa[0])

    for palabra in palabras:
        for fila in range(num_filas):
            for columna in range(num_columnas):
                if buscar_palabra(sopa, palabra, fila, columna, 'derecha'):
                    resultados.append((palabra, [fila, columna], 'derecha'))
                if buscar_palabra(sopa, palabra, fila, columna, 'abajo'):
                    resultados.append((palabra, [fila, columna], 'abajo'))
                if buscar_palabra(sopa, palabra, fila, columna, 'diagonal'):
                    resultados.append((palabra, [fila, columna], 'diagonal'))

    return resultados

if __name__ == "__main__":
    archivo_sopa = "sopa.txt"
    palabras_buscar = ["casa"]
    resultados = sopaletras(archivo_sopa, palabras_buscar)
    print(resultados)

   

           