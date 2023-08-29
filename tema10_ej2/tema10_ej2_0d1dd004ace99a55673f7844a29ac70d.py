def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Matriz de distancias
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calcular las distancias
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    # Calcular el resultado según las especificaciones
    distancia = dp[m][n]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m > n:
            return "IB"
        elif m < n:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)  # Debe imprimir "+1"

    palabra1 = "hola"
    palabra2 = "ola"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)  # Debe imprimir "1S"

    palabra1 = "gallina"
    palabra2 = "gallina"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)  # Debe imprimir "0D"
