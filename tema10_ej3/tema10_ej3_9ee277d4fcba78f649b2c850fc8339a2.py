def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_palabra_horizontal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    palabra_invertida = palabra[::-1]

    for i in range(filas):
        fila = ''.join(sopa[i])
        if palabra in fila or palabra_invertida in fila:
            columna_inicio = fila.index(palabra) if palabra in fila else fila.index(palabra_invertida)
            direccion = "derecha" if palabra in fila else "izquierda"
            return [i, columna_inicio], direccion

    return None

def buscar_palabra_vertical(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    palabra_invertida = palabra[::-1]

    for j in range(columnas):
        columna = ''.join([sopa[i][j] for i in range(filas)])
        if palabra in columna or palabra_invertida in columna:
            fila_inicio = columna.index(palabra) if palabra in columna else columna.index(palabra_invertida)
            direccion = "abajo" if palabra in columna else "arriba"
            return [fila_inicio, j], direccion

    return None

def buscar_palabra_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    diagonal_principal = ''
    diagonal_secundaria = ''
    palabra_invertida = palabra[::-1]

    for i in range(filas):
        for j in range(columnas):
            if i == j:
                diagonal_principal += sopa[i][j]
            if i + j == filas - 1:
                diagonal_secundaria += sopa[i][j]

    if palabra in diagonal_principal or palabra_invertida in diagonal_principal:
        inicio = diagonal_principal.index(palabra) if palabra in diagonal_principal else diagonal_principal.index(palabra_invertida)
        direccion = "diagonal"
        return [inicio, inicio], direccion

    if palabra in diagonal_secundaria or palabra_invertida in diagonal_secundaria:
        inicio = diagonal_secundaria.index(palabra) if palabra in diagonal_secundaria else diagonal_secundaria.index(palabra_invertida)
        direccion = "diagonal"
        return [inicio, filas - 1 - inicio], direccion

    return None

def buscar_palabra(sopa, palabra):
    resultado_horizontal = buscar_palabra_horizontal(sopa, palabra)
    resultado_vertical = buscar_palabra_vertical(sopa, palabra)
    resultado_diagonal = buscar_palabra_diagonal(sopa, palabra)

    if resultado_horizontal:
        return resultado_horizontal
    elif resultado_vertical:
        return resultado_vertical
    elif resultado_diagonal:
        return resultado_diagonal
    else:
        return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        resultado = buscar_palabra(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado[0], resultado[1]))

    return resultados

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de la sopa de letras: ")
    palabras = input("Ingrese las palabras a
