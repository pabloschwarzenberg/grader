def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    i = 0
    j = 0


    while i < len(secuencia1):
        if j < len(secuencia2) and secuencia1[i] == secuencia2[j]:
            secuencia_alineada += secuencia2[j]
            j += 1
        else:
            secuencia_alineada += "_"
        i += 1


    while j < len(secuencia2):
        secuencia_alineada += secuencia2[j]
        j += 1

    return secuencia_alineada


secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")


secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)


print(secuencia_alineada)      