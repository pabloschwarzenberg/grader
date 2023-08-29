def levenshtein(word1, word2):
    m = len(word1)
    n = len(word2)
    
    # Crear una matriz de distancias con tamaño (m+1) x (n+1)
    distances = [[0] * (n+1) for _ in range(m+1)]
    
    # Inicializar la primera fila y la primera columna de la matriz
    for i in range(m+1):
        distances[i][0] = i
    for j in range(n+1):
        distances[0][j] = j
    
    # Calcular las distancias mínimas utilizando el algoritmo de Levenshtein
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                distances[i][j] = min(distances[i-1][j-1], distances[i][j-1], distances[i-1][j]) + 1
    
    # Determinar el tipo de distancia y retornar el string correspondiente
    if distances[m][n] > 1:
        return "+1"
    elif distances[m][n] == 1:
        if m > n or m < n:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"