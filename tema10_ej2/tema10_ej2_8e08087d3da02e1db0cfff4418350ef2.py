def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"
    elif palabra1 == palabra2:
        return "0D"

    if m > n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    distancia = [[0] * (n + 1) for _ in range(2)]

    for j in range(n + 1):
        distancia[0][j] = j

    for i in range(1, m + 1):
        distancia[1][0] = i
        for j in range(1, n + 1):
            costo = int(palabra1[i - 1] != palabra2[j - 1])
            distancia[1][j] = min(distancia[0][j] + 1, distancia[1][j - 1] + 1, distancia[0][j - 1] + costo)
        distancia[0] = distancia[1][:]

    if distancia[1][n] > 1:
        return "+1"
    elif distancia[1][n] == 1:
        return "IB" if m < n else "1S"

    return "0D"