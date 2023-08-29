def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    sopa = [linea.strip().split() for linea in archivo]
    archivo.close()

    resultados = []

    filas = len(sopa)
    columnas = len(sopa[0])

    for palabra in palabras:
        palabra = palabra.lower()
        for i in range(filas):
            for j in range(columnas):
                if sopa[i][j] == palabra[0]:
                    # Verificar horizontalmente hacia la derecha
                    if j + len(palabra) <= columnas and sopa[i][j:j+len(palabra)] == list(palabra):
                        resultados.append((palabra, [i, j], "derecha"))
                    # Verificar verticalmente hacia abajo
                    if i + len(palabra) <= filas and [sopa[k][j] for k in range(i, i+len(palabra))] == list(palabra):
                        resultados.append((palabra, [i, j], "abajo"))
                    # Verificar en diagonal hacia abajo y derecha
                    if i + len(palabra) <= filas and j + len(palabra) <= columnas and [sopa[i+k][j+k] for k in range(len(palabra))] == list(palabra):
                        resultados.append((palabra, [i, j], "diagonal"))
                    # Verificar en diagonal hacia arriba y derecha
                    if i - len(palabra) >= -1 and j + len(palabra) <= columnas and [sopa[i-k][j+k] for k in range(len(palabra))] == list(palabra):
                        resultados.append((palabra, [i, j], "diagonal inversa"))

    return resultados


if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))
