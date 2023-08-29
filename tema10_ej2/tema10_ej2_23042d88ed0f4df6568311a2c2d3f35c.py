def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"
    
    if palabra1 == palabra2:
        return "0D"
    
    if m < n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m
    
    matriz = [[0] * (n + 1) for _ in range(2)]

    for j in range(n + 1):
        matriz[0][j] = j

    for i in range(1, m + 1):
        matriz[1][0] = i
        for j in range(1, n + 1):
            costo = 0 if palabra1[i - 1] == palabra2[j - 1] else 1
            matriz[1][j] = min(matriz[0][j] + 1, matriz[1][j - 1] + 1, matriz[0][j - 1] + costo)
        matriz[0] = matriz[1][:]

    distancia = matriz[1][n]

    if distancia > 1:
        return "+1"
    elif distancia == 1:
        return "IB" if m < n else "1S"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)
