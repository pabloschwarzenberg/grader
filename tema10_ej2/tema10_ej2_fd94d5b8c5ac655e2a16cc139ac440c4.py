def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return '0D'  # palabras iguales

    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return '+1'  # distancia mayor que 1

    # Crear una matriz de distancias
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar primera columna y primera fila de la matriz
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

    if dp[m][n] == 1:
        if m == n:
            return '1S'  # sustituir una letra
        else:
            return 'IB'  # insertar o borrar una letra
    else:
        return '+1'  # distancia mayor que 1

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)

           