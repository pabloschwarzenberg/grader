def levenshtein(word1, word2):
    m, n = len(word1), len(word2)

    # Creamos una matriz de (m+1) x (n+1) e inicializamos la primera fila y columna
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calculamos la distancia de Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    # Determinamos el tipo de distancia y retornamos el resultado correspondiente
    distance = dp[m][n]
    if distance > 1:
        return "+1"
    elif distance == 1:
        if m > n:
            return "IB"  # Insertar o borrar una letra
        elif m < n:
            return "IB"  # Insertar o borrar una letra
        else:
            return "1S"  # Sustituir una letra
    else:
        return "0D"  # Palabras iguales


if __name__ == "__main__":
    word1 = input("Ingresa la primera palabra: ")
    word2 = input("Ingresa la segunda palabra: ")

    result = levenshtein(word1, word2)
    print(result)