def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Creamos una matriz de tamaño (m+1) x (n+1) para almacenar las distancias
    distancias = [[0] * (n+1) for _ in range(m+1)]

    # Inicializamos la primera columna con los valores de 0 a m
    for i in range(m+1):
        distancias[i][0] = i

    # Inicializamos la primera fila con los valores de 0 a n
    for j in range(n+1):
        distancias[0][j] = j

    # Llenamos la matriz de distancias
    for i in range(1, m+1):
        for j in range(1, n+1):
            # Si los caracteres son iguales, la distancia es igual a la diagonal superior izquierda
            if palabra1[i-1] == palabra2[j-1]:
                distancias[i][j] = distancias[i-1][j-1]
            else:
                # Si los caracteres son diferentes, la distancia es el mínimo de las operaciones posibles
                distancias[i][j] = min(distancias[i-1][j] + 1,     # Eliminación
                                       distancias[i][j-1] + 1,     # Inserción
                                       distancias[i-1][j-1] + 1)   # Sustitución

    # Obtenemos la distancia Levenshtein entre las palabras
    distancia = distancias[m][n]

    # Determinamos el tipo de resultado según la distancia obtenida
    if distancia > 1:
        resultado = "+1"
    elif distancia == 1:
        if m > n:
            resultado = "IB"  # Insertar o borrar una letra
        else:
            resultado = "1S"  # Sustituir una letra
    else:
        resultado = "0D"  # Palabras iguales

    return resultado