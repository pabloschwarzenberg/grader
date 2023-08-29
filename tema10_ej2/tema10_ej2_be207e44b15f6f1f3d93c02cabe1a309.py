def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"

    if abs(len(palabra1) - len(palabra2)) > 1:
        return "+1"

    for i in range(min(len(palabra1), len(palabra2))):
        if palabra1[i] != palabra2[i]:
            if len(palabra1) == len(palabra2):
                return "1S"
            elif i == 0 and palabra1[i+1:] == palabra2[i:]:
                return "IB"
            elif i == len(palabra1)-1 and palabra1[:i] == palabra2[:i]:
                return "IB"
            else:
                return "+1"

    return "1S" if len(palabra1) != len(palabra2) else "0D"
