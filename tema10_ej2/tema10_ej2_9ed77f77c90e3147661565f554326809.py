def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"
    elif palabra1 == palabra2:
        return "0D"
    elif len1 == len2:
        distancia = sum(a != b for a, b in zip(palabra1, palabra2))
        if distancia == 1:
            return "1S"
    else:
        if len1 > len2:
            palabra1, palabra2 = palabra2, palabra1
            len1, len2 = len2, len1

        for i in range(len1):
            if palabra1[i] != palabra2[i]:
                if palabra1[i:] == palabra2[i+1:]:
                    return "IB"
                else:
                    return "+1"

        return "IB"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
