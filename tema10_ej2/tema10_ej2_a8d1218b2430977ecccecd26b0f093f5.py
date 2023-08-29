def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"

    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"

    if m > n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

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
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    distancia = dp[m][n]

    if distancia > 1:
        return "+1"
    elif distancia == 1:
        return "IB" if m != n else "1S"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
