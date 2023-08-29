def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, "r") as archivo:
        tablero = []
        for linea in archivo:
            tablero.append(linea.strip().split())


    filas = len(tablero)
    columnas = len(tablero[0])
    resultados = []


    for palabra in palabras:
        encontrada = False
        for fila in range(filas):
            for col in range(columnas - len(palabra) + 1):
                if tablero[fila][col:col + len(palabra)] == list(palabra):
                    resultados.append((palabra, [fila, col], "derecha"))
                    encontrada = True
                    break
            if encontrada:
                break

        if not encontrada:
            for fila in range(filas - len(palabra) + 1):
                for col in range(columnas):
                    if [tablero[fila + i][col] for i in range(len(palabra))] == list(palabra):
                        resultados.append((palabra, [fila, col], "abajo"))
                        encontrada = True
                        break
                if encontrada:
                    break

        if not encontrada:
            for fila in range(filas - len(palabra) + 1):
                for col in range(columnas - len(palabra) + 1):
                    if [tablero[fila + i][col + i] for i in range(len(palabra))] == list(palabra):
                        resultados.append((palabra, [fila, col], "diagonal"))
                        encontrada = True
                        break
                if encontrada:
                    break

    return resultados

if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["CRA"]))
    print(sopaletras("sopa.txt", ["ARO"]))
    print(sopaletras("sopa.txt", ["CASA"]))
    print(sopaletras("sopa.txt", ["CASA", "CRA", "ARO"]))
  