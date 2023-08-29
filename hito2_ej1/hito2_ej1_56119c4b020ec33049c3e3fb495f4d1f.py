def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia1 = 0


    for letra in secuencia1:

        if indice_secuencia1 < len(secuencia2):

            if letra == secuencia2[indice_secuencia1]:
                secuencia_alineada += letra
                indice_secuencia1 += 1
            else:
                secuencia_alineada += "_"
        else:
            secuencia_alineada += "_"


    secuencia_alineada += secuencia2[indice_secuencia1:]

    return secuencia_alineada


secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")


secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

print(secuencia_alineada)





