def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"

    if m > n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    dp = [[0] * (n + 1) for _ in range(2)]

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        dp[i % 2][0] = i
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
            else:
                dp[i % 2][j] = 1 + min(dp[(i - 1) % 2][j], dp[i % 2][j - 1], dp[(i - 1) % 2][j - 1])

    distancia = dp[m % 2][n]

    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m == n:
            return "1S"
        else:
            return "IB"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)