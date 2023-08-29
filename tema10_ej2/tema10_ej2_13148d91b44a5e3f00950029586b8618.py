def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear una matriz de tamaño (m+1) x (n+1) e inicializarla con ceros
    matriz = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna
    for i in range(m + 1):
        matriz[i][0] = i
    for j in range(n + 1):
        matriz[0][j] = j

    # Calcular la distancia de Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(matriz[i - 1][j], matriz[i][j - 1], matriz[i - 1][j - 1]) + 1

    distancia = matriz[m][n]

    # Determinar el tipo de distancia
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m > n:
            return "IB"
        elif m < n:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"

# Ejemplos de palabras para probar la función
palabra1 = "gato"
palabra2 = "gatito"
print(levenshtein(palabra1, palabra2))  # Debe imprimir: +1

palabra1 = "hola"
palabra2 = "ola"
print(levenshtein(palabra1, palabra2))  # Debe imprimir: 1S

palabra1 = "gallina"
palabra2 = "gallina"
print(levenshtein(palabra1, palabra2))  # Debe imprimir: 0D
           