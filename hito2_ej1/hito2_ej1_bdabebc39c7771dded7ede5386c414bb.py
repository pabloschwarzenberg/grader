def alinear_secuencias(seq1, seq2):
   
    m = len(seq1)
    n = len(seq2)
    puntuaciones = [[0] * (n+1) for _ in range(m+1)]

   
    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                puntuaciones[i][j] = puntuaciones[i-1][j-1] + 1
            else:
                puntuaciones[i][j] = max(puntuaciones[i-1][j], puntuaciones[i][j-1])

   
    secuencia_alineada = ''
    i = m
    j = n

    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1]:
            secuencia_alineada = seq2[j-1] + secuencia_alineada
            i -= 1
            j -= 1
        elif puntuaciones[i-1][j] >= puntuaciones[i][j-1]:
            secuencia_alineada = '_' + secuencia_alineada
            i -= 1
        else:
            secuencia_alineada = seq2[j-1] + secuencia_alineada
            j -= 1

    while j > 0:
        secuencia_alineada = seq2[j-1] + secuencia_alineada
        j -= 1

    return secuencia_alineada

if __name__ == "__main__":
    seq1 = input("Ingrese la primera secuencia de ADN: ")
    seq2 = input("Ingrese la segunda secuencia de ADN: ")

    secuencia_alineada = alinear_secuencias(seq1, seq2)
    print(secuencia_alineada)
