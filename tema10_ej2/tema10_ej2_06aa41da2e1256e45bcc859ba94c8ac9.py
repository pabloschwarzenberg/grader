def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"

    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"

    if len1 == len2:
        diff_count = sum([1 for c1, c2 in zip(palabra1, palabra2) if c1 != c2])
        if diff_count == 1:
            return "1S"

    if len1 > len2:
        palabra1, palabra2 = palabra2, palabra1
        len1, len2 = len2, len1

    i = 0
    j = 0
    diff_count = 0

    while i < len1 and j < len2:
        if palabra1[i] != palabra2[j]:
            diff_count += 1
            if diff_count > 1:
                return "+1"
            if len1 < len2:
                i -= 1
        i += 1
        j += 1

    return "IB"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
 