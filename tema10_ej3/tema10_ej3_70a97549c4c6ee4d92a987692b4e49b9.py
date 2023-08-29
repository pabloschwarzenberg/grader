def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [linea.strip().split() for linea in archivo]
    return sopa

def buscar_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for i in range(n_filas):
        fila = ''.join(sopa[i])
        if palabra in fila:
            columna = fila.index(palabra)
            return [i, columna]
    return None

def buscar_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for j in range(n_columnas):
        columna = ''.join([sopa[i][j] for i in range(n_filas)])
        if palabra in columna:
            fila = columna.index(palabra)
            return [fila, j]
    return None

def buscar_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for i in range(n_filas):
        for j in range(n_columnas):
            # Diagonal principal de esquina superior izquierda a esquina inferior derecha
            diagonal = ''.join([sopa[i+k][j+k] for k in range(min(n_filas-i, n_columnas-j))])
            if palabra in diagonal:
                index = diagonal.index(palabra)
                return [i+index, j+index, "diagonal"]
            # Diagonal inversa de esquina superior izquierda a esquina inferior derecha
            diagonal_inversa = ''.join([sopa[i+k][j-k] for k in range(min(n_filas-i, j+1))])
            if palabra in diagonal_inversa:
                index = diagonal_inversa.index(palabra)
                return [i+index, j-index, "diagonal"]
    return None



def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = None
        resultado = buscar_horizontal(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado, "derecha"))
            continue
        resultado = buscar_vertical(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado, "abajo"))
            continue
        resultado = buscar_diagonal(sopa, palabra)
        if resultado:
            resultados.append((palabra, resultado, "diagonal"))
    return resultados

if __name__ == "__main__":
    archivo_sopa = "sopa.txt"
    palabras_a_buscar = ["casa"]
    resultados = sopaletras(archivo_sopa, palabras_a_buscar)
    print(resultados)
