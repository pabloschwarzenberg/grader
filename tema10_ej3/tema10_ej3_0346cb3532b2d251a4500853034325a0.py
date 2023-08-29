def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo]

    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    resultados = []

    def buscar_palabra(palabra, inicio_fila, inicio_columna, delta_fila, delta_columna):
        longitud = len(palabra)
        fin_fila = inicio_fila + (longitud - 1) * delta_fila
        fin_columna = inicio_columna + (longitud - 1) * delta_columna

        if fin_fila >= 0 and fin_fila < n_filas and fin_columna >= 0 and fin_columna < n_columnas:
            for i in range(longitud):
                fila = inicio_fila + i * delta_fila
                columna = inicio_columna + i * delta_columna
                if sopa[fila][columna] != palabra[i]:
                    return False
            return True
        else:
            return False

    for palabra in palabras:
        for fila in range(n_filas):
            for columna in range(n_columnas):
                if buscar_palabra(palabra, fila, columna, 0, 1):
                    resultados.append((palabra, [fila, columna], "derecha"))
                if buscar_palabra(palabra, fila, columna, 1, 0):
                    resultados.append((palabra, [fila, columna], "abajo"))
                if buscar_palabra(palabra, fila, columna, 1, 1):
                    resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados

if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))