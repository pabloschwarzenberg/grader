def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2: return "0D"
    elif len(palabra1) == 0: return len(palabra2)
    elif len(palabra2) == 0: return len(palabra1)
    v0 = [None] * (len(palabra2) + 1)
    v1 = [None] * (len(palabra2) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(palabra1)):
        v1[0] = i + 1
        for j in range(len(palabra2)):
            cost = 0 if palabra1[i] == palabra2[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]
    if v1[len(palabra2)] > 1: return "+1"
    if v1[len(palabra2)] == 1 and cost != 0: return "1S"
    if v1[len(palabra2)] == 1 and cost == 0: return "IB"
    return v1[len(palabra2)]    