def buscar_palabra_horizontal(sopa, palabra):
    for i in range(len(sopa)):
        for j in range(len(sopa[0]) - len(palabra) + 1):
            if sopa[i][j:j + len(palabra)] == palabra:
                return [i, j], "derecha"
    return None

def buscar_palabra_vertical(sopa, palabra):
    for i in range(len(sopa) - len(palabra) + 1):
        for j in range(len(sopa[0])):
            coincidencia = True
            for k in range(len(palabra)):
                if sopa[i + k][j] != palabra[k]:
                    coincidencia = False
                    break
            if coincidencia:
                return [i, j], "abajo"
    return None

def buscar_palabra_diagonal(sopa, palabra):
    for i in range(len(sopa) - len(palabra) + 1):
        for j in range(len(sopa[0]) - len(palabra) + 1):
            coincidencia = True
            for k in range(len(palabra)):
                if sopa[i + k][j + k] != palabra[k]:
                    coincidencia = False
                    break
            if coincidencia:
                return [i, j], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    sopa = [list(linea.strip()) for linea in archivo.readlines()]
    archivo.close()

    resultados = []
    for palabra in palabras:
        resultado = buscar_palabra_horizontal(sopa, palabra)
        if resultado is None:
            resultado = buscar_palabra_vertical(sopa, palabra)
        if resultado is None:
            resultado = buscar_palabra_diagonal(sopa, palabra)
        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))

    return resultados

if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))
           