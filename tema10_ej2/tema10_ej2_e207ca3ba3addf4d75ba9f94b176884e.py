def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  # Las palabras son iguales

    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"  # La distancia es mayor que 1

    # Inicializar matriz de distancias
    distancias = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Llenar primera fila y primera columna
    for i in range(len1 + 1):
        distancias[i][0] = i
    for j in range(len2 + 1):
        distancias[0][j] = j

    # Calcular distancias
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancias[i][j] = distancias[i - 1][j - 1]
            else:
                distancias[i][j] = min(distancias[i - 1][j], distancias[i][j - 1], distancias[i - 1][j - 1]) + 1

    # Determinar el tipo de distancia
    if distancias[len1][len2] > 1:
        return "+1"  # La distancia es mayor que 1
    elif distancias[len1][len2] == 1:
        if len1 == len2:
            return "1S"  # Hay que sustituir una letra
        else:
            return "IB"  # Hay que insertar o borrar una letra

    return "0D"  # Las palabras son iguales
