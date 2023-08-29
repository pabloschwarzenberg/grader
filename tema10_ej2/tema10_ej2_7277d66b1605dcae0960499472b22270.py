def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"

    if m == n:
        distancia = sum(palabra1[i] != palabra2[i] for i in range(m))
        if distancia == 0:
            return "0D"
        elif distancia == 1:
            return "1S"
        else:
            return "+1"

    if m > n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    dp = [i for i in range(m + 1)]
    for j in range(1, n + 1):
        prev = dp[0]
        dp[0] = j
        for i in range(1, m + 1):
            temp = dp[i]
            if palabra1[i - 1] == palabra2[j - 1]:
                dp[i] = prev
            else:
                dp[i] = min(prev + 1, dp[i] + 1, dp[i - 1] + 1)
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
    print(resultado)
