def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)
    
    # matriz para almacenar los valores de la distancia Levenshtein
    distancia = [[0 for x in range(n + 1)] for y in range(m + 1)]
    
    # inicializamos la primera fila y la primera columna
    for i in range(m + 1):
        distancia[i][0] = i
        
    for j in range(n + 1):
        distancia[0][j] = j
        
    # calculamos la distancia Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]
            else:
                distancia[i][j] = 1 + min(distancia[i][j - 1],        # inserción
                                          distancia[i - 1][j],        # eliminación
                                          distancia[i - 1][j - 1])    # sustitución
    
    # devolvemos el resultado correspondiente a la distancia Levenshtein
    if distancia[m][n] > 1:
        return "+1"
    elif distancia[m][n] == 1:
        if m > n or m < n:
            return "IB"    # inserción o eliminación
        else:
            return "1S"    # sustitución
    else:
        return "0D"        # son iguales






















