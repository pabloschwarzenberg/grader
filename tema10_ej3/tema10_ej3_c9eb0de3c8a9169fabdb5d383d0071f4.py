def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa


def buscar_palabra(sopa, palabra, fila, columna, df, dc):
    for letra in palabra:
        if fila < 0 or fila >= len(sopa) or columna < 0 or columna >= len(sopa[0]) or sopa[fila][columna] != letra:
            return False
        fila += df
        columna += dc
    return True


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    direcciones = [(0, 1), (1, 0), (1, 1)]
    resultados = []

    for palabra in palabras:
        for fila in range(len(sopa)):
            for columna in range(len(sopa[0])):
                for df, dc in direcciones:
                    if buscar_palabra(sopa, palabra, fila, columna, df, dc):
                        direccion = "derecha" if df == 0 and dc == 1 else "abajo" if df == 1 and dc == 0 else "diagonal"
                        resultados.append((palabra, [fila, columna], direccion))

    return resultados


if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de la sopa de letras: ")
    palabras = input("Ingrese las palabras a buscar (separadas por comas): ").split(",")

    resultados = sopaletras(nombre_archivo, palabras)
    for resultado in resultados:
        print(resultado)