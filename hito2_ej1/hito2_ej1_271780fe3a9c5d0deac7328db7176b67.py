def alinear_secuencias(secuencia1, secuencia2):
    secuencia_al = ""
    indice_segunda_secuencia = 0

    for caracter in secuencia1:
        if caracter == secuencia2[indice_segunda_secuencia]:
            secuencia_al += secuencia2[indice_segunda_secuencia]
            indice_segunda_secuencia += 1
        else:
            secuencia_al += "_"

    secuencia_al += secuencia2[indice_segunda_secuencia:]

    return secuencia_al


secuencia1 = "ACCTGGTTCTGTAGTCAGGATTACTA"
secuencia2 = "TGACGTTCAGTAGTCGATT"
secuencia_al = alinear_secuencias(secuencia1, secuencia2)
print(secuencia_al)
         