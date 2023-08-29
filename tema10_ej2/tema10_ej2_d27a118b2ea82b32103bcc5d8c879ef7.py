def levenshtein(word1, word2):
    m = len(word1)
    n = len(word2)

    # Crear una matriz de tamaño (m+1) x (n+1)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna de la matriz
    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j

    # Calcular la distancia Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,  # Eliminación
                    matrix[i][j - 1] + 1,  # Inserción
                    matrix[i - 1][j - 1] + 1  # Sustitución
                )

    distance = matrix[m][n]

    # Determinar el resultado basado en la distancia
    if distance > 1:
        return "+1"
    elif distance == 1:
        if m < n:
            return "IB"
        elif m > n:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"