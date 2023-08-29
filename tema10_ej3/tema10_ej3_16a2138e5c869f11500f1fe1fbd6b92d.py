def cargar_sopa(nombre_archivo):
    matriz = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            matriz.append(fila)
    return matriz

def buscar_palabra_horizontal(matriz, palabra):
    for fila in matriz:
        fila_str = "".join(fila)
        if palabra in fila_str:
            columna_inicio = fila_str.index(palabra)
            return [matriz.index(fila), columna_inicio]
    return None

def buscar_palabra_vertical(matriz, palabra):
    for columna in range(len(matriz[0])):
        columna_str = "".join([fila[columna] for fila in matriz])
        if palabra in columna_str:
            fila_inicio = columna_str.index(palabra)
            return [fila_inicio, columna]
    return None

def buscar_palabra_diagonal(matriz, palabra):
    n_filas = len(matriz)
    n_columnas = len(matriz[0])
    for i in range(n_filas):
        for j in range(n_columnas):
            diagonal = ""
            fila = i
            columna = j
            while fila < n_filas and columna < n_columnas:
                diagonal += matriz[fila][columna]
                fila += 1
                columna += 1
            if palabra in diagonal:
                inicio = diagonal.index(palabra)
                return [i + inicio, j + inicio]
    return None

def sopaletras(nombre_archivo, palabras):
    matriz = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        inicio_horizontal = buscar_palabra_horizontal(matriz, palabra)
        if inicio_horizontal is not None:
            resultados.append((palabra, inicio_horizontal, "derecha"))
            continue
        
        inicio_vertical = buscar_palabra_vertical(matriz, palabra)
        if inicio_vertical is not None:
            resultados.append((palabra, inicio_vertical, "abajo"))
            continue
        
        inicio_diagonal = buscar_palabra_diagonal(matriz, palabra)
        if inicio_diagonal is not None:
            resultados.append((palabra, inicio_diagonal, "diagonal"))
            continue
    
    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)

    print(resultados)
