def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)
    
    # Caso base: Si alguna de las palabras es una cadena vacía, la distancia es la longitud de la otra palabra
    if m == 0:
        return str(n)
    if n == 0:
        return str(m)
    
    # Crear una matriz para almacenar los subproblemas de distancia
    matriz_distancia = [[0] * (n+1) for _ in range(m+1)]
    
    # Llenar la primera fila y la primera columna de la matriz
    for i in range(m+1):
        matriz_distancia[i][0] = i
    for j in range(n+1):
        matriz_distancia[0][j] = j
    
    # Calcular la distancia de Levenshtein para los subproblemas
    for i in range(1, m+1):
        for j in range(1, n+1):
            if palabra1[i-1] == palabra2[j-1]:
                matriz_distancia[i][j] = matriz_distancia[i-1][j-1]
            else:
                matriz_distancia[i][j] = min(matriz_distancia[i-1][j-1], matriz_distancia[i][j-1], matriz_distancia[i-1][j]) + 1
    
    # Obtener la distancia final entre las palabras
    distancia = matriz_distancia[m][n]
    
    # Determinar el resultado según las especificaciones
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m > n:
            return "IB"  # Insertar o borrar una letra
        else:
            return "1S"  # Sustituir una letra
    else:
        return "0D"  # Palabras iguales

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)
