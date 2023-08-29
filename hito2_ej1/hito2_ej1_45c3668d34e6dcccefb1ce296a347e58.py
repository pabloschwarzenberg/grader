def alinear_secuencias(seceuencia1, secuencia2):
    aligned_secuencia2 = ""
    i = 0
    for base in secuencia1:
        if base == secuencia2[i]:
            aligned_secuencia2 += secuencia2[i]
            i += 1
        else:
            aligned_secuencia2 += "_"
    aligned_secuencia2 += secuencia2[i:]
    return aligned_secuencia2

secuencia1 ="ACCTGGTTCTGTAGTCAGGATTACTA"
secuencia2 ="TGACGTTCAGTAGTCGATT"
print(alinear_secuencias(secuencia1, secuencia2))