def alinear(secuencia1, secuencia2):
    i = 0
    j = 0
    resultado = ""
    while i < len(secuencia1) and j < len(secuencia2):
        if secuencia1[i] == secuencia2[j]:
            resultado += secuencia2[j]
            j += 1
        else:
            resultado += "_"
        i += 1
    resultado += secuencia2[j:]
    return resultado

secuencia1 = "ACCTGGTTCTGTAGTCAGGATTACTA"
secuencia2 = "TGACGTTCAGTAGTCGATT"

print(alinear(secuencia1, secuencia2))     