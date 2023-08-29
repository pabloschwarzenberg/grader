def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"
    elif palabra1 == palabra2:
        return "0D"
    elif m == n:
        distancia = sum(p1 != p2 for p1, p2 in zip(palabra1, palabra2))
        if distancia == 1:
            return "1S"
    elif m < n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    distancia = [[0] * (n + 1) for _ in range(2)]

    for j in range(n + 1):
        distancia[0][j] = j

    for i in range(1, m + 1):
        distancia[1][0] = i
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[1][j] = distancia[0][j - 1]
            else:
                distancia[1][j] = 1 + min(distancia[0][j - 1], distancia[1][j - 1], distancia[0][j])
        distancia[0] = distancia[1][:]

    if distancia[1][n] == 1:
        return "IB"
    else:
        return "+1"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
