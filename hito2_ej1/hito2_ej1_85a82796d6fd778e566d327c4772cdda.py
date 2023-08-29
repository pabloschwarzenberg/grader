def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    i = 0
    for nucleotido in secuencia1:
        if nucleotido == secuencia2[i]:
            secuencia_alineada += secuencia2[i]
            i += 1
        else:
            secuenciaalineada += "_"

    secuencia_alineada += secuencia2[i:]
    return secuencia_alineada


secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")


secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)


print(secuencia_alineada)
