def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"
    elif len(palabra1) == len(palabra2):
        distancia = sum(1 for c1, c2 in zip(palabra1, palabra2) if c1 != c2)
        if distancia == 1:
            return "1S"
    elif abs(len(palabra1) - len(palabra2)) == 1:
        if len(palabra1) < len(palabra2):
            palabra1, palabra2 = palabra2, palabra1
        for i in range(len(palabra2)):
            if palabra1[i] != palabra2[i]:
                if palabra1[:i] + palabra1[i+1:] == palabra2:
                    return "IB"
                else:
                    break
        else:
            return "IB"
    return "+1"
