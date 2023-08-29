def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"
    elif abs(len(palabra1) - len(palabra2)) > 1:
        return "+1"
    elif len(palabra1) == len(palabra2):
        distancia = sum([palabra1[i] != palabra2[i] for i in range(len(palabra1))])
        return "1S" if distancia == 1 else "+1"
    else:
        if len(palabra1) > len(palabra2):
            palabra1, palabra2 = palabra2, palabra1
        i, j, distancia, cambios = 0, 0, 0, 0
        while i < len(palabra1) and j < len(palabra2):
            if palabra1[i] != palabra2[j]:
                cambios += 1
                if cambios > 1:
                    return "+1"
                if len(palabra1) == len(palabra2):
                    i += 1
                j += 1
            else:
                i += 1
                j += 1
        return "IB"
