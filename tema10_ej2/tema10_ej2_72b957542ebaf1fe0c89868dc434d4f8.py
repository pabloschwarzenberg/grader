def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    if len1 == len2:
        distancia = sum(a != b for a, b in zip(palabra1, palabra2))
        if distancia == 0:
            return "0D"
        elif distancia == 1:
            return "1S"
        else:
            return "+1"
    elif abs(len1 - len2) == 1:
        if len1 < len2:
            if palabra2.startswith(palabra1):
                return "IB"
            else:
                return "+1"
        else:
            if palabra1.startswith(palabra2):
                return "IB"
            else:
                return "+1"
    else:
        return "+1"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
