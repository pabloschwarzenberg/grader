def buscH(sopa, palabra, fila, columna):
    if columna + len(palabra) <= len(sopa[fila]):
        for i in range(len(palabra)):
            if sopa[fila][columna+i].lower() != palabra[i]:
                return False
        return True
    return False

def buscV(sopa, palabra, fila, columna):
    if fila + len(palabra) <= len(sopa):
        for i in range(len(palabra)):
            if sopa[fila+i][columna].lower() != palabra[i]:
                return False
        return True
    return False

def buscD(sopa, palabra, fila, columna):
    if fila + len(palabra) <= len(sopa) and columna + len(palabra) <= len(sopa[fila]):
        for i in range(len(palabra)):
            if sopa[fila+i][columna+i].lower() != palabra[i]:
                return False
        return True
    return False

def sopaletras(nombre_archivo, palabras):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)

    resultados = []
    for palabra in palabras:
        for fila in range(len(sopa)):
            for columna in range(len(sopa[fila])):
                if buscH(sopa, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "derecha"))
                elif buscV(sopa, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "abajo"))
                elif buscD(sopa, palabra, fila, columna):
                    resultados.append((palabra, [fila, columna], "diagonal"))

    return resultados

if __name__ == "__main__":
    resultado = sopaletras("sopa.txt", ["casa","cra","aro"])
    print(resultado)

           