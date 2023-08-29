def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"

    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"
    elif len1 == len2:
        diff = sum(a != b for a, b in zip(palabra1, palabra2))
        if diff == 1:
            return "1S"
        else:
            return "+1"
    elif len1 > len2:
        if palabra1.startswith(palabra2):
            return "IB"
        else:
            return "+1"
    else:
        if palabra2.startswith(palabra1):
            return "IB"
        else:
            return "+1"
