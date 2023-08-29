def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    sopa = [list(line.strip().lower()) for line in archivo]
    archivo.close()

    resultados = []
    filas = len(sopa)
    columnas = len(sopa[0])

    for palabra in palabras:
        for i in range(filas):
            for j in range(columnas):
                # Verificar si la palabra aparece en forma horizontal (derecha)
                if j + len(palabra) <= columnas and sopa[i][j:j+len(palabra)] == list(palabra):
                    resultados.append((palabra, [i, j], "derecha"))

                # Verificar si la palabra aparece en forma vertical (abajo)
                if i + len(palabra) <= filas and [sopa[k][j] for k in range(i, i+len(palabra))] == list(palabra):
                    resultados.append((palabra, [i, j], "abajo"))

                # Verificar si la palabra aparece en forma diagonal (derecha y abajo)
                if i + len(palabra) <= filas and j + len(palabra) <= columnas:
                    diagonal = [sopa[i+k][j+k] for k in range(len(palabra))]
                    if diagonal == list(palabra):
                        resultados.append((palabra, [i, j], "diagonal"))

    return resultados

if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))