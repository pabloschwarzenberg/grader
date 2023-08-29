def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)
    
    # Crear la matriz de distancia con (m+1) filas y (n+1) columnas
    distancia = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Inicializar la primera fila y la primera columna de la matriz
    for i in range(m + 1):
        distancia[i][0] = i
    for j in range(n + 1):
        distancia[0][j] = j
    
    # Calcular la distancia de edición entre las palabras
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]
            else:
                distancia[i][j] = min(distancia[i - 1][j], distancia[i][j - 1], distancia[i - 1][j - 1]) + 1
    
    # Determinar el resultado según la distancia
    if distancia[m][n] > 1:
        return "+1"
    elif distancia[m][n] == 1:
        if m != n:
            return "IB"  # Insertar o borrar una letra
        else:
            return "1S"  # Sustituir una letra
    else:
        return "0D"  # Palabras iguales

# Ejemplo de uso
print(levenshtein("jaron", "jarron"))


           