def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia1 = 0

    for caracter in secuencia2:
        if caracter == secuencia1[indice_secuencia1]:
            secuencia_alineada += caracter
            indice_secuencia1 += 1
        else:
            secuencia_alineada += "_"

    return secuencia_alineada

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")

    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

    print(secuencia_alineada)
      