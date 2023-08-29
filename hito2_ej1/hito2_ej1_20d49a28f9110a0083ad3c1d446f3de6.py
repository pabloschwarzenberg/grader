def alinear_secuencias(secuencia1, secuencia2):
    s_alineada = ""
    i_secuencia2 = 0

    for caracter in secuencia1:
        if caracter == secuencia2[i_secuencia2]:
            s_alineada += secuencia2[i_secuencia2]
            i_secuencia2 += 1
        else:
            s_alineada += "_"

    s_alineada += secuencia2[i_secuencia2:]

    return s_alineada


secuencia1 = "ACCTGGTTCTGTAGTCAGGATTACTA"
secuencia2 = "TGACGTTCAGTAGTCGATT"
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
print(secuencia_alineada)
      