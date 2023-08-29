def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    i = 0
    j = 0

    while i < len(secuencia1) and j < len(secuencia2):
        if secuencia1[i] == secuencia2[j]:
            alineacion += secuencia1[i]
            i += 1
            j += 1
        else:
            alineacion += "_"
            i += 1

    if i < len(secuencia1):
        alineacion += "_" * (len(secuencia1) - i)

    if j < len(secuencia2):
        alineacion += secuencia2[j:]

    return alineacion

# Ejemplo de uso
secuencia1 = "ACCTGGTTCTGTAGTCAGGATTACTA"
secuencia2 = "TGACGTTCAGTAGTCGATT"

resultado = alinear_secuencias(secuencia1, secuencia2)
print(resultado)
      