def alinear_secuencias(adn1, adn2):
    # Calcula la longitud de las secuencias de ADN
    len_adn1 = len(adn1)
    len_adn2 = len(adn2)

    # Crea una matriz para almacenar los puntajes de alineamiento
    matriz_puntajes = [[0] * (len_adn2 + 1) for _ in range(len_adn1 + 1)]

    # Rellena la primera fila y la primera columna de la matriz de puntajes
    for i in range(len_adn1 + 1):
        matriz_puntajes[i][0] = i
    for j in range(len_adn2 + 1):
        matriz_puntajes[0][j] = j

    # Calcula los puntajes de alineamiento para llenar la matriz
    for i in range(1, len_adn1 + 1):
        for j in range(1, len_adn2 + 1):
            if adn1[i - 1] == adn2[j - 1]:
                puntaje_diagonal = matriz_puntajes[i - 1][j - 1]
            else:
                puntaje_diagonal = matriz_puntajes[i - 1][j - 1] + 1
            puntaje_superior = matriz_puntajes[i - 1][j] + 1
            puntaje_izquierdo = matriz_puntajes[i][j - 1] + 1
            matriz_puntajes[i][j] = min(puntaje_diagonal, puntaje_superior, puntaje_izquierdo)

    # Reconstruye el alineamiento insertando caracteres '_' en la segunda secuencia
    alineamiento = ""
    i = len_adn1
    j = len_adn2
    while i > 0 and j > 0:
        if adn1[i - 1] == adn2[j - 1]:
            alineamiento = adn2[j - 1] + alineamiento
            i -= 1
            j -= 1
        elif matriz_puntajes[i][j] == matriz_puntajes[i - 1][j - 1] + 1:
            alineamiento = "_" + alineamiento
            i -= 1
            j -= 1
        elif matriz_puntajes[i][j] == matriz_puntajes[i - 1][j] + 1:
            alineamiento = adn1[i - 1] + alineamiento
            i -= 1
        else:
            alineamiento = "_" + alineamiento
            j -= 1

    # Si una secuencia es más larga que la otra, agrega caracteres '_' al inicio
    while i > 0:
        alineamiento = adn1[i - 1] + alineamiento
        i -= 1
    while j > 0:
        alineamiento = "_" + alineamiento
        j -= 1

    return alineamiento


# Ejemplo de uso
secuencia1 = "ACGTACGT"
secuencia2 = "ATCG"
resultado = alinear_secuencias(secuencia1, secuencia2)
print(resultado)


