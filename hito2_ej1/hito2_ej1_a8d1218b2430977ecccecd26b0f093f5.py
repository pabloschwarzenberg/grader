def alinear_secuencias(secuencia1, secuencia2):
    alineada = ""
    i = 0
    for letra in secuencia1:
        if letra == secuencia2[i]:
            alineada += letra
            i += 1
        else:
            alineada += "_"

    return alineada

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")
    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
    print(secuencia_alineada)
