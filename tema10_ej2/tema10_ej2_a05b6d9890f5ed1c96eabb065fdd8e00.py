def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"
    
    if palabra1 == palabra2:
        return "0D"

    if len1 == len2:
        dif = sum([1 for c1, c2 in zip(palabra1, palabra2) if c1 != c2])
        if dif == 1:
            return "1S"
    
    if len1 < len2:
        palabra1, palabra2 = palabra2, palabra1
        len1, len2 = len2, len1

    i = j = dif = 0
    while i < len1 and j < len2:
        if palabra1[i] != palabra2[j]:
            dif += 1
            if dif > 1:
                return "+1"
            if len1 != len2:
                j -= 1
        i += 1
        j += 1

    return "IB"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    distancia = levenshtein(palabra1, palabra2)
    print("Distancia:", distancia)