def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_palabra(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    
    for fila in range(n_filas):
        for columna in range(n_columnas):
            
            if columna + len(palabra) <= n_columnas:
                palabra_horizontal = ''.join(sopa[fila][columna:columna+len(palabra)])
                if palabra_horizontal == palabra:
                    return [fila, columna], "derecha"
            
            
            if fila + len(palabra) <= n_filas:
                palabra_vertical = ''.join([sopa[f][columna] for f in range(fila, fila+len(palabra))])
                if palabra_vertical == palabra:
                    return [fila, columna], "abajo"
            
            
            if fila + len(palabra) <= n_filas and columna + len(palabra) <= n_columnas:
                palabra_diagonal = ''.join([sopa[fila+i][columna+i] for i in range(len(palabra))])
                if palabra_diagonal == palabra:
                    return [fila, columna], "diagonal"
    
    return None

def sopaletras():
    nombre_archivo = input("Ingrese el nombre del archivo de la sopa de letras: ")
    palabras = input("Ingrese las palabras a buscar (separadas por comas): ").split(",")
    
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    
    for palabra in palabras:
        palabra = palabra.strip()
        posicion = buscar_palabra(sopa, palabra)
        if posicion is not None:
            resultados.append((palabra, posicion[0], posicion[1]))
    
    return resultados


resultados = sopaletras()
print(resultados)
