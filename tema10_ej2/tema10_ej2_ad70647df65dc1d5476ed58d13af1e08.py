def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"
    
    if m == n:
        if palabra1 == palabra2:
            return "0D"
        else:
            distancia = sum(1 for a, b in zip(palabra1, palabra2) if a != b)
            if distancia == 1:
                return "1S"
            else:
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
            cost = 0 if palabra1[i - 1] == palabra2[j - 1] else 1
            dp[i % 2][j] = min(dp[(i - 1) % 2][j] + 1, dp[i % 2][j - 1] + 1, dp[(i - 1) % 2][j - 1] + cost)

    distancia = dp[m % 2][n]
    if distancia == 1:
        return "IB"
    else:
        return "+1"



if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)  # Salida: +1

    palabra1 = "hola"
    palabra2 = "ola"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)  # Salida: 1S

    palabra1 = "gallina"
    palabra2 = "gallina"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)  # Salida: 0D

    palabra1 = "caro"
    palabra2 = "cara"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)  # Salida: 1S
