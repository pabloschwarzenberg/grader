def levenshtein(palabra1, palabra2):
    rows = len(palabra1)
    cols = len(palabra2)

    d = []
    for _ in range(rows + 1):
        d.append([0] * (cols + 1))

    for i in range(rows + 1):
        d[i][0] = i

    for i in range(cols + 1):
        d[0][i] = i

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])

    if d[rows][cols] > 1:
        return "+1"
    if d[rows][cols] == 0:
        return "0D"
    if len(palabra1) == len(palabra2):
        return "1S"

    return "IB"

levenshtein("jarron", "melon")