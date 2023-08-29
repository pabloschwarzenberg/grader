def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear una matriz de distancias con tamaño (m+1) x (n+1)
    distancias = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna
    for i in range(m + 1):
        distancias[i][0] = i
    for j in range(n + 1):
        distancias[0][j] = j

    # Calcular las distancias mínimas
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancias[i][j] = distancias[i - 1][j - 1]
            else:
                distancias[i][j] = min(distancias[i - 1][j], distancias[i][j - 1], distancias[i - 1][j - 1]) + 1

    # Obtener la distancia mínima entre las palabras
    distancia_minima = distancias[m][n]

    # Determinar el resultado según la distancia mínima
    if distancia_minima > 1:
        return "+1"
    elif distancia_minima == 1:
        if m > n:
            return "IB"
        elif m < n:
            return "IB"
        else:
            return "1S"
    elif distancia_minima == 0:
        return "0D"

# Ejemplo de uso
if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print(resultado)