def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear una matriz de distancias con (m+1) filas y (n+1) columnas
    matriz = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna de la matriz
    for i in range(m + 1):
        matriz[i][0] = i
    for j in range(n + 1):
        matriz[0][j] = j

    # Calcular la distancia de Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(matriz[i - 1][j], matriz[i][j - 1], matriz[i - 1][j - 1]) + 1

    # Determinar el resultado según la distancia calculada
    distancia = matriz[m][n]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        return "IB" if m > n else "1S"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)

    palabra1 = "hola"
    palabra2 = "ola"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)

    palabra1 = "gallina"
    palabra2 = "gallina"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)

    palabra1 = "caro"
    palabra2 = "cara"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)