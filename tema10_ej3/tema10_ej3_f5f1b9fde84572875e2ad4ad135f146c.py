def buscar_horizontal(tablero, palabra):
    n = len(tablero)
    m = len(tablero[0])
    for i in range(n):
        for j in range(m - len(palabra) + 1):
            if tablero[i][j:j+len(palabra)] == palabra:
                return [i, j], "derecha"
    return None

def buscar_vertical(tablero, palabra):
    n = len(tablero)
    m = len(tablero[0])
    for i in range(n - len(palabra) + 1):
        for j in range(m):
            columna = [tablero[i+k][j] for k in range(len(palabra))]
            if columna == palabra:
                return [i, j], "abajo"
    return None

def buscar_diagonal(tablero, palabra):
    n = len(tablero)
    m = len(tablero[0])
    for i in range(n - len(palabra) + 1):
        for j in range(m - len(palabra) + 1):
            diagonal = [tablero[i+k][j+k] for k in range(len(palabra))]
            if diagonal == palabra:
                return [i, j], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, "r") as archivo:
        tablero = [list(linea.strip()) for linea in archivo]
    
    resultados = []
    for palabra in palabras:
        palabra = list(palabra)
        resultado = buscar_horizontal(tablero, palabra)
        if resultado:
            resultados.append((''.join(palabra), resultado[0], resultado[1]))
            continue
        
        resultado = buscar_vertical(tablero, palabra)
        if resultado:
            resultados.append((''.join(palabra), resultado[0], resultado[1]))
            continue
        
        resultado = buscar_diagonal(tablero, palabra)
        if resultado:
            resultados.append((''.join(palabra), resultado[0], resultado[1]))
    
    return resultados

if __name__ == "__main__":
    nombre_archivo = input("Ingresa el nombre del archivo de la sopa de letras: ")
    palabras = input("Ingresa las palabras a buscar, separadas por comas: ").split(",")
    
    resultados = sopaletras(nombre_archivo, palabras)
    for resultado in resultados:
        print(resultado)



           