def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"

    if m == n:
        distancia = sum(c1 != c2 for c1, c2 in zip(palabra1, palabra2))
        if distancia == 0:
            return "0D"
        elif distancia == 1:
            return "1S"
        else:
            return "+1"

    if m < n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    i, j = 0, 0
    distancia = 0
    while i < m and j < n:
        if palabra1[i] != palabra2[j]:
            distancia += 1
            if distancia > 1:
                return "+1"
            if m != n:
                j -= 1
        i += 1
        j += 1

    return "IB"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
