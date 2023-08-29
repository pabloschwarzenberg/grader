def levenshtein(palabra1, palabra2):
    # Si las palabras son iguales, retornar 0D
    if palabra1 == palabra2:
        return "0D"
    
    # Inicializar matriz de distancias
    m = [[0] * (len(palabra2) + 1) for _ in range(len(palabra1) + 1)]
    
    # Inicializar primera fila y primera columna de la matriz
    for i in range(1, len(palabra1) + 1):
        m[i][0] = i
    for j in range(1, len(palabra2) + 1):
        m[0][j] = j
    
    # Calcular distancias
    for i in range(1, len(palabra1) + 1):
        for j in range(1, len(palabra2) + 1):
            if palabra1[i-1] == palabra2[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = min(m[i-1][j], m[i][j-1], m[i-1][j-1]) + 1
    
    # Retornar resultado según la distancia
    distancia = m[-1][-1]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if len(palabra1) < len(palabra2):
            return "IB"
        elif len(palabra1) > len(palabra2):
            return "IB"
        else:
            return "1S"
    else:
        return "0D"
