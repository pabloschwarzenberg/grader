def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Caso base: una de las palabras es una cadena vacía
    if m == 0 or n == 0:
        return "IB" if abs(m - n) == 1 else "+1"

    # Crear una matriz de tamaño (m+1) x (n+1)
    matriz = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna de la matriz
    for i in range(m + 1):
        matriz[i][0] = i
    for j in range(n + 1):
        matriz[0][j] = j

    # Calcular la distancia Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(matriz[i - 1][j - 1], matriz[i][j - 1], matriz[i - 1][j]) + 1

    # Determinar el resultado según la distancia Levenshtein
    distancia = matriz[m][n]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        return "IB" if m < n else "1S"
    else:
        return "0D"


if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)

    print("Resultado:", resultado)
