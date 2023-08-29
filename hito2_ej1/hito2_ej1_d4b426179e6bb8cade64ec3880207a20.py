def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice_secuencia1 = 0

    for caracter in secuencia2:
        if caracter == secuencia1[indice_secuencia1]:
            alineacion += caracter
            indice_secuencia1 += 1
        else:
            alineacion += "_"

    return alineacion


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")

    alineacion = alinear_secuencias(secuencia1, secuencia2)
    print(alineacion)