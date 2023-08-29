def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  # Las palabras son iguales

    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"  # La distancia es mayor que 1

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
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[i % 2][j - 1], dp[(i - 1) % 2][j - 1]) + 1

    distancia = dp[m % 2][n]

    if distancia == 1:
        if m == n:
            return "1S"  # Hay que sustituir una letra
        else:
            return "IB"  # Hay que insertar o borrar una letra

    return "+1"  # La distancia es mayor que 1

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print("Distancia entre {} y {}: {}".format(palabra1, palabra2, resultado))