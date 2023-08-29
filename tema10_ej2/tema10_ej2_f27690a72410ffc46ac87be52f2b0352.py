def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    # Crear una matriz de distancias
    matriz = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Inicializar la primera fila y columna de la matriz
    for i in range(len1 + 1):
        matriz[i][0] = i
    for j in range(len2 + 1):
        matriz[0][j] = j

    # Calcular la distancia de Levenshtein
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(matriz[i - 1][j - 1], matriz[i][j - 1], matriz[i - 1][j]) + 1

    # Determinar el resultado según la distancia de Levenshtein
    distancia = matriz[len1][len2]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if len1 > len2:
            return "IB"
        else:
            return "IB" if len1 < len2 else "1S"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = "jaron"
    palabra2 = "jarron"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
