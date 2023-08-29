def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)
    distancias = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(len1 + 1):
        distancias[i][0] = i
    for j in range(len2 + 1):
        distancias[0][j] = j
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancias[i][j] = distancias[i - 1][j - 1]
            else:
                distancias[i][j] = min(distancias[i - 1][j] + 1, distancias[i][j - 1] + 1, distancias[i - 1][j - 1] + 1)
    distancia = distancias[len1][len2]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if len1 < len2:
            return "IB"
        elif len1 > len2:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"
