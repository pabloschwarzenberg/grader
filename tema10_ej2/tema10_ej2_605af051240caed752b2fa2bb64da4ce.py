def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    if dp[m][n] > 1:
        return "+1"
    elif dp[m][n] == 1:
        if m == n:
            return "1S"
        else:
            return "IB"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    print(levenshtein(palabra1, palabra2))  # +1

    palabra1 = "hola"
    palabra2 = "ola"
    print(levenshtein(palabra1, palabra2))  # 1S

    palabra1 = "gallina"
    palabra2 = "gallina"
    print(levenshtein(palabra1, palabra2))  # 0D

    palabra1 = "caro"
    palabra2 = "cara"
    print(levenshtein(palabra1, palabra2))  # 1S
