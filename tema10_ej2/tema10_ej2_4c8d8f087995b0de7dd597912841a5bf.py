def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"

    if palabra1 == palabra2:
        return "0D"

    if len1 == len2:
        distancia = sum(p1 != p2 for p1, p2 in zip(palabra1, palabra2))
        if distancia == 1:
            return "1S"

    distancia = 0
    i = 0
    j = 0

    while i < len1 and j < len2:
        if palabra1[i] != palabra2[j]:
            distancia += 1
            if distancia > 1:
                return "+1"
            if len1 < len2:
                i -= 1
            elif len1 > len2:
                j -= 1
        i += 1
        j += 1

    if distancia == 1:
        return "IB"
    else:
        return "+1"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)
