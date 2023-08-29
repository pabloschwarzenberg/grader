def alinear_secuencias(secuencia1, secuencia2):
    longitud_diferencia = len(secuencia1) - len(secuencia2)
    secuencia_alineada = ""

    for i in range(len(secuencia1)):
        if i < len(secuencia2):
            secuencia_alineada += secuencia2[i]
        else:
            secuencia_alineada += "_"

    return secuencia_alineada


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
    print(secuencia_alineada)
