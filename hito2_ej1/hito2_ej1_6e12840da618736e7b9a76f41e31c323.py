def alinear_secuencias(secuencia1, secuencia2):
    # Longitud de las secuencias
    len_seq1 = len(secuencia1)
    len_seq2 = len(secuencia2)
    
    # Crear una matriz para el alineamiento
    matriz = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]
    
    # Llenar la primera fila y la primera columna de la matriz
    for i in range(len_seq1 + 1):
        matriz[i][0] = i
    for j in range(len_seq2 + 1):
        matriz[0][j] = j
    
    # Calcular la matriz de alineamiento
    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            if secuencia1[i - 1] == secuencia2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(matriz[i - 1][j] + 1, matriz[i][j - 1] + 1)
    
    # Construir el alineamiento
    alineacion = ""
    i = len_seq1
    j = len_seq2
    while i > 0 and j > 0:
        if secuencia1[i - 1] == secuencia2[j - 1]:
            alineacion = secuencia2[j - 1] + alineacion
            i -= 1
            j -= 1
        elif matriz[i][j] == matriz[i - 1][j] + 1:
            alineacion = "_" + alineacion
            i -= 1
        else:
            alineacion = secuencia2[j - 1] + alineacion
            j -= 1
    
    # Si quedan caracteres en la segunda secuencia, agregarlos al inicio
    while j > 0:
        alineacion = secuencia2[j - 1] + alineacion
        j -= 1
    
    return alineacion

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")
    alineacion = alinear_secuencias(secuencia1, secuencia2)
    print(alineacion)
