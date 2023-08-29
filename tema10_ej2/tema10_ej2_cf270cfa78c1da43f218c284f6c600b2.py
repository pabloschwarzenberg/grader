def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"
    elif palabra1 == palabra2:
        return "0D"
    elif m == 0 or n == 0:
        return "IB" if m == 0 else "IB"
    else:
        matriz = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            matriz[i][0] = i

        for j in range(n + 1):
            matriz[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if palabra1[i - 1] == palabra2[j - 1]:
                    matriz[i][j] = matriz[i - 1][j - 1]
                else:
                    matriz[i][j] = 1 + min(matriz[i - 1][j - 1], matriz[i - 1][j], matriz[i][j - 1])

        if matriz[m][n] > 1:
            return "+1"
        elif matriz[m][n] == 1:
            return "IB" if m > n else "IB"
        else:
            return "1S"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)
           