def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_palabra(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    direccion = ""
    
    # Buscar palabra horizontalmente
    for fila in range(filas):
        for col in range(columnas - len(palabra) + 1):
            if sopa[fila][col:col+len(palabra)] == palabra:
                return [fila, col], "derecha"
    
    # Buscar palabra verticalmente
    for fila in range(filas - len(palabra) + 1):
        for col in range(columnas):
            columna = [sopa[f][col] for f in range(fila, fila+len(palabra))]
            if "".join(columna) == palabra:
                return [fila, col], "abajo"
    
    # Buscar palabra en diagonal hacia abajo y derecha
    for fila in range(filas - len(palabra) + 1):
        for col in range(columnas - len(palabra) + 1):
            diagonal = [sopa[fila+i][col+i] for i in range(len(palabra))]
            if "".join(diagonal) == palabra:
                return [fila, col], "diagonal"
    
    return None, None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    
    for palabra in palabras:
        inicio, direccion = buscar_palabra(sopa, palabra)
        resultados.append((palabra, inicio, direccion))
    
    return resultados

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de la sopa de letras: ")
    palabras = input("Ingrese las palabras a buscar en la sopa de letras (separadas por espacios): ").split()
    resultados = sopaletras(nombre_archivo, palabras)
    
    print("Resultados:")
    for resultado in resultados:
        palabra, inicio, direccion = resultado
        print(palabra, inicio, direccion)
