def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for fila in range(n_filas):
        for columna in range(n_columnas - len(palabra) + 1):
            if sopa[fila][columna:columna + len(palabra)] == palabra:
                return fila, columna
    return None

def buscar_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas):
            if all(sopa[fila + i][columna] == palabra[i] for i in range(len(palabra))):
                return fila, columna
    return None

def buscar_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas - len(palabra) + 1):
            if all(sopa[fila + i][columna + i] == palabra[i] for i in range(len(palabra))):
                return fila, columna
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = []
        resultado.append(palabra)
        
        fila_columna = buscar_horizontal(sopa, palabra)
        if fila_columna is not None:
            resultado.append(fila_columna)
            resultado.append("derecha")
            resultados.append(tuple(resultado))
            continue
        
        fila_columna = buscar_vertical(sopa, palabra)
        if fila_columna is not None:
            resultado.append(fila_columna)
            resultado.append("abajo")
            resultados.append(tuple(resultado))
            continue
        
        fila_columna = buscar_diagonal(sopa, palabra)
        if fila_columna is not None:
            resultado.append(fila_columna)
            resultado.append("diagonal")
            resultados.append(tuple(resultado))
            continue
    
    return resultados

if __name__ == "__main__":
    archivo_sopa = "sopa.txt"
    palabras_buscar = ["casa"]
    resultado = sopaletras(archivo_sopa, palabras_buscar)
    print(resultado)
