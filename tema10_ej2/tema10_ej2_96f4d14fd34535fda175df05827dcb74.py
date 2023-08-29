def levenshtein(word1, word2):
    m = len(word1)
    n = len(word2)

    # Crear una matriz de distancias
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Llenar la primera fila y columna
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calcular las distancias
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    # Determinar el tipo de distancia
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

# Ejemplo de uso
if __name__ == "__main__":
    word1 = "gato"
    word2 = "gatito"
    result = levenshtein(word1, word2)
    print(result)  # Debe imprimir "+1"
