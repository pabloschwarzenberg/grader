def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    # Crear matriz de distancias
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Inicializar primera fila y primera columna
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    # Calcular distancias
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    # Determinar resultado
    distancia = dp[len1][len2]

    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if len1 > len2:
            return "IB"
        elif len2 > len1:
            return "IB"
        else:
            return "1S"
    elif distancia == 0:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)

           