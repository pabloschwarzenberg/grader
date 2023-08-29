def alinear_secuencias(secuencia1, secuencia2):
    indice = 0
    secuencia_alineada = ""
    for nucleotido in secuencia1:
        if nucleotido == secuencia2[indice]:
            secuencia_alineada += secuencia2[indice]
            indice += 1
        else:
            secuencia_alineada += "_"
    secuencia_alineada += secuencia2[indice:]
    return secuencia_alineada
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
print(secuencia_alineada)
