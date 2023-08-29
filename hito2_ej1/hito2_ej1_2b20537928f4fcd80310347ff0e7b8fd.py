      def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia1 = 0

    for letra in secuencia2:
        if letra == secuencia1[indice_secuencia1]:
            secuencia_alineada += letra
            indice_secuencia1 += 1
        else:
            secuencia_alineada += "_"

    return secuencia_alineada

secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

print("Resultado del alineamiento:")
print(secuencia_alineada)
