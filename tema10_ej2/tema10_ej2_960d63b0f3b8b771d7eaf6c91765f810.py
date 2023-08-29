def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear una matriz de distancias
    distancias = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y columna de la matriz
    for i in range(m + 1):
        distancias[i][0] = i
    for j in range(n + 1):
        distancias[0][j] = j

    # Calcular las distancias para cada posición
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancias[i][j] = distancias[i - 1][j - 1]
            else:
                distancias[i][j] = min(distancias[i - 1][j] + 1, distancias[i][j - 1] + 1, distancias[i - 1][j - 1] + 1)

    # Obtener la distancia entre las palabras
    distancia = distancias[m][n]

    # Determinar el string de retorno según la distancia
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m > n:
            return "IB"  # Insertar o borrar una letra
        else:
            return "1S"  # Sustituir una letra
    elif distancia == 0:
        return "0D"  # Palabras iguales

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print("Distancia Levenshtein:", resultado)
