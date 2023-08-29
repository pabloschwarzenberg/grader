def levenshtein(word1, word2):
    if word1 == word2:
        return "0D"

    m, n = len(word1), len(word2)

    if abs(m - n) > 1:
        return "+1"

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

    if dp[m][n] > 1:
        return "+1"
    elif dp[m][n] == 1:
        if m < n:
            return "IB"
        else:
            return "1S"
    elif m == n:
        return "0D"
    elif m < n:
        return "IB"
    else:
        return "IB"

# Ejemplos de uso
print(levenshtein("gato", "gatito"))  # +1
print(levenshtein("hola", "ola"))  # IB
print(levenshtein("gallina", "gallina"))  # 0D
print(levenshtein("caro", "cara"))  # 1S
print(levenshtein("Limon", "limon"))  # 1S
print(levenshtein("jaron", "jarron"))  # IB