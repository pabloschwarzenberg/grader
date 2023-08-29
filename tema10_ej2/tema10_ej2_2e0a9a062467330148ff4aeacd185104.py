def levenshtein(word1, word2):
    if word1 == word2:
        return "0D"  # Las palabras son iguales

    m = len(word1)
    n = len(word2)

    # Creamos una matriz de distancias con una fila y una columna adicional para los casos base
    distances = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializamos la primera columna con valores consecutivos de 0 a m
    for i in range(m + 1):
        distances[i][0] = i

    # Inicializamos la primera fila con valores consecutivos de 0 a n
    for j in range(n + 1):
        distances[0][j] = j

    # Calculamos las distancias
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                distances[i][j] = 1 + min(distances[i - 1][j], distances[i][j - 1], distances[i - 1][j - 1])

    # Determinamos el tipo de distancia
    if distances[m][n] > 1:
        return "+1"  # La distancia es mayor que 1
    elif distances[m][n] == 1:
        if m > n or n > m:
            return "IB"  # La distancia es 1 y se requiere insertar o borrar una letra
        else:
            return "1S"  # La distancia es 1 y se requiere sustituir una letra
