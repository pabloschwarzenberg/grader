def leer_sopa(nombre_archivo):
    matriz = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            matriz.append(fila)
    return matriz

def buscar_horizontal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for i in range(filas):
        fila = sopa[i]
        fila_str = ''.join(fila)
        if palabra in fila_str:
            columna = fila_str.index(palabra)
            return [i, columna]
    return None

def buscar_vertical(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for j in range(columnas):
        columna = [sopa[i][j] for i in range(filas)]
        columna_str = ''.join(columna)
        if palabra in columna_str:
            fila = columna_str.index(palabra)
            return [fila, j]
    return None

def buscar_diagonal(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    for i in range(filas):
        for j in range(columnas):
            if i + len(palabra) <= filas and j + len(palabra) <= columnas:
                diagonal = [sopa[i+k][j+k] for k in range(len(palabra))]
                diagonal_str = ''.join(diagonal)
                if palabra == diagonal_str:
                    return [i, j]
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = leer_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        fila_columna = buscar_horizontal(sopa, palabra)
        if fila_columna is None:
            fila_columna = buscar_vertical(sopa, palabra)
            if fila_columna is None:
                fila_columna = buscar_diagonal(sopa, palabra)
                if fila_columna is not None:
                    resultados.append((palabra, fila_columna, 'diagonal'))
        else:
            resultados.append((palabra, fila_columna, 'derecha'))
    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)