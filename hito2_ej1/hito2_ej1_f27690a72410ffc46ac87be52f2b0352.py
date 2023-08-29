def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""

    for i in range(len(secuencia1)):
        if i < len(secuencia2) and secuencia1[i] == secuencia2[i]:
            secuencia_alineada += secuencia2[i]
        else:
            secuencia_alineada += "_"

    if len(secuencia2) > len(secuencia1):
        secuencia_alineada += secuencia2[len(secuencia1):]

    return secuencia_alineada


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
    print(secuencia_alineada)
