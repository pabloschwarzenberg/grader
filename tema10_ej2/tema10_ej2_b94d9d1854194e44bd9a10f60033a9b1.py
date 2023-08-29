def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Caso base: si una de las palabras es vacía, la distancia es igual a la longitud de la otra palabra
    if m == 0:
        return n
    if n == 0:
        return m

    # Creamos una matriz para almacenar los cálculos intermedios
    matriz = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializamos la primera fila y la primera columna de la matriz
    for i in range(m + 1):
        matriz[i][0] = i
    for j in range(n + 1):
        matriz[0][j] = j

    # Calculamos la distancia de Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                insercion = matriz[i][j - 1]
                eliminacion = matriz[i - 1][j]
                sustitucion = matriz[i - 1][j - 1]
                matriz[i][j] = min(insercion, eliminacion, sustitucion) + 1

    # Obtenemos la distancia de Levenshtein final
    distancia = matriz[m][n]

    # Determinamos el resultado según la distancia obtenida
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m > n:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"
