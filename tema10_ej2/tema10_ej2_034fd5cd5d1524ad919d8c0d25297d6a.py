def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"

    if m == n:
        distancia = sum(p1 != p2 for p1, p2 in zip(palabra1, palabra2))
        if distancia == 0:
            return "0D"
        elif distancia == 1:
            return "1S"
        else:
            return "+1"

    if m > n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    dp = list(range(m + 1))
    for i in range(1, n + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            temp = dp[j]
            if palabra1[j - 1] == palabra2[i - 1]:
                dp[j] = prev
            else:
                dp[j] = min(dp[j - 1], dp[j], prev) + 1
            prev = temp

    distancia = dp[m]

    if distancia == 0:
        return "0D"
    elif distancia == 1:
        return "IB"
    else:
        return "+1"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)