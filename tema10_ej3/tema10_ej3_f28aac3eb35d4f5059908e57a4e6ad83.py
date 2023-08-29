def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    sopa = [list(linea.strip()) for linea in archivo]
    archivo.close()

    filas = len(sopa)
    columnas = len(sopa[0])

    direcciones = {
        "derecha": (0, 1),
        "abajo": (1, 0),
        "diagonal": (1, 1)
    }

    resultados = []

    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                for direccion, (dx, dy) in direcciones.items():
                    fin_fila = fila + (len(palabra) - 1) * dx
                    fin_columna = columna + (len(palabra) - 1) * dy

                    if fin_fila < 0 or fin_fila >= filas or fin_columna < 0 or fin_columna >= columnas:
                        continue

                    encontrada = True

                    for i in range(len(palabra)):
                        nueva_fila = fila + i * dx
                        nueva_columna = columna + i * dy

                        if sopa[nueva_fila][nueva_columna] != palabra[i]:
                            encontrada = False
                            break

                    if encontrada:
                        resultados.append((palabra, [fila, columna], direccion))

    return resultados

if __name__ == "__main__":
    archivo = "sopa.txt"
    palabras = ["casa", "cra", "aro"]
    resultados = sopaletras(archivo, palabras)
    print(resultados)          