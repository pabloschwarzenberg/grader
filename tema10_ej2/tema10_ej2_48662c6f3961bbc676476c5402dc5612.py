def levenshtein(a, b):

    x = len(a)
    y = len(b)

    matriz = [[0] * (y+1) for _ in range(x+1)]

    for i in range(x+1):
        matriz[i][0] = i
    for j in range(y+1):
        matriz[0][j] = j

    for i in range(1, x+1):
        for j in range(1, y+1):
            if a[i-1] == b[j-1]:
                matriz[i][j] = matriz[i-1][j-1]
            else:
                matriz[i][j] = min(matriz[i-1][j], matriz[i][j-1], matriz[i-1][j-1]) + 1

    distancia = matriz[x][y]

    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if x != y:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"