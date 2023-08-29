def levenshtein(word1, word2):
    m = len(word1)
    n = len(word2)

    # Caso base: una de las palabras es vacía
    if m == 0 or n == 0:
        return "IB" if abs(m - n) == 1 else "+1"

    # Creamos una matriz para almacenar los resultados intermedios
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializamos la primera fila y la primera columna
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Llenamos la matriz utilizando programación dinámica
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    # Calculamos la distancia de Levenshtein entre las dos palabras
    distance = dp[m][n]

    # Devolvemos el resultado según las especificaciones
    if distance > 1:
        return "+1"
    elif distance == 1:
        return "IB" if m < n else "1S"
    else:
        return "0D"


if __name__ == "__main__":
    word1 = input("Ingrese la primera palabra: ")
    word2 = input("Ingrese la segunda palabra: ")

    result = levenshtein(word1, word2)
    print(result)
