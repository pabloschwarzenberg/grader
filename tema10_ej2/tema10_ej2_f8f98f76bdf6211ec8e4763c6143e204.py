def levenshtein(palabra1, palabra2):
    if len(palabra1) == len(palabra2):
        if palabra1 == palabra2:
            return "0D"
        else:
            distancia = sum([1 for i in range(len(palabra1)) if palabra1[i] != palabra2[i]])
            if distancia == 1:
                return "1S"
            elif distancia > 1:
                return "+1"
            else:
                return "0D"
    elif abs(len(palabra1) - len(palabra2)) > 1:
        return "+1"
    else:
        if len(palabra1) < len(palabra2):
            palabra1, palabra2 = palabra2, palabra1
        for i in range(len(palabra2)):
            if palabra1[i] != palabra2[i]:
                if palabra1[i+1:] == palabra2[i:]:
                    return "IB"
                else:
                    return "+1"
        return "IB"
           