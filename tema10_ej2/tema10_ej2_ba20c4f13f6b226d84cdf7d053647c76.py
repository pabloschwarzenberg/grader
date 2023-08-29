def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear una matriz de distancias
    distancia = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera columna
    for i in range(m + 1):
        distancia[i][0] = i

    # Inicializar la primera fila
    for j in range(n + 1):
        distancia[0][j] = j

    # Calcular las distancias
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]
            else:
                distancia[i][j] = min(distancia[i - 1][j - 1], distancia[i][j - 1], distancia[i - 1][j]) + 1

    # Determinar el tipo de distancia
    if distancia[m][n] > 1:
        return "+1"
    elif distancia[m][n] == 1:
        if m < n:
            return "IB"
        elif m > n:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado) 

#

def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]


    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))
def sopaletras(nombre_archivo, palabras):

    matriz = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            matriz.append(fila)
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    resultados = []
    

    def buscar_palabra(palabra, fila_inicial, col_inicial, dir_fila, dir_col):
        fila_actual = fila_inicial
        col_actual = col_inicial
        
        for letra in palabra:
            if fila_actual < 0 or fila_actual >= filas or col_actual < 0 or col_actual >= columnas or matriz[fila_actual][col_actual].lower() != letra:
                return False
            fila_actual += dir_fila
            col_actual += dir_col
        
        return True
    

    def determinar_direccion(fila_inicial, col_inicial, fila_final, col_final):
        if fila_inicial == fila_final:
            return "derecha"
        elif col_inicial == col_final:
            return "abajo"
        else:
            return "diagonal"
    

    for palabra in palabras:
        palabra = palabra.lower()  
        
        for fila in range(filas):
            for col in range(columnas):
                if buscar_palabra(palabra, fila, col, 0, 1): 
                    direccion = determinar_direccion(fila, col, fila, col+len(palabra)-1)
                    resultados.append((palabra, [fila, col], direccion))
                
                if buscar_palabra(palabra, fila, col, 1, 0):  
                    direccion = determinar_direccion(fila, col, fila+len(palabra)-1, col)
                    resultados.append((palabra, [fila, col], direccion))
                
                if buscar_palabra(palabra, fila, col, 1, 1):  
                    direccion = determinar_direccion(fila, col, fila+len(palabra)-1, col+len(palabra)-1)
                    resultados.append((palabra, [fila, col], direccion))
    
    return resultados



    resultado = sopaletras("sopa.txt", ["casa", "cra", "aro"])