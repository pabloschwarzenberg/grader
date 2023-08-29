def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"

    if m == n:
        if palabra1 == palabra2:
            return "0D"
        else:
            distancia = sum(1 for i in range(m) if palabra1[i] != palabra2[i])
            if distancia == 1:
                return "1S"
            else:
                return "+1"

    if m < n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    i = 0
    j = 0
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

    if distancia == 1:
        return "IB"
    else:
        return "+1"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print("La distancia entre las palabras es:", resultado)

           