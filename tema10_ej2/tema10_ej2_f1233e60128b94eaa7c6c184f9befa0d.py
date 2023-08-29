def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"
    
    if palabra1 == palabra2:
        return "0D"

    if m < n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    dp = [[0] * (n + 1) for _ in range(2)]

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        dp[1][0] = i
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                dp[1][j] = dp[0][j - 1]
            else:
                dp[1][j] = 1 + min(dp[0][j], dp[1][j - 1], dp[0][j - 1])
        dp[0] = dp[1][:]

    if dp[1][n] > 1:
        return "+1"
    elif dp[1][n] == 1:
        return "IB" if m < n else "1S"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
           