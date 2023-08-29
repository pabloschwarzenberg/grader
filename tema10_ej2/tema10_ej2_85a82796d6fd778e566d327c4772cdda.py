def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear una matriz para almacenar las distancias
    matriz = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna
    for i in range(m + 1):
        matriz[i][0] = i
    for j in range(n + 1):
        matriz[0][j] = j

    # Calcular las distancias
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(
                    matriz[i - 1][j] + 1,  # Eliminación
                    matriz[i][j - 1] + 1,  # Inserción
                    matriz[i - 1][j - 1] + 1  # Sustitución
                )

    # Determinar el resultado según la distancia calculada
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
