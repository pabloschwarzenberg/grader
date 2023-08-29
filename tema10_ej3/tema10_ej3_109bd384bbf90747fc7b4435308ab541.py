def cargar_sopa_de_letras(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_horizontal(sopa, palabra):
    for i in range(len(sopa)):
        fila = "".join(sopa[i])
        if palabra in fila:
            columna_inicial = fila.index(palabra)
            return [i, columna_inicial]
    return None

def buscar_vertical(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for j in range(columnas):
        columna = "".join([sopa[i][j] for i in range(filas)])
        if palabra in columna:
            fila_inicial = columna.index(palabra)
            return [fila_inicial, j]
    return None

def buscar_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for i in range(filas):
        for j in range(columnas):
            k = 0
            while i + k < filas and j + k < columnas:
                if sopa[i + k][j + k] != palabra[k]:
                    break
                k += 1
                if k == len(palabra):
                    return [i, j]
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa_de_letras(nombre_archivo)
    resultados = []
    for palabra in palabras:
        inicio_horizontal = buscar_horizontal(sopa, palabra)
        inicio_vertical = buscar_vertical(sopa, palabra)
        inicio_diagonal = buscar_diagonal(sopa, palabra)
        if inicio_horizontal:
            resultados.append((palabra, inicio_horizontal, "derecha"))
        if inicio_vertical:
            resultados.append((palabra, inicio_vertical, "abajo"))
        if inicio_diagonal:
            resultados.append((palabra, inicio_diagonal, "diagonal"))
    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "cra", "aro"]
    resultados = sopaletras(nombre_archivo, palabras)
    print("Resultados:")
    for resultado in resultados:
        palabra, posicion, direccion = resultado
        print(palabra, posicion, direccion)