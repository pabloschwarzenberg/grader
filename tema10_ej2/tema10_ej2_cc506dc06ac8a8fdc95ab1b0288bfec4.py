def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"

    if palabra1 == palabra2:
        return "0D"

    if len1 == len2:
        count = sum(palabra1[i] != palabra2[i] for i in range(len1))
        if count == 1:
            return "1S"
        else:
            return "+1"

    if len1 > len2:
        palabra1, palabra2 = palabra2, palabra1
        len1, len2 = len2, len1

    i = 0
    count = 0
    while i < len1:
        if palabra1[i] != palabra2[i + count]:
            count += 1
            if count > 1:
                return "+1"
        else:
            i += 1

    return "IB"


if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
