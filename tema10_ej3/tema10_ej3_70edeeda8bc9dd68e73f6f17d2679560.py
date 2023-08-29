def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(line.rstrip()) for line in archivo.readlines()]

    resultados = []

    for palabra in palabras:
        encontrada = False
        for fila in range(len(sopa)):
            for col in range(len(sopa[fila])):
                if buscar_derecha(sopa, fila, col, palabra):
                    resultados.append((palabra, [fila, col], "derecha"))
                    encontrada = True
                elif buscar_abajo(sopa, fila, col, palabra):
                    resultados.append((palabra, [fila, col], "abajo"))
                    encontrada = True
                elif buscar_diagonal(sopa, fila, col, palabra):
                    resultados.append((palabra, [fila, col], "diagonal"))
                    encontrada = True

                if encontrada:
                    break
            if encontrada:
                break

    return resultados


def buscar_derecha(sopa, fila, col, palabra):
    if col + len(palabra) > len(sopa[fila]):
        return False
    for i in range(len(palabra)):
        if sopa[fila][col + i] != palabra[i]:
            return False
    return True


def buscar_abajo(sopa, fila, col, palabra):
    if fila + len(palabra) > len(sopa):
        return False
    for i in range(len(palabra)):
        if sopa[fila + i][col] != palabra[i]:
            return False
    return True


def buscar_diagonal(sopa, fila, col, palabra):
    if fila + len(palabra) > len(sopa) or col + len(palabra) > len(sopa[fila]):
        return False
    for i in range(len(palabra)):
        if sopa[fila + i][col + i] != palabra[i]:
            return False
    return True


if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    print(sopaletras(nombre_archivo, palabras))
