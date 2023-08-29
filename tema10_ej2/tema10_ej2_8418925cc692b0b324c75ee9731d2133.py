def levenshtein (palabra1,palabra2):
    if palabra1 == palabra2:
        return "0D"
    elif len(palabra1) == len(palabra2):
        n_reemplazar = 0
        for i in range(len(palabra1)):
            if palabra1[i] != palabra2[i]:
                n_reemplazar += 1
        if n_reemplazar > 1:
            return "+1"
        else:
            return "1S"
    elif abs(len(palabra1) - len(palabra2)) == 1:
        if len(palabra1) > len(palabra2):
            for i in range(len(palabra1)):
                if palabra1[:i] + palabra1[i+1:] == palabra2:
                    return "IB"
            return "+1"
        else:
            for i in range(len(palabra2)):
                if palabra2[:i] + palabra2[i+1:] == palabra1:
                    return "IB"
            return "+1"
    else:
        return "+1"
           