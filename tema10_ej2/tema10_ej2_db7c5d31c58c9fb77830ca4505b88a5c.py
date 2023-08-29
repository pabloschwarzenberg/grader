def levenshtein(word1, word2):
    len1, len2 = len(word1), len(word2)

    # Crear una matriz de distancia con una fila y columna adicional para los casos base
    distances = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Inicializar la primera fila y columna con valores crecientes
    for i in range(len1 + 1):
        distances[i][0] = i
    for j in range(len2 + 1):
        distances[0][j] = j

    # Calcular la distancia de edición entre las subcadenas
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i - 1] == word2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                substitute_cost = distances[i - 1][j - 1] + 1
                insert_cost = distances[i][j - 1] + 1
                delete_cost = distances[i - 1][j] + 1
                distances[i][j] = min(substitute_cost, insert_cost, delete_cost)

    # Determinar la categoría correspondiente según la distancia de edición
    distance = distances[len1][len2]
    if distance > 1:
        return "+1"
    elif distance == 1:
        if len1 > len2:
            return "IB"
        elif len1 < len2:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"
