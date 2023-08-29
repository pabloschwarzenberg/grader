def levenshtein(word1, word2):
    if word1 == word2:
        return "0D"  # Las palabras son iguales

    m = len(word1)
    n = len(word2)

    if abs(m - n) > 1:
        return "+1"  # La distancia es mayor que 1

    # Creamos una matriz de tamaño (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializamos la primera fila y columna de la matriz
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Llenamos el resto de la matriz utilizando el algoritmo de Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    # Determinamos el tipo de distancia y retornamos el resultado correspondiente
    if dp[m][n] > 1:
        return "+1"  # La distancia es mayor que 1
    elif dp[m][n] == 1:
        if m > n or n > m:
            return "IB"  # Hay que insertar o borrar una letra
        else:
            return "1S"  # Hay que sustituir una letra
