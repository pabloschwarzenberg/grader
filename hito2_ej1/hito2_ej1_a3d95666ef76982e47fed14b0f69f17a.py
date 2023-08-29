def alinear_secuencias(secuencia1, secuencia2):
    alineada = ""

    for base1, base2 in zip(secuencia1, secuencia2):
        if base1 != base2:
            alineada += "_"
        else:
            alineada += base2

    if len(secuencia1) > len(secuencia2):
        alineada += "_" * (len(secuencia1) - len(secuencia2))

    return alineada


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    resultado = alinear_secuencias(secuencia1, secuencia2)
    print(resultado)
