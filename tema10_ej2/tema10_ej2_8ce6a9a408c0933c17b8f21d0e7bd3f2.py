def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    # Crear una matriz para almacenar los cálculos de distancia
    matriz = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Inicializar la primera fila y la primera columna de la matriz
    for i in range(len1 + 1):
        matriz[i][0] = i
    for j in range(len2 + 1):
        matriz[0][j] = j

    # Calcular la distancia Levenshtein
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(matriz[i - 1][j], matriz[i][j - 1], matriz[i - 1][j - 1]) + 1

    distancia = matriz[len1][len2]

    # Determinar el resultado según la distancia calculada
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        return "IB" if len1 < len2 else "1S"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print("El resultado es:", resultado)