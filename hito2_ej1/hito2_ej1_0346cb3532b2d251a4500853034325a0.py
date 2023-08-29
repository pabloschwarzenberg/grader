def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""

    i = 0
    j = 0

    while i < len(secuencia1) and j < len(secuencia2):
        if secuencia1[i] == secuencia2[j]:
            secuencia_alineada += secuencia2[j]
            i += 1
            j += 1
        else:
            secuencia_alineada += "_"
            i += 1

    if i < len(secuencia1):
        secuencia_alineada += "_" * (len(secuencia1) - i)

    return secuencia_alineada

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

    print(secuencia_alineada)
