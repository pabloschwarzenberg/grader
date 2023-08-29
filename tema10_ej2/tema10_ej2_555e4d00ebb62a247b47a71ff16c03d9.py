def levenshtein(word1, word2):
    m = len(word1)
    n = len(word2)

    # Crear una matriz de tamaño (m+1) x (n+1) e inicializarla con ceros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera columna con los valores del 0 al m
    for i in range(m + 1):
        dp[i][0] = i

    # Inicializar la primera fila con los valores del 0 al n
    for j in range(n + 1):
        dp[0][j] = j

    # Calcular el costo mínimo de transformación
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    # Determinar el resultado según la distancia calculada
    distance = dp[m][n]
    if distance > 1:
        return "+1"
    elif distance == 1:
        if m > n:
            return "IB"
        elif m < n:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"

