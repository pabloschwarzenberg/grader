def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear una matriz de distancias con tamaño (m+1) x (n+1)
    distancia = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna
    for i in range(m + 1):
        distancia[i][0] = i
    for j in range(n + 1):
        distancia[0][j] = j

    # Calcular las distancias
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]
            else:
                distancia[i][j] = min(
                    distancia[i - 1][j] + 1,  # Eliminación
                    distancia[i][j - 1] + 1,  # Inserción
                    distancia[i - 1][j - 1] + 1  # Sustitución
                )

    # Determinar el resultado según la distancia calculada
    if distancia[m][n] > 1:
        return "+1"
    elif distancia[m][n] == 1:
        if m < n:
            return "IB"
        elif m > n:
            return "DB"
        else:
            return "1S"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
