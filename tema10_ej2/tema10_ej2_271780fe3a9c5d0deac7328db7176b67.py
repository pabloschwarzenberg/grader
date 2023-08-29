def levenshtein(palabra1, palabra2):
    k = len(palabra1)
    n = len(palabra2)

    matriz = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(k + 1):
        matriz[i][0] = i
    for j in range(n + 1):
        matriz[0][j] = j

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(matriz[i - 1][j], matriz[i][j - 1], matriz[i - 1][j - 1]) + 1

    distancia = matriz[k][n]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if k > n:
            return "IB"
        elif k < n:
            return "IB"
        else:
            return "1S"
    elif distancia == 0:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la  palabra 1: ")
    palabra2 = input("Ingrese la  palabra 2: ")

    resultado = levenshtein(palabra1, palabra2)
    print(resultado)